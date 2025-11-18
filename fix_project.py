#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SMA Project - Post-Restore Fix Script
Fixes any issues that occur after deleting and restoring the project folder.
"""

import os
import sys
import subprocess
from pathlib import Path

def ensure_init_files():
    """Ensure all __init__.py files exist in Python packages"""
    dirs = [
        os.path.dirname(os.path.abspath(__file__)),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')
    ]
    
    for directory in dirs:
        init_file = os.path.join(directory, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w', encoding='utf-8') as f:
                f.write('# Package initialization\n')
            print(f"[CREATED] {init_file}")

def clean_pycache():
    """Remove all __pycache__ directories"""
    import shutil
    
    for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
                print(f"[REMOVED] {pycache_path}")
            except Exception as e:
                print(f"[WARNING] Could not remove {pycache_path}: {e}")

def verify_directories():
    """Create necessary directories if they don't exist"""
    dirs = ['csv_examples', 'db_examples', 'plots', 'scripts']
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for directory in dirs:
        full_path = os.path.join(base_dir, directory)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"[CREATED] {directory}/")

def verify_requirements():
    """Check if all required packages are installed"""
    try:
        # Test critical imports
        import pandas
        import praw
        import numpy
        import plotly
        import dash
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        from googleapiclient.discovery import build
        
        print("[OK] All critical dependencies are installed")
        return True
    except ImportError as e:
        print(f"[WARNING] Missing dependency: {e}")
        print("\nTo install all dependencies, run:")
        print("  pip install -r requirements.txt")
        return False

def main():
    print("=" * 60)
    print("SMA PROJECT - POST-RESTORE FIX")
    print("=" * 60)
    
    print("\n[1] Ensuring __init__.py files...")
    ensure_init_files()
    
    print("\n[2] Cleaning __pycache__ directories...")
    clean_pycache()
    
    print("\n[3] Verifying directory structure...")
    verify_directories()
    
    print("\n[4] Checking dependencies...")
    deps_ok = verify_requirements()
    
    print("\n" + "=" * 60)
    print("FIX COMPLETE!")
    print("=" * 60)
    
    print("\nYou can now run:")
    print("  python pipeline.py     - Run data collection pipeline")
    print("  python dashboard.py    - Launch the dashboard")
    print("  python test.py         - Run tests")
    
    return 0 if deps_ok else 1

if __name__ == "__main__":
    sys.exit(main())
