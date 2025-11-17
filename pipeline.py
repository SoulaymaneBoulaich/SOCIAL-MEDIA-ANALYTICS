import schedule
import time
import pandas as pd
from collect_data import collect_reddit_posts
from collect_youtube import collect_youtube_comments
from process_data import process_data
from sentiment_analysis import analyze_data
from database import SocialMediaDB

def get_user_preferences():
    """
    Ask user which platforms to extract from and what queries to use.
    """
    print("\n" + "="*60)
    print("📋 DATA EXTRACTION PREFERENCES")
    print("="*60)
    
    preferences = {
        'reddit': False,
        'youtube': False,
        'reddit_query': None,
        'youtube_query': None,
        'limit': 50
    }
    
    # Ask which platforms to extract from
    print("\nWhich platforms would you like to extract data from?")
    reddit_choice = input("Extract from Reddit? (y/n): ").strip().lower()
    preferences['reddit'] = reddit_choice == 'y'
    
    youtube_choice = input("Extract from YouTube? (y/n): ").strip().lower()
    preferences['youtube'] = youtube_choice == 'y'
    
    # Check if at least one platform is selected
    if not any([preferences['reddit'], preferences['youtube']]):
        print("\n⚠ No platforms selected. Exiting...")
        return None
    
    # Set limit
    limit_input = input("\nHow many items to collect per platform? (default: 50): ").strip()
    preferences['limit'] = int(limit_input) if limit_input.isdigit() else 50
    
    # Get queries for selected platforms
    if preferences['reddit']:
        reddit_query = input("Enter Reddit subreddit name (default: 'datascience'): ").strip()
        preferences['reddit_query'] = reddit_query if reddit_query else 'datascience'
    
    if preferences['youtube']:
        youtube_query = input("Enter YouTube search query (default: 'machine learning'): ").strip()
        preferences['youtube_query'] = youtube_query if youtube_query else 'machine learning'
    
    return preferences

def run_pipeline(preferences=None):
    """
    This is the main function that runs everything:
    1. Collects data from selected platforms
    2. Processes and cleans the data
    3. Analyzes sentiment
    4. Stores everything in the database
    """
    if preferences is None:
        preferences = get_user_preferences()
        if preferences is None:
            return
    
    print("\n" + "="*60)
    print("🚀 STARTING PIPELINE RUN")
    print("="*60)
    
    # ====== STEP 1: COLLECT DATA ======
    print("\n📥 Step 1: Collecting data from selected platforms...")
    
    dfs = []
    
    # Collect from Reddit if selected
    if preferences['reddit']:
        print(f"\n🔴 Extracting from Reddit (r/{preferences['reddit_query']})...")
        df_reddit = collect_reddit_posts(preferences['reddit_query'], limit=preferences['limit'])
        dfs.append(df_reddit)
        print(f"   ✓ Collected {len(df_reddit)} posts")
    else:
        df_reddit = pd.DataFrame()
    
    # Collect from YouTube if selected
    if preferences['youtube']:
        print(f"\n▶️ Extracting from YouTube ('{preferences['youtube_query']}')...")
        df_youtube = collect_youtube_comments(preferences['youtube_query'], limit=preferences['limit'])
        dfs.append(df_youtube)
        print(f"   ✓ Collected {len(df_youtube)} comments")
    else:
        df_youtube = pd.DataFrame()
    
    # Combine all data into one DataFrame
    if dfs:
        df_all = pd.concat(dfs, ignore_index=True)
    else:
        df_all = pd.DataFrame()
    
    print(f"\n📊 Total collected: {len(df_all)} posts")
    print(f"   - Reddit: {len(df_reddit)} posts")
    print(f"   - YouTube: {len(df_youtube)} comments")
    
    if df_all.empty:
        print("⚠ No data collected. Exiting...")
        return
    
    # ====== STEP 2: PROCESS DATA ======
    print("\n⚙ Step 2: Processing and cleaning data...")
    df_processed = process_data(df_all)
    
    if df_processed.empty:
        print("⚠ No data after processing. Exiting...")
        return
    
    # ====== STEP 3: ANALYZE SENTIMENT ======
    print("\n🔍 Step 3: Analyzing sentiment...")
    df_analyzed = analyze_data(df_processed)
    
    # ====== STEP 4: STORE IN DATABASE ======
    print("\n💾 Step 4: Storing in database...")
    
    # Select only the columns we want in the database
    db_columns = [
        'id', 'platform', 'title', 'text', 'author', 'created_utc',
        'score', 'num_comments', 'url', 'sentiment_score', 'sentiment_label'
    ]
    
    df_to_insert = pd.DataFrame()
    for col in db_columns:
        df_to_insert[col] = df_analyzed[col] if col in df_analyzed.columns else None
    
    # Create new database with timestamp
    db = SocialMediaDB()
    db.insert_posts(df_to_insert)
    
    # Log extraction details
    if preferences['reddit']:
        db.log_extraction('reddit', preferences['reddit_query'], len(df_reddit))
    if preferences['youtube']:
        db.log_extraction('youtube', preferences['youtube_query'], len(df_youtube))
    
    # Display summary statistics
    print("\n" + "="*60)
    print("📊 SUMMARY STATISTICS")
    print("="*60)
    stats_df = db.get_summary_stats()
    if not stats_df.empty:
        for idx, row in stats_df.iterrows():
            print(f"\n{row['platform'].upper()}:")
            print(f"   Total Posts: {row['total_posts']}")
            print(f"   Avg Sentiment: {row['avg_sentiment']:.3f}")
            print(f"   😊 Positive: {row['positive_count']} | 😐 Neutral: {row['neutral_count']} | 😞 Negative: {row['negative_count']}")
            print(f"   Avg Score: {row['avg_score']:.1f} | Avg Comments: {row['avg_comments']:.1f}")
    
    print("\n" + "="*60)
    print("✅ PIPELINE COMPLETE!")
    print(f"📁 Database saved as: {db.db_name}")
    print("="*60 + "\n")

if __name__ == "__main__":
    # Get user preferences for what to extract
    user_prefs = get_user_preferences()
    
    if user_prefs is None:
        print("\nExiting...")
        exit()
    
    # Run the pipeline with user preferences
    run_pipeline(user_prefs)
    
    # Ask if user wants to schedule recurring runs
    schedule_choice = input("\nWould you like to schedule this pipeline to run automatically? (y/n): ").strip().lower()
    
    if schedule_choice == 'y':
        frequency = input("How often should it run? (6 = 6 hours, 12 = 12 hours, 24 = daily): ").strip()
        try:
            hours = int(frequency)
            schedule.every(hours).hours.do(run_pipeline, user_prefs)
            print(f"\n⏰ Pipeline scheduled to run every {hours} hours")
            print("Press Ctrl+C to stop\n")
            
            # Keep the script running and check for scheduled tasks
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except ValueError:
            print("Invalid input. Pipeline will not be scheduled.")
    else:
        print("\n✅ Done! Pipeline completed successfully.")

