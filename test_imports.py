#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

errors = []

print("Testing imports...")
print("-" * 50)

try:
    from database import SocialMediaDB
    print("[OK] database.py")
except Exception as e:
    errors.append(f"[FAIL] database.py - {str(e)}")
    print(f"[FAIL] database.py - {str(e)}")

try:
    from collect_data import collect_reddit_posts
    print("[OK] collect_data.py")
except Exception as e:
    errors.append(f"[FAIL] collect_data.py - {str(e)}")
    print(f"[FAIL] collect_data.py - {str(e)}")

try:
    from collect_youtube import collect_youtube_comments
    print("[OK] collect_youtube.py")
except Exception as e:
    errors.append(f"[FAIL] collect_youtube.py - {str(e)}")
    print(f"[FAIL] collect_youtube.py - {str(e)}")

try:
    from process_data import process_data
    print("[OK] process_data.py")
except Exception as e:
    errors.append(f"[FAIL] process_data.py - {str(e)}")
    print(f"[FAIL] process_data.py - {str(e)}")

try:
    from sentiment_analysis import analyze_data
    print("[OK] sentiment_analysis.py")
except Exception as e:
    errors.append(f"[FAIL] sentiment_analysis.py - {str(e)}")
    print(f"[FAIL] sentiment_analysis.py - {str(e)}")

try:
    from pipeline import run_pipeline
    print("[OK] pipeline.py")
except Exception as e:
    errors.append(f"[FAIL] pipeline.py - {str(e)}")
    print(f"[FAIL] pipeline.py - {str(e)}")

print("-" * 50)

if errors:
    print("\nERRORS FOUND:")
    for error in errors:
        print(error)
    sys.exit(1)
else:
    print("\nAll imports successful!")
    sys.exit(0)
