# Import statements here...
from openrouter import OpenRouter
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(".env")

# Create the helper function...
def chat(message: str):
    client = OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY"))
    
    response = client.chat.send(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        messages=[{"role": "user", "content": message}]
    )
    
    return response.choices[0].message.content