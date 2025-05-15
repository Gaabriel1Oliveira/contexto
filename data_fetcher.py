import yfinance as yf
from datetime import datetime

def fetch_market_data():
    symbols = {
        "USD/BRL": "USDBRL=X",
        "USD/MXN": "USDMXN=X",
        "USD/AUD": "AUDUSD=X",
        "USD/ZAR": "USDZAR=X",
        "DXY": "DX-Y.NYB",
        "10Y Treasury": "^TNX",
        "VIX": "^VIX",
        "Brent": "BZ=F",
        "WTI": "CL=F",
    }

    data = {}
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for name, ticker in symbols.items():
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d", interval="1h")
            latest = hist.iloc[-1]
            previous = hist.iloc[-2]
            price = latest["Close"]
            change = ((price - previous["Close"]) / previous["Close"]) * 100
            data[name] = {
                "price": round(price, 4),
                "change_pct": round(change, 2),
            }
        except Exception as e:
            data[name] = {"error": str(e)}

    data["timestamp"] = now
    return data
