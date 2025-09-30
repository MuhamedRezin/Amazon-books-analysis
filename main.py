import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print(pd.__version__)
df = pd.read_csv("bestsellers.csv", encoding="utf-8")
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
df["Price"] = df["Price"].replace('[\$,]', '', regex=True).astype(float)

author_counts = df['Author'].value_counts()
for author, count in author_counts.items():
    safe_author = author.encode("ascii", errors="ignore").decode()
    print(safe_author, count)
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)
# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
import matplotlib
import seaborn
print(matplotlib.__version__, seaborn.__version__)
top_authors = df['Author'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_authors.values, y=top_authors.index, palette='viridis')
plt.title('Top 10 Authors by Number of Bestsellers')
plt.xlabel('Number of Books')
plt.ylabel('Author')
plt.tight_layout()
plt.savefig('outputs/top_authors.png', dpi=150)
plt.show()
avg_rating = df.groupby('Genre')['Rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=avg_rating.index, y=avg_rating.values, palette='coolwarm')
plt.title('Average Rating by Genre')
plt.ylabel('Average Rating')
plt.xlabel('Genre')
plt.tight_layout()
plt.savefig('outputs/avg_rating_genre.png', dpi=150)
plt.show()
plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=20, kde=True, color='skyblue')
plt.title('Price Distribution of Bestsellers')
plt.xlabel('Price')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('outputs/price_distribution.png', dpi=150)
plt.show()
import os
if not os.path.exists('outputs'):
    os.makedirs('outputs')
