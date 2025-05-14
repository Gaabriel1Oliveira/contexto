import schedule
import time
from main import run_analysis

def schedule_analysis():
    for hour in range(8, 18):  # Das 8h às 17h
        schedule.every().day.at(f"{hour:02}:00").do(run_analysis)

    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    schedule_analysis()
