import yfinance as yf

def get_investments():
    portfolio = {
        "AAPL": yf.Ticker("AAPL").info.get("currentPrice"),
        "MSFT": yf.Ticker("MSFT").info.get("currentPrice"),
        "TSLA": yf.Ticker("TSLA").info.get("currentPrice")
    }

    results = []
    for name, price in portfolio.items():
        results.append({"name": name, "value": f"${price}"})

    return results
