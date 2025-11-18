
<<<<<<< HEAD
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
## Social Media Analytics (SMA)

A modular Python project that collects social media data (Reddit, Twitter, YouTube), performs text cleaning and sentiment analysis, stores results in SQLite, and exposes an interactive Plotly Dash dashboard.

This repository contains the core code and instructions to run the pipeline locally on Windows (also works on macOS/Linux with minor path differences).

---

## Quick Start

1. Clone the repository:

    git clone https://github.com/SoulaymaneBoulaich/SOCIAL-MEDIA-ANALYTICS.git
    cd SOCIAL-MEDIA-ANALYTICS

2. Create and activate a virtual environment (Windows):

    python -m venv .venv
    .venv\Scripts\activate

3. Install dependencies:

    pip install -r requirements.txt

4. Create a `.env` file in the project root containing your API keys (example below).

5. Run the pipeline to collect data and populate the database:

    python pipeline.py

6. Start the dashboard:

    python dashboard.py

Open http://127.0.0.1:8050 in your browser to view the dashboard.

---

## Environment variables (.env)

Create a `.env` file with these entries:

REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=YourApp/1.0

TWITTER_BEARER_TOKEN=your_twitter_bearer_token

YOUTUBE_API_KEY=your_youtube_api_key

Do not commit `.env` to source control.

---

## Main Files (what they do)

- `pipeline.py`: Main orchestration script. Collects data from all sources, processes and analyzes it, then stores results in the SQLite database.
- `collect_data.py`: Reddit collector (PRAW). Fetches posts and metadata from subreddits.
- `collect_twitter.py`: Twitter/X collector (Tweepy). Fetches tweets based on a query. (May be optional depending on API access.)
- `collect_youtube.py`: YouTube comment collector (Google API client). Searches for a video and retrieves comments.
- `process_data.py`: Data cleaning utilities (remove URLs, special characters, normalize text) and preparation of `full_text` column.
- `sentiment_analysis.py`: Sentiment scoring using VADER; returns compound scores and labels.
- `database.py`: Lightweight manager for SQLite storage (create tables, insert posts, deduplicate, simple queries).
- `dashboard.py`: Plotly Dash application that reads the database and renders interactive charts and tables.
- `requirements.txt`: Python package dependencies.
- `.gitignore`: Ensures `.venv`, `.env`, DB files, and caches are not committed.

---

## Running and Testing

- Test imports and environment quickly:

  python test_imports.py

- Run the full pipeline:

  python pipeline.py

- Start the dashboard:

  python dashboard.py

If the dashboard shows no data, run the pipeline first and then refresh the page.

---

## Notes and Best Practices

- Keep API keys out of version control. Use `.env` and a `.gitignore` entry.
- Avoid committing large or generated files: `.venv/`, `*.db`, `__pycache__/`, and logs are ignored.
- If you get API errors, verify credentials and consider rate limits.

---

## Deployment hints

- A `Procfile` and `runtime.txt` are included for Heroku deployment. Store secrets with `heroku config:set` rather than committing them.
- For production, consider using a managed database and proper secrets management.

---

## Contributing

Contributions are welcome. For small changes, open a Pull Request with a clear description and tests where appropriate.

---

## License

MIT License. See `LICENSE` for details.

---

If you'd like, I can:
- remove any remaining emoji characters across code files, or
- further polish the dashboard layout and color theme, or
- create a short `FILES.md` that documents each main file in one paragraph.

Which of these would you like me to do next?
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
=======
>>>>>>> ac04673bd7229e391784dc85fdfd748d4e0090f7

