"""Repair summary_stats numeric columns in existing social_media_*.db files.

This script finds all databases named `social_media_*.db` in the current
directory, reads their `summary_stats` table, converts any binary/blob fields
to native ints/floats where appropriate, and rewrites the corrected rows.
"""
import glob
import sqlite3
import pandas as pd
import os

NUMERIC_COLUMNS = ['total_posts', 'avg_sentiment', 'positive_count', 'negative_count', 'neutral_count', 'avg_score', 'avg_comments']

def fix_db(db_path):
    conn = sqlite3.connect(db_path)
    try:
        df = pd.read_sql_query('SELECT * FROM summary_stats', conn)
    except Exception as e:
        print(f'No summary_stats table in {db_path}: {e}')
        conn.close()
        return

    if df.empty:
        print(f'No rows to fix in {db_path}')
        conn.close()
        return

    # Convert columns if they are bytes
    updated = False
    for col in NUMERIC_COLUMNS:
        if col in df.columns:
            def _to_native(x):
                try:
                    if isinstance(x, (bytes, bytearray)):
                        # little-endian int/float from sqlite BLOB; attempt int first
                        try:
                            return int.from_bytes(x, byteorder='little')
                        except Exception:
                            try:
                                return float(x)
                            except Exception:
                                return x
                    return x
                except Exception:
                    return x

            newcol = df[col].apply(_to_native)
            if not newcol.equals(df[col]):
                df[col] = newcol
                updated = True

    if updated:
        # Write back: simple approach - delete all rows and reinsert
        cur = conn.cursor()
        cur.execute('DELETE FROM summary_stats')
        conn.commit()

        insert_cols = [c for c in df.columns if c != 'id']
        for _, row in df.iterrows():
            vals = [row[c] for c in insert_cols]
            placeholders = ','.join(['?'] * len(vals))
            cur.execute(f'INSERT INTO summary_stats ({",".join(insert_cols)}) VALUES ({placeholders})', vals)
        conn.commit()
        print(f'Fixed numeric types in {db_path}')
    else:
        print(f'No changes needed for {db_path}')

    conn.close()

def main():
    dbs = sorted(glob.glob('social_media_*.db'))
    if not dbs:
        print('No social_media_*.db files found in current directory.')
        return
    for db in dbs:
        fix_db(db)

if __name__ == '__main__':
    main()
