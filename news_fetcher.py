import requests
import json

def fetch_news():
    #user input
    query = input('What type of news you want:')

    url = f"https://newsapi.org/v2/everything?q={query}&from=2024-01-23&sortBy=publishedAt&apiKey=API_KEY"
    
    r = requests.get(url)
    
    # Parsing the JSON response
    news = json.loads(r.text)
    
    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("-------------------------------------------")


fetch_news()
