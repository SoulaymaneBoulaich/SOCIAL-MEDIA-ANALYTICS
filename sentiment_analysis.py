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