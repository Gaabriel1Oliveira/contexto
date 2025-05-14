def generate_report(context_list, timestamp=None):
    hora = timestamp.split(" ")[1][:5] if timestamp else "Horário desconhecido"

    header = f"\n🕒 Análise das {hora}:\n"
    divider = "-" * 40
    body = "\n".join(f"- {item}" for item in context_list) if context_list else "Sem dados suficientes para análise."

    return f"{header}{divider}\n{body}\n"
