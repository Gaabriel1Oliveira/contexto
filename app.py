import streamlit as st
from data_fetcher import fetch_market_data
from analyzer import analyze_context
from reporter import generate_report

st.set_page_config(page_title="Análise Macro do Dólar", layout="wide")
st.title("📊 Análise Macroeconômica do Dólar")

if st.button("Gerar análise agora"):
    with st.spinner("Coletando dados..."):
        data = fetch_market_data()
        context = analyze_context(data)
        report = generate_report(context, data.get("timestamp"))
        st.text_area("📝 Relatório Gerado", report, height=300)
