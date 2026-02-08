# Import the modules here...
from modules.webscraper import scrapeUrl

# Use here...
url = input("enter url: ")
response = scrapeUrl(url)
print(response)