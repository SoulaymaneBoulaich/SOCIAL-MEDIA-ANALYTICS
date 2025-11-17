"""Smoke test for dashboard helper functions.

This script loads the most recent social_media_*.db and runs the dashboard
figure/table creators to ensure they execute without exception.
"""
import os
import glob
import sys
from database import SocialMediaDB
import dashboard

def find_latest_db():
    dbs = sorted(glob.glob('social_media_*.db'), reverse=True)
    return dbs[0] if dbs else None

def main():
    db_file = find_latest_db()
    if not db_file:
        print('No social_media_*.db files found in current directory.')
        sys.exit(1)

    print(f'Using DB: {db_file}')
    db = SocialMediaDB(db_file)
    df = db.get_all_posts()

    # Run each dashboard creator
    try:
        fig1 = dashboard.create_sentiment_by_platform(df)
        fig2 = dashboard.create_sentiment_timeline(df)
        fig3 = dashboard.create_platform_pie(df)
        table = dashboard.create_top_posts_table(df)
    except Exception as e:
        print('Smoke test FAILED: exception while creating visuals:')
        raise

    print('Smoke test PASSED: all dashboard creators ran successfully')

if __name__ == '__main__':
    main()
