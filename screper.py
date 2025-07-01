
# [My Code] - Import necessary libraries for web scraping
import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    """
    [My Code] - Fetches content from a given URL and parses it to extract quotes and authors.
    This function is specifically designed for http://quotes.toscrape.com/.
    Args:
        url (str): The URL of the website to scrape.
    Returns:
        list: A list of dictionaries, where each dictionary represents an extracted quote.
    """
    try:
        # [Gemini Code] - Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        # [My Code] - Handle request errors (e.g., network issues, invalid URL)
        print(f"Error fetching the URL: {e}")
        return []

    # [Gemini Code] - Parse the HTML content using BeautifulSoup
    # 'html.parser' is a built-in Python HTML parser
    soup = BeautifulSoup(response.text, 'html.parser')

    # [My Code] - Initialize a list to store extracted data
    quotes_data = []

    # [My Code] - Find all quote containers on the page
    # Inspecting http://quotes.toscrape.com/ shows each quote is in a <div class="quote">
    quote_divs = soup.find_all('div', class_='quote')

    if not quote_divs:
        print(f"No quote divs found with class 'quote' on {url}. Please check selectors or target URL.")
        return []

    # [My Code] - Iterate through each quote div and extract specific elements
    for quote_div in quote_divs:
        # [Gemini Code] - Extract the text of the quote
        # The quote text is in a <span class="text"> tag
        text_tag = quote_div.find('span', class_='text')
        quote_text = text_tag.get_text(strip=True) if text_tag else 'N/A'

        # [Gemini Code] - Extract the author of the quote
        # The author is in a <small class="author"> tag
        author_tag = quote_div.find('small', class_='author')
        author_name = author_tag.get_text(strip=True) if author_tag else 'N/A'

        # [My Code] - Store the extracted quote and author as a dictionary
        quotes_data.append({
            'quote': quote_text,
            'author': author_name
        })
    
    return quotes_data

# [My Code] - Main execution block of the script
if __name__ == "__main__":
    # [My Code] - Target URL for scraping
    # This is a safe public test site for web scraping.
    target_url = "http://quotes.toscrape.com/" 

    print(f"Scraping data from: {target_url}")
    extracted_quotes = scrape_quotes(target_url)

    if extracted_quotes:
        print("\n--- Extracted Quotes ---")
        for i, item in enumerate(extracted_quotes):
            print(f"{i+1}. Quote: \"{item['quote']}\" - Author: {item['author']}")
    else:
        print("No quotes extracted or an error occurred during scraping.")

