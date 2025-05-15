import logging
 from data_fetcher import fetch_market_data
 from analyzer import analyze_context
 from reporter import generate_report
 

 # Configurar o logging
 logging.basicConfig(filename='analysis.log', level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s')
 

 def run_analysis():
  try:
  data = fetch_market_data()
  logging.info("Dados coletados com sucesso.")
  context = analyze_context(data)
  logging.info("Análise de contexto concluída.")
  report = generate_report(context, data.get("timestamp"))
  print(report)
  logging.info("Relatório gerado e exibido.")
  except Exception as e:
  logging.error(f"Erro durante a análise: {str(e)}")
 

 if __name__ == "__main__":
  run_analysis()