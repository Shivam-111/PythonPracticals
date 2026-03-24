import pandas as pd

# Adjust the path to where your books.csv is located
file_path = r"Book.csv"

# Read the CSV file
df = pd.read_csv(file_path)

print("Preview of data:")
print(df.head())   # shows first 5 rows

# a) Print the complete report of books in tabular form
print("=== Complete Report of Books ===")
print(df.to_string(index=False))

# b) Print the list of available books of a given author
author = input("\nEnter author name: ")
books_by_author = df[df['author'].str.lower() == author.lower()]
print(f"\nBooks by {author}:")
print(books_by_author if not books_by_author.empty else "No books found.")

# c) Print the list of available books of a given publishing house
pub_house = input("\nEnter publishing house: ")
books_by_pub = df[df['publishing_house'].str.lower() == pub_house.lower()]
print(f"\nBooks from {pub_house}:")
print(books_by_pub if not books_by_pub.empty else "No books found.")

# d) Print the Titles of cheapest & costliest book available
cheapest = df.loc[df['price'].idxmin()]
costliest = df.loc[df['price'].idxmax()]
print("\nCheapest Book:", cheapest['title'], "Price:", cheapest['price'])
print("Costliest Book:", costliest['title'], "Price:", costliest['price'])

# e) Print the list by sorting based on the year of publication
print("\n=== Books sorted by year of publication ===")
print(df.sort_values(by='publication_year').to_string(index=False))