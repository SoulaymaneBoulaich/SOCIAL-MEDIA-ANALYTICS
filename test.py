from database import SocialMediaDB
import pandas as pd

db = SocialMediaDB()
df = db.get_all_posts()

print(f'Total posts in database: {len(df)}')
print(df.head())
print(df.info())

print(df['sentiment_label'].value_counts())