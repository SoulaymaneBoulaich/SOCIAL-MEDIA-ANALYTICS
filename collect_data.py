import praw
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# CONNECT TO REDDIT API
try:
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )

    # TEST IF CONNECTION WORKS
    reddit.user.me()
    print("REDDIT API CONNECTED SUCCESSFULLY!")

except Exception as e:
    print(f"REDDIT API ERROR: {e}")
    print("CHECK YOUR .env FILE AND REDDIT API CREDENTIALS")
    reddit = None

def collect_reddit_posts(subreddit_name, limit=1000):
    if not reddit:
        print("REDDIT CLIENT NOT INITIALIZED")
        return pd.DataFrame()
    
    print(f"COLLECTING POSTS FROM r/{subreddit_name}...")
    posts_data = []

    try:
        subreddit = reddit.subreddit(subreddit_name)

        for post in subreddit.hot(limit=limit):
            posts_data.append({
                'id': post.id,
                'platform': 'reddit',
                'title': post.title,
                'text': post.selftext,
                'score': post.score,
                'num_comments': post.num_comments,
                'created_utc': datetime.fromtimestamp(post.created_utc),
                'author': str(post.author),
                'url': post.url
            })
    except Exception as e:
        print(f"ERROR COLLECTING REDDIT POSTS: {e}")
        return pd.DataFrame()
    
    df = pd.DataFrame(posts_data)
    print(f"COLLECTED {len(df)} REDDIT POSTS")
    return df

if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")  # Change only this
    df = collect_reddit_posts(subreddit_name, limit=500)
    
    if not df.empty:
        filename = f"reddit_{subreddit_name}.csv"
        df.to_csv(filename, index=False)
        print(f"SAVED TO {filename}")

    