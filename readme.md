# 🚀 Social Media Analytics Pipeline - Complete Windows Guide
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> **A complete, beginner-friendly project that collects data from Reddit, Twitter, and YouTube, analyzes sentiment, and displays beautiful interactive dashboards - optimized for Windows!**

This project is perfect for learning about data science, APIs, databases, and web development all in one place!

---

## 📖 Table of Contents

- [What This Project Does](#-what-this-project-does)
- [What You'll Learn](#-what-youll-learn)
- [Prerequisites](#-prerequisites)
- [Complete Installation Guide](#-complete-installation-guide)
- [Getting Your API Keys](#-getting-your-api-keys)
- [Project Structure Explained](#-project-structure-explained)
- [Running the Project](#-running-the-project)
- [Understanding the Code](#-understanding-the-code)
- [Troubleshooting](#-troubleshooting)
- [Making It Your Own](#-making-it-your-own)

---

## 🎯 What This Project Does

Imagine you want to know what people are saying about "Python programming" across social media. This project:

1. **Collects** posts from Reddit, tweets from Twitter, and comments from YouTube
2. **Cleans** the text (removes URLs, special characters, etc.)
3. **Analyzes** sentiment (positive, negative, or neutral)
4. **Stores** everything in a database
5. **Visualizes** the data in a beautiful interactive dashboard

**Example Output:**
```
📊 Total collected: 150 posts
   - 50 from Reddit
   - 50 from Twitter  
   - 50 from YouTube

🔍 Sentiment Analysis:
   - Positive: 45%
   - Neutral: 35%
   - Negative: 20%

✅ All data stored in database!
```

---

## 🎓 What You'll Learn

By completing this project, you'll understand:

- ✅ **API Integration** - How to connect to and fetch data from social media platforms
- ✅ **Data Processing** - Cleaning and transforming messy real-world data
- ✅ **Natural Language Processing (NLP)** - Analyzing text to understand sentiment
- ✅ **Database Management** - Storing and querying data with SQLite
- ✅ **Data Visualization** - Creating interactive dashboards with Plotly Dash
- ✅ **Automation** - Scheduling tasks to run automatically
- ✅ **Virtual Environments** - Managing Python dependencies properly
- ✅ **Environment Variables** - Keeping API keys secure

---

## 📋 Prerequisites

### What You Need to Know

- **Basic Python** (variables, functions, loops)
- **Basic Command Prompt/PowerShell** (cd, dir, running commands)
- **Curiosity and patience!** 

**Don't worry if you're not an expert!** This guide explains everything step-by-step.

### System Requirements

- **Windows 10** or **Windows 11**
- **Python 3.8+** (we'll install this)
- **Internet connection**
- **~500MB free disk space**

---

## 🛠️ Complete Installation Guide

### Step 1: Install Python

1. **Download Python:**
   - Go to https://www.python.org/downloads/
   - Click the big yellow "Download Python 3.x.x" button
   - Download the installer

2. **Install Python:**
   - Run the downloaded installer
   - ⚠️ **CRITICAL:** Check ✅ **"Add Python to PATH"** at the bottom!
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close"

3. **Verify Installation:**
   - Press `Windows Key + R`
   - Type `cmd` and press Enter
   - In the Command Prompt, type:
   ```cmd
   python --version
   ```
   - You should see something like: `Python 3.11.5`

---

### Step 2: Create Your Project Folder

1. **Open Command Prompt:**
   - Press `Windows Key + R`
   - Type `cmd` and press Enter

2. **Create Project Folder:**
   ```cmd
   cd %USERPROFILE%\Documents
   mkdir social-media-analytics
   cd social-media-analytics
   ```

**What this does:** Creates a folder called `social-media-analytics` in your Documents folder and opens it.

---

### Step 3: Create a Virtual Environment

```cmd
python -m venv venv
```

**What this does:** Creates an isolated Python environment for this project.

**Activate the virtual environment:**
```cmd
venv\Scripts\activate
```

**You'll know it worked** when you see `(venv)` at the start of your command prompt:
```
(venv) C:\Users\YourName\Documents\social-media-analytics>
```

⚠️ **IMPORTANT:** You must run `venv\Scripts\activate` every time you open a new Command Prompt to work on this project!

---

### Step 4: Upgrade pip

```cmd
python -m pip install --upgrade pip
```

**What this does:** Updates pip (Python's package manager) to the latest version.

---

### Step 5: Install Python Packages

Now install all the libraries we need (this may take 3-5 minutes):

```cmd
pip install pandas numpy matplotlib seaborn praw tweepy google-api-python-client textblob vaderSentiment sqlalchemy plotly dash schedule python-dotenv spacy scikit-learn nltk joblib
```

**What each package does:**

| Package | Purpose |
|---------|---------|
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computing |
| `matplotlib`, `seaborn` | Data visualization |
| `praw` | Reddit API wrapper |
| `tweepy` | Twitter API wrapper |
| `google-api-python-client` | YouTube API wrapper |
| `textblob`, `vaderSentiment` | Sentiment analysis |
| `sqlalchemy` | Database toolkit |
| `plotly`, `dash` | Interactive dashboards |
| `schedule` | Task scheduling |
| `python-dotenv` | Load environment variables |
| `spacy` | Advanced NLP |
| `scikit-learn` | Machine learning |
| `nltk` | Natural language toolkit |
| `joblib` | Save/load models |

---

### Step 6: Download NLP Models

```cmd
python -m spacy download en_core_web_sm
```

```cmd
python -c "import nltk; nltk.download('stopwords'); nltk.download('vader_lexicon')"
```

**What this does:** Downloads pre-trained models needed for natural language processing.

---

## 🔑 Getting Your API Keys

To collect data from social media platforms, you need API keys. Think of these as special passwords that let your code access their data.

### 🔴 Reddit API (5 minutes)

1. Go to: https://www.reddit.com/prefs/apps
2. Log in to your Reddit account
3. Scroll down and click **"Create App"** or **"Create Another App"**
4. Fill in the form:
   - **Name:** `My Social Analytics App`
   - **App type:** Select `script`
   - **Description:** `Learning data science`
   - **About URL:** Leave blank
   - **Redirect URI:** `http://localhost:8080`
5. Click **"Create app"**
6. You'll see:
   - **Client ID** (under the app name, 14 characters)
   - **Secret** (next to "secret:", 27 characters)

**Save these for later!**

---

### 🔵 Twitter API (15 minutes)

1. Go to: https://developer.twitter.com
2. Click **"Sign up"** (or "Sign in" if you have an account)
3. Apply for a developer account:
   - Choose **"Hobbyist"** → **"Exploring the API"**
   - Fill in the required information
   - Agree to terms
4. Once approved (may take minutes to hours), go to the Developer Portal
5. Create a Project and App:
   - Click **"Create Project"**
   - Name it `Social Analytics`
   - Choose **"Exploring"** as use case
   - Provide a description
6. In your app settings, go to **"Keys and tokens"**
7. Generate a **Bearer Token**

**Save this Bearer Token!**

---

### 🔴 YouTube API (10 minutes)

1. Go to: https://console.cloud.google.com
2. Create a new project:
   - Click **"Select a project"** at the top
   - Click **"New Project"**
   - Name it `Social Analytics`
   - Click **"Create"**
3. Enable YouTube Data API:
   - Go to **"APIs & Services"** → **"Library"**
   - Search for **"YouTube Data API v3"**
   - Click on it and click **"Enable"**
4. Create credentials:
   - Go to **"APIs & Services"** → **"Credentials"**
   - Click **"Create Credentials"** → **"API Key"**
   - Copy your API key

**Save this API Key!**

---

### 📝 Create Your .env File

Now create a file to store all your API keys securely.

**Method 1: Using Notepad**

1. Open Notepad (search in Start Menu)
2. Paste this template and **replace with your actual keys**:

```env
# Reddit API Credentials
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_secret_here
REDDIT_USER_AGENT=MyAnalyticsApp/1.0

# Twitter/X API Credentials
TWITTER_BEARER_TOKEN=your_bearer_token_here

# YouTube API Credentials
YOUTUBE_API_KEY=your_google_api_key_here
```

3. Click **File** → **Save As**
4. Navigate to: `C:\Users\YourName\Documents\social-media-analytics`
5. Change **"Save as type"** to **"All Files"**
6. Name the file: `.env` (include the dot!)
7. Click **Save**

**Method 2: Using Command Prompt**

```cmd
echo # Reddit API Credentials > .env
echo REDDIT_CLIENT_ID=your_client_id_here >> .env
echo REDDIT_CLIENT_SECRET=your_secret_here >> .env
echo REDDIT_USER_AGENT=MyAnalyticsApp/1.0 >> .env
echo. >> .env
echo # Twitter/X API Credentials >> .env
echo TWITTER_BEARER_TOKEN=your_bearer_token_here >> .env
echo. >> .env
echo # YouTube API Credentials >> .env
echo YOUTUBE_API_KEY=your_google_api_key_here >> .env
```

Then edit the file with:
```cmd
notepad .env
```

Replace the placeholder values with your actual API keys, then save.

⚠️ **NEVER share your .env file or upload it to GitHub!**

---

## 📁 Project Structure Explained

Here's what each file in your project does:

```
social-media-analytics/
│
├── venv/                          # Virtual environment (don't touch)
│
├── .env                           # Your API keys (SECRET!)
│
├── database.py                    # Handles SQLite database operations
├── collect_data.py                # Collects posts from Reddit
├── collect_twitter.py             # Collects tweets from Twitter
├── collect_youtube.py             # Collects comments from YouTube
├── process_data.py                # Cleans and processes text data
├── sentiment_analysis.py          # Analyzes sentiment of posts
├── pipeline.py                    # Main script - runs everything
├── dashboard.py                   # Interactive web dashboard
│
├── requirements.txt               # List of all Python packages
│
└── social_media.db               # SQLite database (created after first run)
```

---

## 🏗️ Creating Your Project Files

Now let's create each file with the actual code!

### File 1: `database.py` - Database Manager

**Create the file:**
```cmd
notepad database.py
```

**Copy and paste this code:**

```python
import sqlite3
import pandas as pd
from datetime import datetime

class SocialMediaDB:
    """
    This class handles all database operations.
    It creates tables and stores/retrieves posts.
    """
    
    def __init__(self, db_name='social_media.db'):
        """Initialize database connection"""
        self.db_name = db_name
        self.create_tables()
    
    def create_tables(self):
        """Create the posts table if it doesn't exist"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # SQL command to create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                title TEXT,
                text TEXT,
                author TEXT,
                created_utc TIMESTAMP,
                score INTEGER,
                num_comments INTEGER,
                url TEXT,
                sentiment_score REAL,
                sentiment_label TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
        print("✓ Database tables created/verified!")
    
    def insert_posts(self, df):
        """Insert new posts into the database"""
        if df.empty:
            print("⚠ No data to insert")
            return
            
        conn = sqlite3.connect(self.db_name)
        
        try:
            # Insert data into table
            df.to_sql('posts', conn, if_exists='append', index=False)
            
            # Remove any duplicate posts (same ID)
            conn.execute('''
                DELETE FROM posts
                WHERE rowid NOT IN (
                    SELECT MIN(rowid)
                    FROM posts
                    GROUP BY id
                )
            ''')
            conn.commit()
            print(f"✓ Inserted/Updated {len(df)} posts in database")
        except Exception as e:
            print(f"✗ Error inserting posts: {e}")
        finally:
            conn.close()
    
    def get_all_posts(self):
        """Retrieve all posts from the database"""
        conn = sqlite3.connect(self.db_name)
        try:
            df = pd.read_sql_query("SELECT * FROM posts", conn)
        except Exception as e:
            print(f"✗ Error reading posts: {e}")
            df = pd.DataFrame()
        finally:
            conn.close()
        return df
```

**Save:** Press `Ctrl+S`, then close Notepad

---

### File 2: `collect_data.py` - Reddit Collector

```cmd
notepad collect_data.py
```

```python
import praw
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# Try to connect to Reddit API
try:
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )
    # Test if connection works
    reddit.user.me()
    print("✓ Reddit API connected successfully!")
except Exception as e:
    print(f"✗ Reddit API error: {e}")
    print("Check your .env file and Reddit API credentials")
    reddit = None

def collect_reddit_posts(subreddit_name, limit=100):
    """
    Collect posts from a specific subreddit.
    
    Args:
        subreddit_name: The subreddit to collect from (e.g., 'python')
        limit: Maximum number of posts to collect
    
    Returns:
        DataFrame with post data
    """
    if not reddit:
        print("✗ Reddit client not initialized")
        return pd.DataFrame()
    
    print(f"📥 Collecting posts from r/{subreddit_name}...")
    posts_data = []
    
    try:
        subreddit = reddit.subreddit(subreddit_name)
        
        # Get hot posts from the subreddit
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
        print(f"✗ Error collecting Reddit posts: {e}")
        return pd.DataFrame()
    
    df = pd.DataFrame(posts_data)
    print(f"✓ Collected {len(df)} Reddit posts")
    return df

# This runs if you execute this file directly
if __name__ == "__main__":
    df = collect_reddit_posts('python', limit=50)
    if not df.empty:
        df.to_csv('reddit_data.csv', index=False)
        print("✓ Saved to reddit_data.csv")
```

**Save and close**

---

### File 3: `collect_twitter.py` - Twitter Collector

```cmd
notepad collect_twitter.py
```

```python
import tweepy
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# Try to connect to Twitter API
try:
    client = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'))
    print("✓ Twitter API connected successfully!")
except Exception as e:
    print(f"✗ Twitter API error: {e}")
    print("Check your .env file and Twitter Bearer Token")
    client = None

def collect_twitter_tweets(query, limit=100):
    """
    Collect recent tweets matching a search query.
    
    Args:
        query: What to search for (e.g., 'python programming')
        limit: Maximum number of tweets to collect
    
    Returns:
        DataFrame with tweet data
    """
    if not client:
        print("✗ Twitter client not initialized")
        return pd.DataFrame()
    
    print(f"📥 Collecting tweets for: '{query}'...")
    tweets_data = []
    
    try:
        # Search for recent tweets
        response = client.search_recent_tweets(
            query=query,
            max_results=min(limit, 100),  # Twitter API limit is 100
            tweet_fields=['created_at', 'public_metrics', 'author_id']
        )
        
        if response.data:
            for tweet in response.data:
                tweets_data.append({
                    'id': str(tweet.id),
                    'platform': 'twitter',
                    'title': '',  # Twitter doesn't have titles
                    'text': tweet.text,
                    'author': str(tweet.author_id),
                    'created_utc': tweet.created_at,
                    'score': tweet.public_metrics['like_count'],
                    'num_comments': tweet.public_metrics['reply_count'],
                    'url': f"https://twitter.com/i/status/{tweet.id}"
                })
        else:
            print("⚠ No tweets found for that query")
            
    except Exception as e:
        print(f"✗ Error collecting tweets: {e}")
        return pd.DataFrame()
    
    df = pd.DataFrame(tweets_data)
    print(f"✓ Collected {len(df)} tweets")
    return df

if __name__ == "__main__":
    df = collect_twitter_tweets('python programming', limit=50)
    if not df.empty:
        df.to_csv('twitter_data.csv', index=False)
        print("✓ Saved to twitter_data.csv")
```

**Save and close**

---

### File 4: `collect_youtube.py` - YouTube Collector

```cmd
notepad collect_youtube.py
```

```python
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load API keys
load_dotenv()

def collect_youtube_comments(query, limit=100):
    """
    Collect comments from YouTube videos matching a search query.
    
    Args:
        query: What to search for (e.g., 'python tutorial')
        limit: Maximum number of comments to collect
    
    Returns:
        DataFrame with comment data
    """
    print(f"📥 Collecting YouTube comments for: '{query}'...")
    
    # Build YouTube API client
    try:
        youtube = build('youtube', 'v3', developerKey=os.getenv('YOUTUBE_API_KEY'))
        print("✓ YouTube API connected successfully!")
    except Exception as e:
        print(f"✗ YouTube API error: {e}")
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
        print(f"✗ Error searching videos: {e}")
        return pd.DataFrame()
    
    if not search_response.get('items'):
        print("✗ No videos found for that query")
        return pd.DataFrame()
    
    video_id = search_response['items'][0]['id']['videoId']
    video_title = search_response['items'][0]['snippet']['title']
    print(f"📹 Found video: '{video_title}'")
    
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
        print(f"✗ Error getting comments (may be disabled): {e}")
        return pd.DataFrame()
    
    df = pd.DataFrame(comments_data)
    print(f"✓ Collected {len(df)} comments")
    return df

if __name__ == "__main__":
    df = collect_youtube_comments('python tutorial', limit=50)
    if not df.empty:
        df.to_csv('youtube_data.csv', index=False)
        print("✓ Saved to youtube_data.csv")
```

**Save and close**

---

### File 5: `process_data.py` - Data Cleaner

```cmd
notepad process_data.py
```

```python
import pandas as pd
import re

def clean_text(text):
    """
    Clean text data by removing URLs, special characters, and extra spaces.
    
    Args:
        text: The text to clean
    
    Returns:
        Cleaned text in lowercase
    """
    # Handle empty or non-string values
    if pd.isna(text) or not isinstance(text, str):
        return ""
    
    # Remove URLs (like http://example.com)
    text = re.sub(r'http\S+', '', text)
    
    # Remove special characters (keep only letters and spaces)
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Convert to lowercase
    return text.lower()

def process_data(df):
    """
    Process and clean a DataFrame of posts.
    
    Args:
        df: DataFrame with raw post data
    
    Returns:
        Cleaned DataFrame
    """
    if df.empty:
        return df
        
    print(f"⚙ Processing {len(df)} posts...")
    
    # Make sure 'title' column exists (Twitter/YouTube don't have titles)
    if 'title' not in df.columns:
        df['title'] = ''
    
    # Clean title and text
    df['title_clean'] = df['title'].apply(clean_text)
    df['text_clean'] = df['text'].apply(clean_text)
    
    # Combine title and text into one column
    df['full_text'] = (df['title_clean'] + ' ' + df['text_clean']).str.strip()
    
    # Remove duplicate posts
    df = df.drop_duplicates(subset=['id'])
    
    # Remove posts with very short text (less than 10 characters)
    df = df[df['full_text'].str.len() > 10]
    
    print(f"✓ {len(df)} posts remaining after processing")
    return df
```

**Save and close**

---

### File 6: `sentiment_analysis.py` - Sentiment Analyzer

```cmd
notepad sentiment_analysis.py
```

```python
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment_vader(text):
    """
    Analyze sentiment using VADER (Valence Aware Dictionary and sEntiment Reasoner).
    VADER is great for social media text!
    
    Args:
        text: The text to analyze
    
    Returns:
        (score, label) tuple
        - score: -1 (very negative) to +1 (very positive)
        - label: 'positive', 'negative', or 'neutral'
    """
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    
    # Get compound score (overall sentiment)
    compound = scores['compound']
    
    # Classify sentiment
    if compound >= 0.05:
        label = 'positive'
    elif compound <= -0.05:
        label = 'negative'
    else:
        label = 'neutral'
    
    return compound, label

def analyze_data(df):
    """
    Analyze sentiment for all posts in a DataFrame.
    
    Args:
        df: DataFrame with 'full_text' column
    
    Returns:
        DataFrame with sentiment_score and sentiment_label columns added
    """
    if df.empty:
        return df
        
    print("🔍 Analyzing sentiment...")
    
    # Apply sentiment analysis to each post
    df[['sentiment_score', 'sentiment_label']] = df['full_text'].apply(
        lambda x: pd.Series(analyze_sentiment_vader(x))
    )
    
    print("✓ Sentiment analysis complete!")
    print("\n📊 Sentiment Distribution:")
    print(df['sentiment_label'].value_counts())
    print()
    
    return df
```

**Save and close**

---

### File 7: `pipeline.py` - Main Pipeline

```cmd
notepad pipeline.py
```

```python
import schedule
import time
import pandas as pd
from collect_data import collect_reddit_posts
from collect_twitter import collect_twitter_tweets
from collect_youtube import collect_youtube_comments
from process_data import process_data
from sentiment_analysis import analyze_data
from database import SocialMediaDB

def run_pipeline():
    """
    This is the main function that runs everything:
    1. Collects data from all platforms
    2. Processes and cleans the data
    3. Analyzes sentiment
    4. Stores everything in the database
    """
    print("\n" + "="*60)
    print("🚀 STARTING PIPELINE RUN")
    print("="*60)
    
    # ====== STEP 1: COLLECT DATA ======
    print("\n📥 Step 1: Collecting data from all platforms...")
    
    df_reddit = collect_reddit_posts('datascience', limit=50)
    df_twitter = collect_twitter_tweets('data engineering', limit=50)
    df_youtube = collect_youtube_comments('machine learning', limit=50)
    
    # Combine all data into one DataFrame
    df_all = pd.concat([df_reddit, df_twitter, df_youtube], ignore_index=True)
    
    print(f"\n📊 Total collected: {len(df_all)} posts")
    print(f"   - Reddit: {len(df_reddit)} posts")
    print(f"   - Twitter: {len(df_twitter)} tweets")
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
    
    db = SocialMediaDB()
    db.insert_posts(df_to_insert)
    
    print("\n" + "="*60)
    print("✅ PIPELINE COMPLETE!")
    print("="*60 + "\n")

if __name__ == "__main__":
    # Run the pipeline immediately when script starts
    run_pipeline()
    
    # Schedule to run automatically every 6 hours
    schedule.every(6).hours.do(run_pipeline)
    
    print("\n⏰ Pipeline scheduled to run every 6 hours")
    print("Press Ctrl+C to stop\n")
    
    # Keep the script running and check for scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
```

**Save and close**

---

## 🎮 Running the Project

### Step 1: Activate Virtual Environment

Every time you work on this project, first activate the virtual environment:

```cmd
cd %USERPROFILE%\Documents\social-media-analytics
venv\Scripts\activate
```

### Step 2: Test Individual Components

Test each module separately:

**Test Reddit collector:**
```cmd
python collect_data.py
```

**Test Twitter collector:**
```cmd
python collect_twitter.py
```

**Test YouTube collector:**
```cmd
python collect_youtube.py
```

### Step 3: Run the Full Pipeline

```cmd
python pipeline.py
```

This will:
1. Collect data from all 3 platforms
2. Clean and process the data
3. Analyze sentiment
4. Store everything in the database

**Expected Output:**
```
🚀 STARTING PIPELINE RUN
============================================================

📥 Step 1: Collecting data from all platforms...
✓ Reddit API connected successfully!
📥 Collecting posts from r/datascience...
✓ Collected 50 Reddit posts
✓ Twitter API connected successfully!
📥 Collecting tweets for: 'data engineering'...
✓ Collected 50 tweets
✓ YouTube API connected successfully!
📥 Collecting YouTube comments for: 'machine learning'...
📹 Found video: 'Machine Learning Tutorial for Beginners'
✓ Collected 50 comments

📊 Total collected: 150 posts
   - Reddit: 50 posts
   - Twitter: 50 tweets
   - YouTube: 50 comments

⚙ Step 2: Processing and cleaning data...
✓ 147 posts remaining after processing

🔍 Step 3: Analyzing sentiment...
✓ Sentiment analysis complete!

📊 Sentiment Distribution:
positive    68
neutral     52
negative    27

💾 Step 4: Storing in database...
✓ Database tables created/verified!
✓ Inserted/Updated 147 posts in database

============================================================
✅ PIPELINE COMPLETE!
============================================================
```

---

## 📊 Creating the Dashboard

### File 8: `dashboard.py` - Interactive Visualization

```cmd
notepad dashboard.py
```

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from database import SocialMediaDB

# Initialize the Dash app
app = dash.Dash(__name__)

# Load data from database
db = SocialMediaDB()
df = db.get_all_posts()

# Define color scheme
COLORS = {
    'background': '#111111',
    'text': '#7FDBFF',
    'positive': '#2ECC71',
    'neutral': '#3498DB',
    'negative': '#E74C3C'
}

# Create the layout
app.layout = html.Div(style={'backgroundColor': COLORS['background'], 'padding': '20px'}, children=[
    html.H1(
        children='Social Media Analytics Dashboard',
        style={'textAlign': 'center', 'color': COLORS['text'], 'marginBottom': '30px'}
    ),
    
    html.Div([
        html.Div([
            html.H3('Total Posts', style={'color': COLORS['text']}),
            html.H2(f"{len(df)}", style={'color': '#FFF', 'fontSize': '48px'})
        ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#1E1E1E', 
                  'borderRadius': '10px', 'width': '30%', 'display': 'inline-block', 'margin': '10px'}),
        
        html.Div([
            html.H3('Positive', style={'color': COLORS['positive']}),
            html.H2(f"{len(df[df['sentiment_label'] == 'positive'])}", 
                   style={'color': COLORS['positive'], 'fontSize': '48px'})
        ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#1E1E1E',
                  'borderRadius': '10px', 'width': '30%', 'display': 'inline-block', 'margin': '10px'}),
        
        html.Div([
            html.H3('Negative', style={'color': COLORS['negative']}),
            html.H2(f"{len(df[df['sentiment_label'] == 'negative'])}", 
                   style={'color': COLORS['negative'], 'fontSize': '48px'})
        ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#1E1E1E',
                  'borderRadius': '10px', 'width': '30%', 'display': 'inline-block', 'margin': '10px'}),
    ], style={'textAlign': 'center', 'marginBottom': '30px'}),
    
    # Sentiment Distribution by Platform
    html.Div([
        dcc.Graph(
            id='sentiment-by-platform',
            figure=create_sentiment_by_platform(df)
        )
    ], style={'marginBottom': '30px'}),
    
    # Sentiment Over Time
    html.Div([
        dcc.Graph(
            id='sentiment-over-time',
            figure=create_sentiment_timeline(df)
        )
    ], style={'marginBottom': '30px'}),
    
    # Platform Distribution
    html.Div([
        dcc.Graph(
            id='platform-distribution',
            figure=create_platform_pie(df)
        )
    ], style={'marginBottom': '30px'}),
    
    # Top Posts Table
    html.Div([
        html.H2('Top Posts by Score', style={'color': COLORS['text'], 'marginBottom': '20px'}),
        create_top_posts_table(df)
    ])
])

def create_sentiment_by_platform(df):
    """Create stacked bar chart of sentiment by platform"""
    if df.empty:
        return go.Figure()
    
    sentiment_counts = df.groupby(['platform', 'sentiment_label']).size().reset_index(name='count')
    
    fig = px.bar(
        sentiment_counts,
        x='platform',
        y='count',
        color='sentiment_label',
        title='Sentiment Distribution by Platform',
        color_discrete_map={
            'positive': COLORS['positive'],
            'neutral': COLORS['neutral'],
            'negative': COLORS['negative']
        },
        labels={'count': 'Number of Posts', 'platform': 'Platform', 'sentiment_label': 'Sentiment'}
    )
    
    fig.update_layout(
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['background'],
        font_color=COLORS['text'],
        title_font_size=20
    )
    
    return fig

def create_sentiment_timeline(df):
    """Create line chart showing sentiment over time"""
    if df.empty:
        return go.Figure()
    
    # Convert to datetime if needed
    df['created_utc'] = pd.to_datetime(df['created_utc'])
    df['date'] = df['created_utc'].dt.date
    
    # Count sentiments by date
    timeline_data = df.groupby(['date', 'sentiment_label']).size().reset_index(name='count')
    
    fig = px.line(
        timeline_data,
        x='date',
        y='count',
        color='sentiment_label',
        title='Sentiment Trends Over Time',
        color_discrete_map={
            'positive': COLORS['positive'],
            'neutral': COLORS['neutral'],
            'negative': COLORS['negative']
        },
        labels={'count': 'Number of Posts', 'date': 'Date', 'sentiment_label': 'Sentiment'}
    )
    
    fig.update_layout(
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['background'],
        font_color=COLORS['text'],
        title_font_size=20
    )
    
    return fig

def create_platform_pie(df):
    """Create pie chart of posts by platform"""
    if df.empty:
        return go.Figure()
    
    platform_counts = df['platform'].value_counts().reset_index()
    platform_counts.columns = ['platform', 'count']
    
    fig = px.pie(
        platform_counts,
        values='count',
        names='platform',
        title='Posts by Platform',
        color_discrete_sequence=['#E74C3C', '#3498DB', '#2ECC71']
    )
    
    fig.update_layout(
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['background'],
        font_color=COLORS['text'],
        title_font_size=20
    )
    
    return fig

def create_top_posts_table(df):
    """Create a table showing top posts by score"""
    if df.empty:
        return html.Div("No data available")
    
    top_posts = df.nlargest(10, 'score')[['platform', 'title', 'text', 'score', 'sentiment_label']]
    
    # Truncate text for display
    top_posts['text'] = top_posts['text'].str[:100] + '...'
    top_posts['title'] = top_posts['title'].str[:50]
    
    rows = []
    for _, row in top_posts.iterrows():
        sentiment_color = {
            'positive': COLORS['positive'],
            'neutral': COLORS['neutral'],
            'negative': COLORS['negative']
        }.get(row['sentiment_label'], '#FFF')
        
        rows.append(html.Tr([
            html.Td(row['platform'].upper(), style={'color': '#FFF', 'padding': '10px'}),
            html.Td(row['title'] if row['title'] else row['text'], 
                   style={'color': '#FFF', 'padding': '10px', 'maxWidth': '400px'}),
            html.Td(str(row['score']), style={'color': '#FFF', 'padding': '10px'}),
            html.Td(row['sentiment_label'].upper(), 
                   style={'color': sentiment_color, 'padding': '10px', 'fontWeight': 'bold'})
        ]))
    
    table = html.Table([
        html.Thead(html.Tr([
            html.Th('Platform', style={'color': COLORS['text'], 'padding': '10px'}),
            html.Th('Content', style={'color': COLORS['text'], 'padding': '10px'}),
            html.Th('Score', style={'color': COLORS['text'], 'padding': '10px'}),
            html.Th('Sentiment', style={'color': COLORS['text'], 'padding': '10px'})
        ])),
        html.Tbody(rows)
    ], style={'width': '100%', 'backgroundColor': '#1E1E1E', 'borderRadius': '10px'})
    
    return table

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Starting Dashboard Server...")
    print("="*60)
    print("\n📊 Dashboard running at: http://127.0.0.1:8050")
    print("\nPress Ctrl+C to stop\n")
    
    app.run_server(debug=True, host='127.0.0.1', port=8050)
```

**Save and close**

### Run the Dashboard

```cmd
python dashboard.py
```

**Open your browser and go to:** `http://127.0.0.1:8050`

You'll see a beautiful interactive dashboard with:
- Summary statistics
- Sentiment distribution by platform
- Sentiment trends over time
- Platform distribution pie chart
- Top posts table

---

## 🔧 Troubleshooting

### Problem: "Python is not recognized"

**Solution:**
1. Reinstall Python from python.org
2. Make sure to check ✅ "Add Python to PATH"
3. Restart Command Prompt

### Problem: "pip is not recognized"

**Solution:**
```cmd
python -m pip --version
```
Use `python -m pip` instead of just `pip`

### Problem: "Module not found" errors

**Solution:**
```cmd
# Make sure virtual environment is activated
venv\Scripts\activate

# Reinstall all packages
pip install --upgrade pip
pip install -r requirements.txt
```

### Problem: Reddit API authentication fails

**Solution:**
1. Double-check your `.env` file
2. Make sure there are no extra spaces or quotes
3. Verify credentials at https://www.reddit.com/prefs/apps

**Correct format:**
```env
REDDIT_CLIENT_ID=abc123xyz789
REDDIT_CLIENT_SECRET=secretkey123456789
```

**Wrong format:**
```env
REDDIT_CLIENT_ID = "abc123xyz789"    # No quotes or spaces!
```

### Problem: Twitter API "Could not authenticate"

**Solution:**
1. Make sure you have Essential access (free tier)
2. Generate a new Bearer Token
3. Update `.env` file
4. Twitter may have rate limits - wait 15 minutes and try again

### Problem: YouTube API quota exceeded

**Solution:**
- YouTube API has daily quotas (10,000 units/day)
- Reduce `limit` parameter in `collect_youtube_comments()`
- Or wait until tomorrow for quota reset

### Problem: Dashboard shows no data

**Solution:**
```cmd
# Run the pipeline first to collect data
python pipeline.py

# Then run the dashboard
python dashboard.py
```

### Problem: Port 8050 already in use

**Solution:**
Edit `dashboard.py` and change the port:
```python
app.run_server(debug=True, host='127.0.0.1', port=8051)  # Changed to 8051
```

---

## 📝 Creating requirements.txt

Create this file to easily share your project:

```cmd
notepad requirements.txt
```

```txt
pandas==2.0.3
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.12.2
praw==7.7.1
tweepy==4.14.0
google-api-python-client==2.95.0
textblob==0.17.1
vaderSentiment==3.3.2
sqlalchemy==2.0.19
plotly==5.16.1
dash==2.12.1
schedule==1.2.0
python-dotenv==1.0.0
spacy==3.6.1
scikit-learn==1.3.0
nltk==3.8.1
joblib==1.3.1
```

**Save and close**

Now anyone can install all dependencies with:
```cmd
pip install -r requirements.txt
```

---

## 🎨 Making It Your Own

### Change What Topics to Track

Edit `pipeline.py` and modify these lines:

```python
# Change subreddit
df_reddit = collect_reddit_posts('gaming', limit=50)  # Changed from 'datascience'

# Change Twitter query
df_twitter = collect_twitter_tweets('artificial intelligence', limit=50)

# Change YouTube query
df_youtube = collect_youtube_comments('react tutorial', limit=50)
```

### Change Collection Schedule

In `pipeline.py`, change this line:

```python
# Run every 6 hours (default)
schedule.every(6).hours.do(run_pipeline)

# Or run every hour
schedule.every(1).hours.do(run_pipeline)

# Or run every day at 9 AM
schedule.every().day.at("09:00").do(run_pipeline)

# Or run every 30 minutes
schedule.every(30).minutes.do(run_pipeline)
```

### Collect More Data

Change the `limit` parameter:

```python
df_reddit = collect_reddit_posts('python', limit=200)  # Collect 200 posts instead of 50
```

⚠️ **Warning:** Higher limits may hit API rate limits!

### Add More Platforms

You can extend this project to collect from:
- **Instagram** (using `instaloader`)
- **TikTok** (using `TikTokApi`)
- **LinkedIn** (using `linkedin-api`)
- **Facebook** (using `facebook-sdk`)

---

## 📊 Understanding Your Data

### View Database Contents

**Option 1: Using Python**

```cmd
python
```

```python
from database import SocialMediaDB
import pandas as pd

db = SocialMediaDB()
df = db.get_all_posts()

print(df.head())  # Show first 5 rows
print(df.info())  # Show column info
print(df['sentiment_label'].value_counts())  # Count sentiments
```

**Option 2: Using DB Browser for SQLite**

1. Download DB Browser from: https://sqlitebrowser.org/dl/
2. Install it
3. Open `social_media.db` file
4. Browse the `posts` table

### Export Data to Excel

```python
from database import SocialMediaDB

db = SocialMediaDB()
df = db.get_all_posts()

df.to_excel('social_media_data.xlsx', index=False)
print("✓ Exported to social_media_data.xlsx")
```

---

## 🚀 Running the Project Automatically on Windows Startup

### Method 1: Create a Batch Script

1. Create `start_pipeline.bat`:

```cmd
notepad start_pipeline.bat
```

```batch
@echo off
cd %USERPROFILE%\Documents\social-media-analytics
call venv\Scripts\activate
python pipeline.py
pause
```

2. Save and double-click `start_pipeline.bat` to run!

### Method 2: Use Windows Task Scheduler

1. Open **Task Scheduler** (search in Start Menu)
2. Click **"Create Basic Task"**
3. Name it: `Social Media Analytics`
4. Trigger: **"When I log on"**
5. Action: **"Start a program"**
6. Program: `C:\Users\YourName\Documents\social-media-analytics\start_pipeline.bat`
7. Click **Finish**

Now it runs automatically when you log in to Windows!

---

## 📈 Advanced Features to Add

### 1. Email Notifications

```python
# Add this to pipeline.py
import smtplib
from email.mime.text import MIMEText

def send_email_notification(message):
    """Send email when pipeline completes"""
    sender = "your_email@gmail.com"
    receiver = "your_email@gmail.com"
    password = "your_app_password"
    
    msg = MIMEText(message)
    msg['Subject'] = 'Social Media Pipeline Complete'
    msg['From'] = sender
    msg['To'] = receiver
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.send_message(msg)

# Call it at the end of run_pipeline()
send_email_notification(f"Collected {len(df_all)} posts!")
```

### 2. Save Charts as Images

```python
# In dashboard.py
import plotly.io as pio

fig = create_sentiment_by_platform(df)
pio.write_image(fig, 'sentiment_chart.png')
```

### 3. Add Word Cloud

```cmd
pip install wordcloud
```

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Combine all text
all_text = ' '.join(df['full_text'])

# Create word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloud.png')
print("✓ Word cloud saved to wordcloud.png")
```

---

## ❓ FAQ

**Q: How much does this cost?**
A: $0! All APIs used have free tiers sufficient for this project.

**Q: Can I use this for my business?**
A: Check each platform's API Terms of Service. This project is educational.

**Q: How do I stop the pipeline?**
A: Press `Ctrl+C` in the Command Prompt window.

**Q: Can I share my API keys?**
A: **NEVER!** Keep your `.env` file private. Don't upload it to GitHub.

**Q: The dashboard is slow. How to fix?**
A: Reduce the amount of data collected or add pagination to the dashboard.

**Q: Can I deploy this to the cloud?**
A: Yes! You can deploy to:
- **Heroku** (free tier available)
- **AWS EC2** (free tier for 1 year)
- **Google Cloud** (free tier with credits)
- **PythonAnywhere** (free tier available)

---

## 🚀 Heroku Deployment

Follow these steps to deploy the dashboard to Heroku from Windows (Command Prompt):

- **1. Install Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli

- **2. Log in to Heroku**:

```cmd
heroku login
```

- **3. Initialize git (if not already a git repo)**:

```cmd
git init
git add .
git commit -m "Prepare app for Heroku"
```

- **4. Create a Heroku app** (or use an existing name):

```cmd
heroku create my-social-dashboard
```

- **5. Set required environment variables** (your API keys):

```cmd
heroku config:set REDDIT_CLIENT_ID=your_id_here REDDIT_CLIENT_SECRET=your_secret_here REDDIT_USER_AGENT="MyApp/1.0"
heroku config:set TWITTER_BEARER_TOKEN=your_bearer_token_here
heroku config:set YOUTUBE_API_KEY=your_google_api_key_here
```

- **6. Push to Heroku**:

```cmd
git push heroku main
```

- **7. Scale the web dyno (usually already 1)**:

```cmd
heroku ps:scale web=1
```

- **8. Open the app**:

```cmd
heroku open
```

Notes:
- The repository must include a `Procfile`, `requirements.txt`, and (optionally) `runtime.txt` — this repo contains them.
- Heroku will use `gunicorn dashboard:app.server` (see `Procfile`) to run the Dash app.
- Keep your `.env` secret — use `heroku config:set` to store secrets instead of committing them.

**Q: How do I update Python packages?**
```cmd
pip install --upgrade package_name
```

Or update all:
```cmd
pip install --upgrade -r requirements.txt
```

**Q: The dashboard doesn't update automatically**
A: The dashboard shows data from the database. Run `pipeline.py` to collect new data, then refresh the browser.

---

## 🎓 What You've Learned

Congratulations! By completing this project, you now know:

✅ **API Integration** - Connected to 3 different social media APIs  
✅ **Data Collection** - Scraped real-world data from multiple sources  
✅ **Data Processing** - Cleaned and transformed messy text data  
✅ **NLP** - Analyzed sentiment using VADER  
✅ **Database** - Stored and retrieved data with SQLite  
✅ **Visualization** - Created interactive dashboards with Plotly Dash  
✅ **Automation** - Scheduled tasks to run automatically  
✅ **Windows Development** - Set up Python projects on Windows  
✅ **Best Practices** - Used virtual environments, .env files, and modular code  

---

## 📚 Next Steps

### Beginner Projects to Try Next:
1. **Weather Dashboard** - Track weather across cities
2. **Stock Price Tracker** - Monitor stock prices and trends
3. **News Aggregator** - Collect and categorize news articles
4. **Personal Finance Tracker** - Track expenses and budget

### Intermediate Projects:
1. **Machine Learning Classifier** - Train custom sentiment models
2. **Chatbot** - Build a conversational AI
3. **Recommendation System** - Suggest content based on preferences
4. **Real-time Stream Processor** - Process live social media streams

### Advanced Projects:
1. **Full Stack Web App** - Add user authentication and profiles
2. **Mobile App** - Create iOS/Android app
3. **Microservices Architecture** - Split into multiple services
4. **MLOps Pipeline** - Deploy ML models to production

---

## 🌟 Show Off Your Project!

### Share on LinkedIn:
```
🚀 Just completed my Social Media Analytics Pipeline project!

Built a system that:
✅ Collects data from Reddit, Twitter & YouTube
✅ Analyzes sentiment using NLP
✅ Stores data in SQLite database
✅ Visualizes insights in interactive dashboard

Technologies: Python, Pandas, Plotly, APIs, NLP, SQLite

#DataScience #Python #MachineLearning #NLP #Analytics

[Link to GitHub repo]
```

### Add to Your Resume:
```
SOCIAL MEDIA ANALYTICS PIPELINE | Python, NLP, APIs
• Engineered data collection pipeline integrating 3 social media APIs (Reddit, Twitter, YouTube)
• Implemented sentiment analysis using VADER, processing 500+ posts daily
• Built interactive Plotly Dash dashboard visualizing sentiment trends across platforms
• Automated data collection and storage using SQLite database and task scheduling
• Technologies: Python, Pandas, NLTK, REST APIs, Plotly, SQLAlchemy
```

---

## 🤝 Contributing & Getting Help

### Need Help?
- **Stack Overflow**: Search for specific error messages
- **Reddit**: r/learnpython, r/Python
- **Discord**: Python Discord Server
- **Documentation**:
  - [Pandas](https://pandas.pydata.org/docs/)
  - [Plotly](https://plotly.com/python/)
  - [PRAW (Reddit)](https://praw.readthedocs.io/)
  - [Tweepy](https://docs.tweepy.org/)

### Found a Bug?
Create an issue on GitHub describing:
1. What you expected to happen
2. What actually happened
3. Error messages
4. Steps to reproduce

---

## 📄 License

This project is licensed under the MIT License - feel free to use it for learning, personal projects, or commercial applications!

---

## 🙏 Acknowledgments

- **Reddit API** - PRAW library
- **Twitter API** - Tweepy library
- **YouTube API** - Google API Client
- **VADER** - Sentiment analysis tool
- **Plotly** - Interactive visualizations
- **Python Community** - For amazing open-source tools

---

**Happy Coding! 🎉**

*Remember: The best way to learn is by doing. Don't be afraid to experiment, break things, and ask questions!*

---

*Last Updated: November 2025*  
*Version: 1.0.0 (Windows Edition)*  
*Platform: Windows 10/11*