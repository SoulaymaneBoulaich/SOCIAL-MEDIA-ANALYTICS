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