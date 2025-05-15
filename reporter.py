
import datetime
import pytz
from economic_calendar import fetch_important_events

def format_event_alerts(events):
    if not events:
        return "Nenhum evento relevante encontrado para hoje."

    alerts = "✅ Eventos Econômicos Relevantes:\n"
    for e in events:
        country_flag = "🇺🇸" if e["country"] == "United States" else "🇧🇷"
        time = datetime.datetime.fromisoformat(e["date"]).strftime("%H:%M")
        stars = "★" * e.get("importance", 1)
        alerts += f"- {country_flag} {e['event']} às {time} - Impacto: {stars}\n"
    return alerts.strip()

def generate_report(context_data, timestamp=None):
    br_tz = pytz.timezone("America/Sao_Paulo")
    now = timestamp if timestamp else datetime.datetime.now(br_tz).strftime("%H:%M")
    events = fetch_important_events()
    events_section = format_event_alerts(events)

    report = f"🕒 Análise das {now}:\n"
    report += "----------------------------------------\n"
    report += events_section + "\n\n"

    report += "📊 Contexto Macroeconômico:\n"
    for item in context_data:
        report += f"- {item}\n"

    return report.strip()
