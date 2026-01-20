# Import the library here...
import requests

# These are the desired helpers...
output_Path = r"C:\Users\DELL\OneDrive\Desktop\agentic-ai\output\output.html"

def getUrl(url):
    data = requests.get(url).text
    return data
