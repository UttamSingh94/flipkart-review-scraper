import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# User-Agent and Accept-Language headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Accept-Language': 'en-us,en;q=0.5'
}

customer_names = []
review_titles = []
ratings = []
comments = []

# iterate the page based on your requrement
for i in range(1, 6):
    # Construct the URL for the current page
    inputurl="https://www.flipkart.com/marq-flipkart-2024-range-1-5-ton-3-star-split-inverter-4-in-1-convertible-turbo-cool-technology-ac-white/product-reviews/itm90337c1c192b2?pid=ACNGW3NXCJ22ZG7J&lid=LSTACNGW3NXCJ22ZG7JUFWQUH&marketplace=FLIPKART"  #given by user
    url = f"{inputurl}&page={i}"
    print(f"\nFetching data from page {i}...")

    try:
        # Send a GET request to the page
        page = requests.get(url, headers=headers)
        page.raise_for_status()  # Check for request errors

        # Parse the HTML content
        soup = BeautifulSoup(page.content, 'html.parser')

        # Extract customer names
        names = soup.find_all('p', class_='_2NsDsF AwS1CA')
        for name in names:
            customer_names.append(name.get_text())

        # Extract review titles
        titles = soup.find_all('p', class_='z9E0IG')
        for title in titles:
            review_titles.append(title.get_text())

        # Extract ratings
        ratings_elements = soup.find_all('div', class_='XQDdHH Ga3i8K')
        for r in ratings_elements:
            rating = r.get_text()
            ratings.append(rating if rating else '0')  # Replace null ratings with '0'

        # Extract comments
        comments_elements = soup.find_all('div', class_='ZmyHeo')
        for c in comments_elements:
            comment_text = c.div.div.get_text(strip=True) if c.div and c.div.div else ''
            comments.append(comment_text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching page {i}: {e}")
        continue  # Skip to the next page if there was an error

    # Add a delay to avoid IP blocking
    time.sleep(2)  # delay of 2 seconds between requests

# Ensure all lists have the same length
min_length = min(len(customer_names), len(review_titles), len(ratings), len(comments))
customer_names = customer_names[:min_length]
review_titles = review_titles[:min_length]
ratings = ratings[:min_length]
comments = comments[:min_length]

# Create a DataFrame from the collected data
data = {
    'Customer Name': customer_names,
    'Review Title': review_titles,
    'Rating': ratings,
    'Comment': comments
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file with UTF-8 BOM encoding
csv_filename = 'Product_sample.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
print(f"\nCSV file '{csv_filename}' has been created successfully.")
