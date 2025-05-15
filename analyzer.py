def analyze_context(data):
  context = []
 

  try:
  dxy = data.get("DXY", {}).get("change_pct")
  treasuries = data.get("10Y Treasury", {}).get("change_pct")
  vix = data.get("VIX", {}).get("change_pct")
 

  if dxy is not None:
  if dxy > 0.3:
  context.append("O DXY sobe, indicando fortalecimento global do dólar.")
  elif dxy < -0.3:
  context.append("O DXY recua, sugerindo enfraquecimento global do dólar.")
 

  if treasuries is not None:
  if treasuries > 0.2:
  context.append("Os Treasuries de 10 anos sobem, reforçando expectativa de juros altos nos EUA.")
  elif treasuries < -0.2:
  context.append("Os Treasuries caem, indicando possível alívio nas taxas futuras.")
 

  if vix is not None:
  if vix > 1:
  context.append("O VIX sobe, apontando aumento da aversão ao risco no mercado.")
  elif vix < -1:
  context.append("O VIX recua, sugerindo melhora no apetite ao risco.")
 

  brent = data.get("Brent", {}).get("change_pct")
  wti = data.get("WTI", {}).get("change_pct")
  if brent is not None and wti is not None:
  if brent < 0 and wti < 0:
  context.append("O recuo do petróleo pode pressionar moedas de países exportadores, como Brasil e México.")
 

  usd_brl = data.get("USD/BRL", {}).get("change_pct")
  usd_mxn = data.get("USD/MXN", {}).get("change_pct")
  if usd_brl is not None:
  if usd_brl > 0.4:
  context.append("O dólar sobe frente ao real, refletindo pressão no câmbio brasileiro.")
  if usd_mxn is not None:
  if usd_mxn > 0.4:
  context.append("O dólar sobe contra o peso mexicano, sugerindo fuga de capital da região.")
 

  except Exception as e:
  context.append(f"Erro na análise: {str(e)}")
 

  return context