import pandas as pd
import numpy as np

# 1. FIXED: Corrected the path/string and ensured the file is loaded
# Make sure "Movies.csv" is in the same folder as your script
try:
    df = pd.read_csv("Movies.csv")
except FileNotFoundError:
    print("Error: 'Movies.csv' not found. Please ensure the file exists.")
    # Creating dummy data for demonstration if file is missing
    data = {
        'movie_name': ['Movie A', 'Movie B', 'Movie C'],
        'budget': [100, 150, 50],
        'revenue': [500, 100, 300],
        'rating': [9.0, 6.5, 8.8],
        'genre': ['Action', 'Drama', 'Action'],
        'release_year': [1994, 2010, 1999]
    }
    df = pd.DataFrame(data)

# Quick look at the data
print("First 5 movies:")
print(df.head())
print()

# 2. FIXED: Profit formula was subtracting budget from budget (resulting in 0)
# Formula should be Revenue - Budget
df['profit'] = df['revenue'] - df['budget']

# Basic Statistics
total_movies = len(df)
avg_rating = df["rating"].mean()
highest_rating = df['rating'].max()
lowest_rating = df['rating'].min()

# Using .get() or checking columns to avoid errors if data is missing
avg_budget = df[df['budget'] > 0]['budget'].mean()
avg_revenue = df[df['revenue'] > 0]['revenue'].mean()
total_profit_all = df['profit'].sum()

# Find the best and worst performers
most_profitable = df.loc[df['profit'].idxmax()]
highest_rated = df.loc[df['rating'].idxmax()]
biggest_budget = df.loc[df['budget'].idxmax()]
biggest_box_office = df.loc[df['revenue'].idxmax()]

# Genre analysis
genre_counts = df['genre'].value_counts()
most_common_genre = genre_counts.index[0]
avg_rating_by_genre = df.groupby('genre')['rating'].mean()
highest_genre_rating = avg_rating_by_genre.idxmax()

# Year analysis
oldest_year = int(df['release_year'].min())
newest_year = int(df['release_year'].max())
movies_90s = df[(df['release_year'] >= 1990) & (df['release_year'] < 2000)]
num_90s_movies = len(movies_90s)

# Success metrics
profitable_movies = df[df['profit'] > 0]
profit_rate = (len(profitable_movies) / total_movies) * 100

# Super hits: profit > 500 million AND rating > 8.5
super_hits = df[(df['profit'] > 500) & (df['rating'] > 8.5)]
num_super_hits = len(super_hits)

# More insights - Highest ROI
df_safe = df[df['budget'] > 0].copy()
df_safe['roi'] = (df_safe['profit'] / df_safe['budget']) * 100
best_roi_movie = df_safe.loc[df_safe['roi'].idxmax()]

# Final Executive Summary Report
print("=" * 60)
print("           TOP 100 MOVIES - EXECUTIVE ANALYSIS REPORT")
print("=" * 60)
print(f"Total Movies Analyzed: {total_movies}")
print(f"Release Years Covered: {oldest_year} - {newest_year}")
print(f"Average IMDb Rating: {avg_rating:.2f}")
print(f"Highest Rated Movie: {highest_rated['movie_name']} ({highest_rating})")
print("_" * 60)
print("BOX OFFICE HIGHLIGHTS")
print(f"Most Profitable Movie: {most_profitable['movie_name']} (${most_profitable['profit']}M profit)")
print(f"Highest Grossing: {biggest_box_office['movie_name']} (${biggest_box_office['revenue']}M)")
print(f"Biggest Budget: {biggest_budget['movie_name']} (${biggest_budget['budget']}M)")
print(f"Best ROI: {best_roi_movie['movie_name']} ({best_roi_movie['roi']:.1f}% return)")
print("_" * 60)
print("GENRE INSIGHTS")
print(f"Most Common Genre: {most_common_genre} ({genre_counts.iloc[0]} movies)")
print(f"Highest Average Rated Genre: {highest_genre_rating}")
print("_" * 60)
print("SUCCESS METRICS")
print(f"Profitability Rate: {profit_rate:.1f}% of movies made profit")
print(f"Number of Super Hits (Profit > $500M + Rating > 8.5): {num_super_hits}")
print(f"Movies from the 1990s in Top 100: {num_90s_movies}")
print("_" * 60)
print("END OF REPORT - Great job learning pandas!")
print("=" * 60)