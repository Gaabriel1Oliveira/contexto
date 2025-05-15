import yfinance as yf
 from datetime import datetime
 import pytz # Importe a biblioteca pytz
 

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
  sa_timezone = pytz.timezone('America/Sao_Paulo') # Defina o fuso horário de São Paulo
  now = datetime.now(sa_timezone).strftime("%Y-%m-%d %H:%M:%S") # Obtenha a hora atual em São Paulo
 

  for name, ticker in symbols.items():
  try:
  stock = yf.Ticker(ticker)
  hist = stock.history(period="1d", interval="1h")
  if len(hist) > 1: # Verifique se há dados suficientes
  latest = hist.iloc[-1]
  previous = hist.iloc[-2]
  price = latest["Close"]
  change = ((price - previous["Close"]) / previous["Close"]) * 100
  data[name] = {
  "price": round(price, 4),
  "change_pct": round(change, 2),
  }
  else:
  data[name] = {"error": "Insufficient data"}
  except Exception as e:
  data[name] = {"error": str(e)}
 

  data["timestamp"] = now
  return data