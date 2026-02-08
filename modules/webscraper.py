# Import the library here...
from playwright.sync_api import sync_playwright
import os

# These are the desired helpers...
output_path = os.path.join(os.path.dirname(__file__), "..", "output", "webscraped.html")

def scrapeUrl(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge")
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        data = page.content()
        browser.close()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(data)
    
    return "Fetched data using Agentic AI..."