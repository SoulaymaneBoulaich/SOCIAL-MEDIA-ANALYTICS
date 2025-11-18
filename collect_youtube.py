import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load API keys
load_dotenv()

def collect_youtube_comments(query, limit=1000):
    """
    Collect comments from YouTube videos matching a search query.
    
    Args:
        query: What to search for (e.g., 'python tutorial')
        limit: Maximum number of comments to collect
    
    Returns:
        DataFrame with comment data
    """
    print(f"[YOUTUBE] Collecting YouTube comments for: '{query}'...")
    
    # Build YouTube API client
    try:
        youtube = build('youtube', 'v3', developerKey=os.getenv('YOUTUBE_API_KEY'))
        print("[OK] YouTube API connected successfully!")
    except Exception as e:
        print(f"[ERROR] YouTube API error: {e}")
        print("Check your .env file and YouTube API key")
        return pd.DataFrame()
    
    # Step 1: Search for a video matching the query
    try:
        search_response = youtube.search().list(
            q=query,
            part='snippet',
            maxResults=1,  # Just get the top video
            type='video'
        ).execute()
    except Exception as e:
        print(f"[ERROR] Error searching videos: {e}")
        return pd.DataFrame()
    
    if not search_response.get('items'):
        print("[ERROR] No videos found for that query")
        return pd.DataFrame()
    
    video_id = search_response['items'][0]['id']['videoId']
    video_title = search_response['items'][0]['snippet']['title']
    print(f"[FOUND] Found video: '{video_title}'")
    
    # Step 2: Get comments from that video
    comments_data = []
    try:
        comment_response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            maxResults=min(limit, 100)
        ).execute()
        
        for item in comment_response.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']
            comments_data.append({
                'id': item['id'],
                'platform': 'youtube',
                'title': '',
                'text': comment['textDisplay'],
                'author': comment['authorDisplayName'],
                'created_utc': datetime.strptime(comment['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"),
                'score': comment['likeCount'],
                'num_comments': item['snippet']['totalReplyCount'],
                'url': f"https://youtube.com/watch?v={video_id}&lc={item['id']}"
            })
    except Exception as e:
        print(f"[ERROR] Error getting comments (may be disabled): {e}")
        return pd.DataFrame()
    
    df = pd.DataFrame(comments_data)
    print(f"[OK] Collected {len(df)} comments")
    return df

if __name__ == "__main__":
    youtube_vid = input("Enter the YouTube search query: ")  # Change only this
    
    df = collect_youtube_comments(youtube_vid, limit=500)
    if not df.empty:
        filename = f"youtube_{youtube_vid.replace(' ', '_')}.csv"
        df.to_csv('youtube_data.csv', index=False)
        print("[OK] Saved to youtube_data.csv")