**Flipkart Product Review Scraper**
This Python script scrapes customer reviews from a specific product page on Flipkart. It collects details like customer names, review titles, ratings, and comments from multiple pages, then saves the data into a CSV file for easy analysis.

Prerequisites
Ensure you have the following Python libraries installed:

**requests
beautifulsoup4
pandas**

You can install these packages using:pip install requests beautifulsoup4 pandas

How to Use
Open the script file and modify the inputurl variable to the product page URL you want to scrape. Currently, it is set to:
inputurl = "https://www.flipkart.com/marq-flipkart-2024-range-1-5-ton-3-star-split-inverter-4-in-1-convertible-turbo-cool-technology-ac-white/product-reviews/itm90337c1c192b2?pid=ACNGW3NXCJ22ZG7J&lid=LSTACNGW3NXCJ22ZG7JUFWQUH&marketplace=FLIPKART"

The script will fetch reviews from the first five pages of the specified product. You can adjust the page range in the for loop if needed.

A CSV file named Product_sample.csv will be generated in the project directory with the collected data.

Script Details
The script utilizes User-Agent and Accept-Language headers to mimic a browser request, which helps avoid potential blocks by the website.
It iterates over multiple pages, fetching reviews from each one, and handles exceptions in case of connectivity or page loading issues.
The data is stored in lists for customer names, review titles, ratings, and comments, and then combined into a Pandas DataFrame for export.
Note
To avoid getting blocked by the website, the script adds a 2-second delay between requests.
Make sure you are compliant with Flipkart's terms of service while using this scraper.
