#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SMA Project Startup Script
Verifies all dependencies and sets up the environment before running the pipeline.
"""

import sys
import os
import subprocess

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def check_env_file():
    """Verify .env file exists with required keys"""
    if not os.path.exists('.env'):
        print("[WARNING] .env file not found!")
        print("          Create a .env file with:")
        print("          - REDDIT_CLIENT_ID")
        print("          - REDDIT_CLIENT_SECRET")
        print("          - REDDIT_USER_AGENT")
        print("          - YOUTUBE_API_KEY")
        return False
    return True

def check_dependencies():
    """Verify all Python dependencies are installed"""
    required_packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn',
        'praw', 'tweepy', 'google-api-python-client', 'textblob',
        'vaderSentiment', 'sqlalchemy', 'plotly', 'dash',
        'schedule', 'python-dotenv', 'spacy', 'scikit-learn',
        'nltk', 'joblib', 'gunicorn'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing.append(package)
    
    if missing:
        print("[WARNING] Missing packages:")
        for pkg in missing:
            print(f"          - {pkg}")
        print("\nRun: pip install -r requirements.txt")
        return False
    return True

def check_imports():
    """Verify all project modules can be imported"""
    modules = [
        'database',
        'collect_data',
        'collect_youtube',
        'process_data',
        'sentiment_analysis',
        'pipeline'
    ]
    
    failed = []
    for module in modules:
        try:
            __import__(module)
        except ImportError as e:
            failed.append(f"{module}: {str(e)}")
    
    if failed:
        print("[FAIL] Module import errors:")
        for error in failed:
            print(f"       - {error}")
        return False
    return True

def verify_directories():
    """Create necessary directories if they don't exist"""
    dirs_to_create = [
        'csv_examples',
        'db_examples',
        'plots',
        'scripts'
    ]
    
    for directory in dirs_to_create:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"[CREATED] {directory}/")

def main():
    print("=" * 60)
    print("SMA PROJECT VERIFICATION")
    print("=" * 60)
    
    all_ok = True
    
    print("\n[1] Checking environment file...")
    if check_env_file():
        print("    [OK] .env file found")
    else:
        all_ok = False
    
    print("\n[2] Checking dependencies...")
    if check_dependencies():
        print("    [OK] All dependencies installed")
    else:
        all_ok = False
    
    print("\n[3] Checking project modules...")
    if check_imports():
        print("    [OK] All modules imported successfully")
    else:
        all_ok = False
    
    print("\n[4] Verifying directory structure...")
    verify_directories()
    print("    [OK] Directory structure verified")
    
    print("\n" + "=" * 60)
    if all_ok:
        print("SUCCESS: Project is ready to run!")
        print("=" * 60)
        print("\nTo run the pipeline, execute:")
        print("  python pipeline.py")
        print("\nTo run the dashboard, execute:")
        print("  python dashboard.py")
        return 0
    else:
        print("WARNING: Some issues detected above")
        print("Please fix the issues before running the project")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
