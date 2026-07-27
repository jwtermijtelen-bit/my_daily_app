import requests

API_KEY = "YOUR_ALPHA_VANTAGE_KEY"

def get_commodities():
    gold_url = f"https://www.alphavantage.co/query?function=COMMODITY_EXCHANGE_RATE&from_symbol=XAU&to_symbol=USD&apikey={API_KEY}"
    oil_url = f"https://www.alphavantage.co/query?function=WTI&apikey={API_KEY}"

    gold_data = requests.get(gold_url).json()
    oil_data = requests.get(oil_url).json()

    gold_price = gold_data.get("Realtime Commodity Exchange Rate", {}).get("5. Exchange Rate", "N/A")
    oil_price = oil_data.get("data", [{}])[0].get("value", "N/A")

    return [
        {"name": "Gold", "price": f"${gold_price}"},
        {"name": "Oil (WTI)", "price": f"${oil_price}"}
    ]
