import schedule
 import time
 from main import run_analysis
 import pytz # Importe a biblioteca pytz
 

 def schedule_analysis():
  sa_timezone = pytz.timezone('America/Sao_Paulo') # Defina o fuso horário de São Paulo
  for hour in range(8, 18): # Das 8h às 17h
  schedule.every().day.at(f"{hour:02}:00", sa_timezone).do(run_analysis)
 

  while True:
  schedule.run_pending()
  time.sleep(30)
 

 if __name__ == "__main__":
  schedule_analysis()