import sqlite3
import pandas as pd
from datetime import datetime
import os


class SocialMediaDB:
    """
    THIS CLASS HANDLES ALL DATABASE OPERATIONS.
    IT CREATES SEPARATE DATABASES FOR EACH RUN WITH MULTIPLE TABLES FOR EACH PLATFORM.
    """
    def __init__(self, db_name=None):
        # If no db_name provided, create one with timestamp
        if db_name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            db_name = f"social_media_{timestamp}.db"
        
        self.db_name = db_name
        self.db_path = os.path.join(os.getcwd(), db_name)
        print(f"\n📁 Database: {self.db_name}")
        self.create_tables()
    
    def create_tables(self):
        """CREATE SEPARATE TABLES FOR EACH PLATFORM AND SUMMARY TABLE."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Reddit Posts Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reddit_posts(
                id TEXT PRIMARY KEY,
                title TEXT,
                text TEXT,
                author TEXT,
                created_utc TIMESTAMP,
                score INTEGER,
                num_comments INTEGER,
                url TEXT,
                sentiment_score REAL,
                sentiment_label TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')
        
        # YouTube Comments Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS youtube_posts(
                id TEXT PRIMARY KEY,
                title TEXT,
                text TEXT,
                author TEXT,
                created_utc TIMESTAMP,
                score INTEGER,
                num_comments INTEGER,
                url TEXT,
                sentiment_score REAL,
                sentiment_label TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')
        
        # Summary Statistics Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS summary_stats(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                total_posts INTEGER,
                avg_sentiment REAL,
                positive_count INTEGER,
                negative_count INTEGER,
                neutral_count INTEGER,
                avg_score REAL,
                avg_comments REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')
        
        # Session Log Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS session_log(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT,
                query TEXT,
                items_collected INTEGER,
                extraction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')
        
        conn.commit()
        conn.close()
        print('✓ All tables created successfully.')
    
    def insert_posts(self, df):
        """INSERT POSTS INTO APPROPRIATE TABLES BASED ON PLATFORM."""
        if df.empty:
            print("⚠ No new posts to insert.")
            return
        
        conn = sqlite3.connect(self.db_path)
        
        try:
            # Separate data by platform
            reddit_df = df[df['platform'] == 'reddit'] if 'platform' in df.columns else pd.DataFrame()
            youtube_df = df[df['platform'] == 'youtube'] if 'platform' in df.columns else pd.DataFrame()
            
            # Insert Reddit posts
            if not reddit_df.empty:
                reddit_df_clean = reddit_df.drop('platform', axis=1, errors='ignore')
                reddit_df_clean.to_sql('reddit_posts', conn, if_exists='append', index=False)
                print(f"   ✓ Inserted {len(reddit_df)} Reddit posts")
            # Insert YouTube posts
            if not youtube_df.empty:
                youtube_df_clean = youtube_df.drop('platform', axis=1, errors='ignore')
                youtube_df_clean.to_sql('youtube_posts', conn, if_exists='append', index=False)
                print(f"   ✓ Inserted {len(youtube_df)} YouTube posts")
            
            # Remove duplicates from each table
            self._remove_duplicates(conn)
            
            # Generate and insert summary statistics
            self._insert_summary_stats(conn, df)
            
            conn.commit()
            print(f"\n✅ Total {len(df)} posts successfully stored in database!")
            
        except Exception as e:
            print(f"❌ Error inserting posts: {e}")
            conn.rollback()
        finally:
            conn.close()
    
    def _remove_duplicates(self, conn):
        """REMOVE DUPLICATE POSTS FROM EACH TABLE."""
        tables = ['reddit_posts', 'youtube_posts']
        for table in tables:
            try:
                conn.execute(f'''
                    DELETE FROM {table}
                    WHERE rowid NOT IN (
                        SELECT MIN(rowid)
                        FROM {table}
                        GROUP BY id)''')
            except:
                pass  # Table might not exist yet
    
    def _insert_summary_stats(self, conn, df):
        """INSERT SENTIMENT SUMMARY STATISTICS BY PLATFORM."""
        platforms = df['platform'].unique() if 'platform' in df.columns else []
        
        for platform in platforms:
            platform_df = df[df['platform'] == platform]
            
            if platform_df.empty:
                continue
            
            # Convert any numpy/pandas dtypes to native Python types to avoid
            # sqlite storing them as BLOBs. Use explicit ordering for clarity.
            total_posts = int(len(platform_df))
            avg_sentiment = float(platform_df['sentiment_score'].mean()) if 'sentiment_score' in platform_df.columns else 0.0
            positive_count = int((platform_df['sentiment_label'] == 'positive').sum()) if 'sentiment_label' in platform_df.columns else 0
            negative_count = int((platform_df['sentiment_label'] == 'negative').sum()) if 'sentiment_label' in platform_df.columns else 0
            neutral_count = int((platform_df['sentiment_label'] == 'neutral').sum()) if 'sentiment_label' in platform_df.columns else 0
            avg_score = float(platform_df['score'].mean()) if 'score' in platform_df.columns else 0.0
            avg_comments = float(platform_df['num_comments'].mean()) if 'num_comments' in platform_df.columns else 0.0

            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO summary_stats 
                (platform, total_posts, avg_sentiment, positive_count, negative_count, neutral_count, avg_score, avg_comments)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (platform, total_posts, avg_sentiment, positive_count, negative_count, neutral_count, avg_score, avg_comments))
    
    def log_extraction(self, platform, query, items_collected):
        """LOG EXTRACTION DETAILS TO SESSION LOG."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO session_log (platform, query, items_collected)
            VALUES (?, ?, ?)
        ''', (platform, query, items_collected))
        
        conn.commit()
        conn.close()
    
    def get_all_posts(self, platform=None):
        """RETRIEVE POSTS FROM DATABASE BY PLATFORM OR ALL."""
        conn = sqlite3.connect(self.db_path)
        try:
            if platform:
                table_name = f"{platform}_posts"
                df = pd.read_sql_query(f'SELECT * FROM {table_name}', conn)
            else:
                # Get all posts from all tables
                reddit_df = pd.read_sql_query('SELECT * FROM reddit_posts', conn)
                youtube_df = pd.read_sql_query('SELECT * FROM youtube_posts', conn)
                
                # Add platform column
                reddit_df['platform'] = 'reddit'
                youtube_df['platform'] = 'youtube'
                
                df = pd.concat([reddit_df, youtube_df], ignore_index=True)
        except Exception as e:
            print(f"Error retrieving posts: {e}")
            df = pd.DataFrame()
        finally:
            conn.close()
        return df
    
    def get_summary_stats(self):
        """RETRIEVE SUMMARY STATISTICS."""
        conn = sqlite3.connect(self.db_path)
        try:
            df = pd.read_sql_query('SELECT * FROM summary_stats', conn)
        except Exception as e:
            print(f"Error retrieving statistics: {e}")
            df = pd.DataFrame()
        finally:
            conn.close()
        return df
    
    def list_databases(self):
        """LIST ALL SOCIAL MEDIA DATABASES IN CURRENT DIRECTORY."""
        db_files = [f for f in os.listdir() if f.startswith('social_media_') and f.endswith('.db')]
        return sorted(db_files, reverse=True)  # Most recent first