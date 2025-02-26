import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset successfully loaded.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def count_movies_tv_shows(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='type', data=df, hue='type', palette='Set2', legend=False) 
    plt.title('Count of Movies - TV Shows')
    plt.xlabel('Movie or TV Show')
    plt.ylabel('Count')
    plt.show()

def country_distribution(df):
    top_countries = df['country'].value_counts().head(10).reset_index()
    top_countries.columns = ['country', 'count']
    plt.figure(figsize=(10, 6))
    sns.barplot(x='country', y='count', data=top_countries, hue='country', palette='Blues', legend=False) 
    plt.title('Top Countries with Most Movies/TV Shows')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

def release_year_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='release_year', data=df, hue='release_year', palette='coolwarm', legend=False)  
    plt.title('Movies/TV Shows Release Year')
    plt.xlabel('Release Year')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()


def rating_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='rating', data=df, hue='rating', palette='Set1', legend=False) 
    plt.title('Distribution of Ratings for Movies/TV Shows')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

def main():
    file_path = 'netflix_titles.csv'  
    df = load_data(file_path)
    
    if df is not None:
        print("Generating visualizations...\n")

        count_movies_tv_shows(df)
        country_distribution(df)
        release_year_distribution(df)
        rating_distribution(df)

if __name__ == "__main__":
    main()
