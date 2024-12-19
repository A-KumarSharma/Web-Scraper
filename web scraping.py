
##basic code of web scraping 

import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = 'https://akkportfolio.netlify.app/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find and extract the data you need
    # For example, extracting all the headings
    headings = soup.find_all()
    for heading in headings:
        print(heading.text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    
    
    
## advance code of web scraping

import scrapy
from bs4 import BeautifulSoup

class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = [
        'https://akkportfolio.netlify.app/',  # Replace with your target URL
    ]

    def parse(self, response):
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the meta description
        meta_description = soup.find('meta', attrs={'name': 'description'})
        if meta_description:
            print("Meta Description:", meta_description['content'])
            yield {'Meta Description': meta_description['content']}
        else:
            print("No meta description found.")
            yield {'Meta Description': 'No meta description found.'}
        
        # Extract the first three paragraphs
        paragraphs = soup.find_all('p')
        if paragraphs:
            for i, paragraph in enumerate(paragraphs[:3]):
                print(f"Paragraph {i+1}:", paragraph.text)
                yield {f'Paragraph {i+1}': paragraph.text}
        else:
            print("No paragraphs found.")
            yield {'Paragraphs': 'No paragraphs found.'}

        # Extracting all the headings
        headings = soup.find_all('h1')
        if headings:
            for heading in headings:
                print("Heading:", heading.text)
                yield {'Heading': heading.text}
        else:
            print("No headings found.")
            yield {'Headings': 'No headings found.'}

# Command to run the spider:
# scrapy crawl myspider
