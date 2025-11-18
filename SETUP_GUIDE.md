# SMA - Social Media Analytics Project

## Project Setup & Recovery Guide

This guide helps you fix any issues after deleting and restoring the project folder.

### Quick Start (After Folder Restoration)

```bash
# 1. Run the project fix script
python fix_project.py

# 2. Run the pipeline
python pipeline.py

# 3. Launch the dashboard
python dashboard.py
```

---

## Prerequisites

- Python 3.11+
- Virtual Environment (`.venv` folder)
- All dependencies installed

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
SMA/
├── __init__.py                    # Package initialization
├── .env                           # API credentials (keep secret!)
├── requirements.txt               # Python dependencies
├── database.py                    # Database operations
├── collect_data.py               # Reddit data collection
├── collect_youtube.py            # YouTube data collection
├── process_data.py               # Data cleaning
├── sentiment_analysis.py         # Sentiment analysis using VADER
├── pipeline.py                   # Main data pipeline
├── dashboard.py                  # Dash visualization dashboard
├── test.py                       # Quick database test
├── fix_project.py                # Post-restore fix script
├── verify_project.py             # Project verification
├── run_project.bat               # Windows launcher
├── scripts/
│   ├── __init__.py
│   ├── fix_dbs.py               # Database fix utilities
│   └── smoke_test_dashboard.py  # Dashboard smoke test
├── csv_examples/                 # Example CSV files
├── db_examples/                  # Example database files
└── plots/                        # Generated plots directory
```

---

## What to Do After Folder Restoration

### Option 1: Automatic Fix (Recommended)

Run the automatic fix script:

```bash
python fix_project.py
```

This will:
- [OK] Create missing `__init__.py` files
- [OK] Clean up `__pycache__` directories
- [OK] Verify directory structure
- [OK] Check all dependencies

### Option 2: Manual Setup

If automatic fix doesn't work, follow these steps:

1. **Clean up Python cache:**
   ```bash
   find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null
   ```

2. **Ensure `__init__.py` exists:**
   ```bash
   touch __init__.py
   touch scripts/__init__.py
   ```

3. **Verify dependencies:**
   ```bash
   python verify_project.py
   ```

4. **Test imports:**
   ```bash
   python test_imports.py
   ```

---

## Running the Project

### Method 1: Direct Python Execution

**Run the Data Pipeline:**
```bash
python pipeline.py
```

**Launch the Dashboard:**
```bash
python dashboard.py
```
Then open: `http://127.0.0.1:8050`

**Run Database Test:**
```bash
python test.py
```

### Method 2: Windows Batch File

Simply run:
```bash
run_project.bat
```

This opens an interactive menu to select what to run.

---

## Configuration

### .env File Requirements

The `.env` file must contain:

```env
# Reddit API
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=Analytics/1.0

# YouTube API
YOUTUBE_API_KEY=your_api_key
```

**Note:** Keep your `.env` file secure and never commit it to version control!

---

## Troubleshooting

### Issue: "Module not found" errors

**Solution:**
```bash
python fix_project.py
```

### Issue: "No module named 'praw'" or similar

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: __pycache__ conflicts

**Solution:**
```bash
python fix_project.py
```

### Issue: Dashboard won't start

**Check dependencies:**
```bash
python verify_project.py
```

---

## Project Modules

### `database.py`
Handles all SQLite database operations:
- Create tables for different platforms (Reddit, YouTube)
- Insert posts and comments
- Store sentiment analysis results
- Retrieve and summarize statistics

### `collect_data.py`
Reddit data collection using PRAW API:
- Search subreddits
- Extract post data
- Save to CSV

### `collect_youtube.py`
YouTube comment collection using Google API:
- Search videos
- Extract comments
- Save to CSV

### `process_data.py`
Data cleaning and preprocessing:
- Remove URLs and special characters
- Remove duplicates
- Clean text for sentiment analysis

### `sentiment_analysis.py`
Sentiment analysis using VADER:
- Classify as positive, negative, neutral
- Calculate sentiment scores
- Summarize by platform

### `pipeline.py`
Main orchestration pipeline:
- Collect from multiple platforms
- Process data
- Analyze sentiment
- Store in database
- Generate statistics

### `dashboard.py`
Interactive Dash visualization dashboard:
- Sentiment distribution charts
- Timeline trends
- Platform comparison
- Top posts by engagement

---

## Common Commands

```bash
# Fix after folder restoration
python fix_project.py

# Verify project setup
python verify_project.py

# Test imports
python test_imports.py

# Run data pipeline
python pipeline.py

# Launch dashboard
python dashboard.py

# Test database
python test.py

# Smoke test dashboard
python scripts/smoke_test_dashboard.py
```

---

## Performance Notes

- First run may take time to collect and process data
- Dashboard requires at least some data in the database
- API rate limits may apply (Reddit: 60 requests/min, YouTube: quota-based)

---

## Questions?

For issues or questions:
1. Check the troubleshooting section above
2. Run `python verify_project.py` to diagnose issues
3. Review `.env` file for API credentials
4. Check internet connection for API access

---

## Dependencies

- **pandas** - Data manipulation
- **numpy** - Numerical operations
- **matplotlib, seaborn** - Visualization
- **praw** - Reddit API
- **tweepy** - Twitter API (optional)
- **google-api-python-client** - YouTube API
- **vaderSentiment** - Sentiment analysis
- **plotly, dash** - Interactive dashboards
- **sqlalchemy** - Database ORM
- **python-dotenv** - Environment variables

---

**Happy Analyzing!**
