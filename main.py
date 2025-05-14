from data_fetcher import fetch_market_data
from analyzer import analyze_context
from reporter import generate_report

def run_analysis():
    data = fetch_market_data()
    context = analyze_context(data)
    report = generate_report(context, data.get("timestamp"))
    print(report)

if __name__ == "__main__":
    run_analysis()
