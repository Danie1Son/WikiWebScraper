# WILL NEED LIBRARIES: requests, bs4, pandas
# TO INSTALL, USE "pip install <library name>" in your IDE terminal

# MODULES TO IMPORT ##############################################
import requests # Module used for making HTTP requests
from bs4 import BeautifulSoup # Module used for reading/parsing HTML received from HTTP request
import pandas as pd # Module for visualizing the parsed HTML fetched from the HTTP request

# BEAUTIFUL SOUP SCRAPE FUNCTION #################################

def scrape_wikipedia(url):
    response = requests.get(url) # get() function from "requests" module is used to fetch data from the HTTP service with the url provided
    soup = BeautifulSoup(response.text, 'html.parser') # BeautifulSoup function to parse the HTML from the HTTP service
    title = soup.find('h1', id='firstHeading').text # BS tells Python the title is the first heading found
    content = soup.find(id='mw-content-text') # BS tells Python the content of the HTML using find() function
    paragraphs = content.find_all('p') # BS tells Python the paragraphs found from the HTML content. find_all() is a BS function that allows to search for certain elements throughout the HTML
    article_text = ' '.join([p.text.strip() for p in paragraphs]) # Pure article text is extracted by joining paragraphs together and reading the text
    images = len(soup.find_all('img')) # Python counts the number of images provided by BS

    return title, article_text, images

# PANDAS CSV RESULTS ##############################################

def save_to_csv(title, article_text, images):
    new_data = pd.DataFrame({ # Pandas DataFrame() function creates a 2D table
        'Title': [title], # DataFrame() lists the "Title" header followed by the parsed HTML data from BS
        'Images': [images], # DataFrame() lists the "Images" header followed by the image count from find_all() earlier
        'Article Text': [article_text] # DataFrame() lists the "Article Text" header and the joined paragraphs retrieved from BS
    })


    new_data.to_csv('wikipedia_scraped_data.csv', index=False) # to_csv() Creates a CSV file to write the scraped data to. index=False tells Pandas not to include an index
    print('\nWebpage Results:\n') # Format the results with \n
    print(new_data) # Print the full Pandas DataFrame in Python output

# INITIALIZE WEB SCRAPING FUNCTION ################################

def load(userinput):
    url = f'https://en.wikipedia.org/wiki/{userinput}' # URL to fetch from HTTP service
    title, article_text, images = scrape_wikipedia(url) # Calls scrape function to get the title, content, images
    save_to_csv(title, article_text, images) # Calls to save the freshly scraped data to a CSV file

# GET USER INPUT & INITIALIZE #####################################

userinput=str(input('Enter the name of the Wikipedia article to scrape. Case-sensitive, enter a "_" instead of a space:\n')) # Asks user for Wikipedia article to scrape
load(userinput) # Initialize & run functions with the user's input for scraping