import requests

API_KEY = "XJ2VR15W7GM7LPVJ"

STOCKS = ["AAPL", "MSFT", "TSLA"]

def get_investments():
    results = []

    for symbol in STOCKS:
        url = (
            f"https://www.alphavantage.co/query?"
            f"function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        )

        data = requests.get(url).json()
        quote = data.get("Global Quote", {})

        price = quote.get("05. price", "N/A")

        results.append({
            "name": symbol,
            "value": f"${price}"
        })

    return results
