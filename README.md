# Dollar Context Analyzer

Ferramenta automatizada para gerar análises de contexto macroeconômico do dólar de hora em hora, entre 08h e 17h.

## 📌 Funcionalidades

- Coleta dados de mercado via Yahoo Finance:
  - Moedas: USD/BRL, USD/MXN, USD/AUD, USD/ZAR
  - Índices: DXY, VIX
  - Títulos: Treasuries 10Y
  - Commodities: Brent e WTI
- Analisa variações percentuais por hora
- Gera relatórios com linguagem natural
- Pode ser agendado para rodar automaticamente

## 📁 Estrutura dos Arquivos

- `main.py`: Executa uma análise pontual
- `data_fetcher.py`: Faz a coleta dos dados de mercado
- `analyzer.py`: Interpreta os dados e extrai o contexto
- `reporter.py`: Gera o texto da análise
- `scheduler.py`: Agendamento de execução de hora em hora

## ▶️ Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/dollar-context-analyzer.git
cd dollar-context-analyzer
```

2. Instale as dependências:

```bash
pip install yfinance schedule
```

3. Execute manualmente:

```bash
python main.py
```

4. Ou agende para rodar das 8h às 17h:

```bash
python scheduler.py
```

## ✅ Exemplo de Saída

```
🕒 Análise das 10:00:
----------------------------------------
- O DXY sobe, indicando fortalecimento global do dólar.
- Os Treasuries de 10 anos sobem, reforçando expectativa de juros altos nos EUA.
- O VIX sobe, apontando aumento da aversão ao risco no mercado.
- O recuo do petróleo pode pressionar moedas de países exportadores, como Brasil e México.
- O dólar sobe frente ao real, refletindo pressão no câmbio brasileiro.
```

---

Criado com ❤️ usando Python e dados financeiros em tempo real.
