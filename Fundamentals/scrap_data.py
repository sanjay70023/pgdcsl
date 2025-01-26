# Write a Python script to scrape data from a website using the BeautifulSoup library 
# and save the extracted data to a CSV file.


import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, output_file):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extract all headings (h1, h2, h3)
        headings = []
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            headings.append({
                "Tag": heading.name,
                "Content": heading.get_text(strip=True)
            })

        # Write data to a CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Tag', 'Content']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(headings)

        print(f"Data scraped and saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = input("Enter the URL to scrape: ")
output_file = "scraped_data.csv"
scrape_website(url, output_file)
