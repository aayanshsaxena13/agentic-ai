# Import the library here...
import requests
import os

# These are the desired helpers...
output_path = os.path.join(os.path.dirname(__file__), "..", "output", "webscraped.html")

def scrapeUrl(url):
    data = requests.get(url).text
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(data)
    return "Fetched data using Agentic AI..."