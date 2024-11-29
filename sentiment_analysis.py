import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load cleaned data
df = pd.read_csv('data/cleaned_data.csv')

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Ensure all entries in 'cleaned_message' are strings
df['cleaned_message'] = df['cleaned_message'].fillna('')  # Replace NaN with an empty string
df['cleaned_message'] = df['cleaned_message'].astype(str)  # Ensure all are strings

# Compute sentiment scores
df['sentiment'] = df['cleaned_message'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

# Save data with sentiment scores
df.to_csv('data/sentiment_data.csv', index=False)
print("Sentiment data saved to data/sentiment_data.csv.")
