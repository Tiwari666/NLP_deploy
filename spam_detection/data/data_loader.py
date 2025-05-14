import pandas as pd
import re
import os
import sys  


def load_clean_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Absolute path
    path = os.path.join(base_dir, "processed", "cleaned_spam.csv")  

    df = pd.read_csv(path)

    if 'clean_text' not in df.columns:
        df['clean_text'] = df['text'].apply(
            lambda x: re.sub(r'[^a-zA-Z\s]', '', str(x)).lower().split()
        )

    return df


if __name__ == "__main__":
    df = load_clean_data()
    print(df.head())
    print("Data loaded successfully.")
    print("Data shape:", df.shape)



# python data/data_loader.py
# cd C:\Users\naren\Desktop\New DS\spam_detection