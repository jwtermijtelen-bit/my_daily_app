import requests

API_KEY = "7c79496b5e0f478d90133c69c9482664"

def get_news():
    url = (
        "https://newsapi.org/v2/top-headlines?"
        "country=gb&"
        f"apiKey={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    articles = []
    for item in data.get("articles", []):
        articles.append({
            "title": item.get("title"),
            "summary": item.get("description"),
            "url": item.get("url")
        })

    return articles[:5]  # return top 5
