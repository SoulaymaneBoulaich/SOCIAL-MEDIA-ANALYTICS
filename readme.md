# Social Media Analytics (SMA)

> **A complete, beginner-friendly project that collects data from Reddit and YouTube, analyzes sentiment, and displays beautiful interactive dashboards - optimized for Windows\!**

This project is perfect for learning about data science, APIs, databases, and web development all in one place\!

-----

## 📖 Table of Contents

  - [What This Project Does](https://www.google.com/search?q=%23-what-this-project-does)
  - [What You'll Learn](https://www.google.com/search?q=%23-what-youll-learn)
  - [Prerequisites](https://www.google.com/search?q=%23-prerequisites)
  - [Complete Installation Guide](https://www.google.com/search?q=%23-complete-installation-guide)
  - [Getting Your API Keys](https://www.google.com/search?q=%23-getting-your-api-keys)
  - [Project Structure Explained](https://www.google.com/search?q=%23-project-structure-explained)
  - [Running the Project](https://www.google.com/search?q=%23-running-the-project)
  - [Understanding the Code](https://www.google.com/search?q=%23-understanding-the-code)
  - [Troubleshooting](https://www.google.com/search?q=%23-troubleshooting)
  - [Making It Your Own](https://www.google.com/search?q=%23-making-it-your-own)

-----

## 🎯 What This Project Does

Imagine you want to know what people are saying about "Python programming" across social media. This project:

1.  **Collects** posts from Reddit and comments from YouTube
2.  **Cleans** the text (removes URLs, special characters, etc.)
3.  **Analyzes** sentiment (positive, negative, or neutral)
4.  **Stores** everything in a database
5.  **Visualizes** the data in a beautiful interactive dashboard

**Example Output:**

```
📊 Total collected: 100 posts
   - 50 from Reddit 
   - 50 from YouTube

🔍 Sentiment Analysis:
   - Positive: 45%
   - Neutral: 35%
   - Negative: 20%

✅ All data stored in database!
```

-----

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

-----

## Quick Start

1.  Clone the repository and change into it:

    `git clone https://github.com/SoulaymaneBoulaich/SOCIAL-MEDIA-ANALYTICS.git`
    `cd SOCIAL-MEDIA-ANALYTICS`

2.  Create and activate a virtual environment (Windows):

    `python -m venv .venv`
    `.venv\Scripts\activate`

3.  Install dependencies:

    `pip install -r requirements.txt`

4.  Create a `.env` file in the project root with your API credentials (example below).

5.  Run the pipeline to collect data and populate the database:

    `python pipeline.py`

6.  Start the dashboard (runs on port 8050 by default):

    `python dashboard.py`

Open `http://127.0.0.1:8050` in your browser to view the dashboard.

-----

## Environment variables (`.env`)

Create a `.env` file in the project root with at least the keys you will use. Example:

```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=YourApp/1.0

YOUTUBE_API_KEY=your_youtube_api_key
```

Important: Never commit `.env` to the repository. Add secrets to your host service's secret manager when deploying.

-----

## Main Files (what they do)

  - `pipeline.py`: Orchestrator — collects from sources, runs processing and sentiment analysis, and stores results to SQLite.
  - `collect_data.py`: Reddit collector (PRAW) — fetches posts and metadata from subreddits.
  - `collect_youtube.py`: YouTube comment collector (Google API client) — searches videos and retrieves comments.
  - `process_data.py`: Text cleaning and preparation utilities (creates `full_text` used for sentiment analysis).
  - `sentiment_analysis.py`: Applies VADER and returns sentiment scores/labels per post.
  - `database.py`: Manages SQLite storage (create tables, insert/update posts, simple queries).
  - `dashboard.py`: Plotly Dash app that queries the database and renders interactive charts and tables.
  - `requirements.txt`: Pin list of Python dependencies for reproducible installs.
  - `.gitignore`: Keeps virtual env, DB files, and secrets out of version control.

-----

## Running and Testing

  - Quick import check:

    `python test_imports.py`

  - Run the full pipeline (collect → process → sentiment → save):

    `python pipeline.py`

  - Start the dashboard:

    `python dashboard.py`

If the dashboard is empty, run the pipeline first, then refresh the dashboard.

-----

## Notes and Best Practices

  - Keep API keys out of version control; use `.env` locally and a secret manager in production.
  - Make sure `.gitignore` excludes `.venv`, `*.db`, `__pycache__/`, and logs.
  - API services enforce rate limits — lower collection `limit` values when you see quota errors.

-----

## Deployment hints

  - Heroku: the repo includes a `Procfile` and `runtime.txt`. Use `heroku config:set` to add credentials (do not commit `.env`).
  - Production: swap SQLite for a managed DB (Postgres) and use environment secrets or a vault.

-----

## Contributing

Contributions welcome. Open a PR with a clear description and small, focused changes. If you add new dependencies, update `requirements.txt`.

-----

## 🔧 Troubleshooting

### Problem: "Python is not recognized"

**Solution:**

1.  Reinstall Python from python.org
2.  Make sure to check ✅ "Add Python to PATH"
3.  Restart Command Prompt

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

1.  Double-check your `.env` file
2.  Make sure there are no extra spaces or quotes
3.  Verify credentials at [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)

**Correct format:**

```env
REDDIT_CLIENT_ID=abc123xyz789
REDDIT_CLIENT_SECRET=secretkey123456789
```

**Wrong format:**

```env
REDDIT_CLIENT_ID = "abc123xyz789"    # No quotes or spaces!
```

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

-----

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

-----

## 🎨 Making It Your Own

### Change What Topics to Track

Edit `pipeline.py` and modify these lines:

```python
# Change subreddit
df_reddit = collect_reddit_posts('gaming', limit=50)  # Changed from 'datascience'

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

⚠️ **Warning:** Higher limits may hit API rate limits\!

### Add More Platforms

You can extend this project to collect from:

  - **Instagram** (using `instaloader`)
  - **TikTok** (using `TikTokApi`)
  - **LinkedIn** (using `linkedin-api`)
  - **Facebook** (using `facebook-sdk`)

-----

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

1.  Download DB Browser from: [https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/)
2.  Install it
3.  Open `social_media.db` file
4.  Browse the `posts` table

### Export Data to Excel

```python
from database import SocialMediaDB

db = SocialMediaDB()
df = db.get_all_posts()

df.to_excel('social_media_data.xlsx', index=False)
print("✓ Exported to social_media_data.xlsx")
```

-----

## 🚀 Running the Project Automatically on Windows Startup

### Method 1: Create a Batch Script

1.  Create `start_pipeline.bat`:

<!-- end list -->

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

2.  Save and double-click `start_pipeline.bat` to run\!

### Method 2: Use Windows Task Scheduler

1.  Open **Task Scheduler** (search in Start Menu)
2.  Click **"Create Basic Task"**
3.  Name it: `Social Media Analytics`
4.  Trigger: **"When I log on"**
5.  Action: **"Start a program"**
6.  Program: `C:\Users\YourName\Documents\social-media-analytics\start_pipeline.bat`
7.  Click **Finish**

Now it runs automatically when you log in to Windows\!

-----

## 📈 Advanced Features to Add

### 1\. Email Notifications

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

### 2\. Save Charts as Images

```python
# In dashboard.py
import plotly.io as pio

fig = create_sentiment_by_platform(df)
pio.write_image(fig, 'sentiment_chart.png')
```

### 3\. Add Word Cloud

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

-----

## ❓ FAQ

**Q: How much does this cost?**
A: $0\! All APIs used have free tiers sufficient for this project.

**Q: Can I use this for my business?**
A: Check each platform's API Terms of Service. This project is educational.

**Q: How do I stop the pipeline?**
A: Press `Ctrl+C` in the Command Prompt window.

**Q: Can I share my API keys?**
A: **NEVER\!** Keep your `.env` file private. Don't upload it to GitHub.

**Q: The dashboard is slow. How to fix?**
A: Reduce the amount of data collected or add pagination to the dashboard.

**Q: Can I deploy this to the cloud?**
A: Yes\! You can deploy to:

  - **Heroku** (free tier available)
  - **AWS EC2** (free tier for 1 year)
  - **Google Cloud** (free tier with credits)
  - **PythonAnywhere** (free tier available)

-----

## 🚀 Heroku Deployment

Follow these steps to deploy the dashboard to Heroku from Windows (Command Prompt):

  - **1. Install Heroku CLI**: [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

  - **2. Log in to Heroku**:

<!-- end list -->

```cmd
heroku login
```

  - **3. Initialize git (if not already a git repo)**:

<!-- end list -->

```cmd
git init
git add .
git commit -m "Prepare app for Heroku"
```

  - **4. Create a Heroku app** (or use an existing name):

<!-- end list -->

```cmd
heroku create my-social-dashboard
```

  - **5. Set required environment variables** (your API keys):

<!-- end list -->

```cmd
heroku config:set REDDIT_CLIENT_ID=your_id_here REDDIT_CLIENT_SECRET=your_secret_here REDDIT_USER_AGENT="MyApp/1.0"
heroku config:set YOUTUBE_API_KEY=your_google_api_key_here
```

  - **6. Push to Heroku**:

<!-- end list -->

```cmd
git push heroku main
```

  - **7. Scale the web dyno (usually already 1)**:

<!-- end list -->

```cmd
heroku ps:scale web=1
```

  - **8. Open the app**:

<!-- end list -->

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

## 🤝 Contributing & Getting Help

### Need Help?

  - **Stack Overflow**: Search for specific error messages
  - **Reddit**: r/learnpython, r/Python
  - **Discord**: Python Discord Server
  - **Documentation**:
      - [Pandas](https://pandas.pydata.org/docs/)
      - [Plotly](https://plotly.com/python/)
      - [PRAW (Reddit)](https://praw.readthedocs.io/)

### Found a Bug?

Create an issue on GitHub describing:

1.  What you expected to happen
2.  What actually happened
3.  Error messages
4.  Steps to reproduce

## 🙏 Acknowledgments

  - **Reddit API** - PRAW library
  - **YouTube API** - Google API Client
  - **VADER** - Sentiment analysis tool
  - **Plotly** - Interactive visualizations
  - **Python Community** - For amazing open-source tools

-----

**Happy Coding\! 🎉**

*Remember: The best way to learn is by doing. Don't be afraid to experiment, break things, and ask questions\!*

-----

*Last Updated: November 2025* *Made By Soulaymane Boulaich*
