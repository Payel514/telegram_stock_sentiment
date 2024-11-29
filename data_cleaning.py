import pandas as pd
import re

# Load raw data
df = pd.read_csv('data/raw_data.csv')

# Clean the text data
def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r"http\S+", "", text)  # Remove URLs
        text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
        return text.lower()
    return text

# Apply cleaning
df['cleaned_message'] = df['message'].apply(clean_text)

# Save cleaned data
df.to_csv('data/cleaned_data.csv', index=False)
print("Cleaned data saved to data/cleaned_data.csv.")
