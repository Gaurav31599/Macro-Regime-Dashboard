# 🌍 Macro Regime Dashboard

A Streamlit-based financial intelligence dashboard that tracks key macroeconomic indicators, classifies the current market regime, and generates an AI-powered macro brief using NVIDIA-hosted language models.

This project is designed to demonstrate how financial data, rule-based market logic, and generative AI can be combined into a practical decision-support tool for investors, analysts, fintech teams, and business strategy users.

---

## 🚀 Project Summary

The **Macro Regime Dashboard** helps users quickly understand whether markets are currently operating in a **risk-on**, **risk-off**, **stagflation-risk**, or **neutral/transitional** environment.

It pulls live market data from Yahoo Finance, visualises six-month trends, calculates 30-day changes, classifies the market regime using macro rules, and generates a concise AI analyst-style interpretation of the current macro environment.

---

## 💼 Business Problem It Solves

Financial markets move quickly, and investors often struggle to connect multiple macro signals into one clear market view.

Most people look at indicators such as the S&P 500, VIX, oil, gold, and bond yields separately. This creates three problems:

1. **Fragmented decision-making**  
   Users need to check multiple websites and manually interpret unrelated charts.

2. **Slow macro interpretation**  
   Retail investors, analysts, and business teams may not have time to translate raw market data into a clear investment or risk view.

3. **Lack of explainability**  
   Many dashboards show charts but do not explain what the data means or how different signals combine into a broader regime.

This dashboard solves that by turning raw market data into a simple macro regime classification and an AI-generated professional market brief.

---

## 🎯 Target Users

This product could be valuable for:

- Retail investors who want a simple macro overview before making investment decisions
- Financial analysts who need a quick daily market snapshot
- Wealth management teams preparing client commentary
- Fintech platforms that want to add AI-powered market intelligence
- Business strategy teams monitoring market risk
- Portfolio builders looking for macro context before asset allocation

---

## 🧠 Market Value / Differentiation

Unlike a basic financial dashboard, this project does not just display charts.

It combines:

- **Live financial data**
- **Rule-based macro regime detection**
- **AI-generated interpretation**
- **Clear visual market trends**
- **Decision-support language for non-specialist users**

This makes it closer to a lightweight **AI macro intelligence assistant** than a simple price tracker.

The key differentiator is that the dashboard translates data into business meaning:

> “What is happening in the market, what regime are we in, and what does that imply?”

---

## 📊 Key Features

### 1. Live Macro Data Collection

The app pulls six months of daily market data using `yfinance`.

Tracked indicators:

| Indicator | Ticker | Why It Matters |
|---|---:|---|
| S&P 500 | `^GSPC` | Measures broad US equity market performance |
| Crude Oil | `CL=F` | Tracks energy prices and inflation pressure |
| Gold | `GC=F` | Often reflects safe-haven demand and inflation hedging |
| VIX | `^VIX` | Measures equity market volatility and fear |
| US 10-Year Yield | `^TNX` | Reflects bond market expectations, rates, and growth/inflation outlook |

---

### 2. Current Macro Snapshot

The dashboard shows the latest value of each indicator and its 30-day percentage change.

This gives users a fast overview of:

- Equity market direction
- Volatility level
- Commodity pressure
- Safe-haven demand
- Interest rate environment

---

### 3. Six-Month Trend Visualisation

Each macro indicator is plotted as an interactive six-month line chart using Plotly.

This allows users to quickly see whether an indicator is:

- Trending upward
- Trending downward
- Volatile
- Stable
- Breaking into a new regime

---

### 4. Market Regime Classification

The app uses simple, explainable macro rules to classify the current market environment.

Example regime logic:

- **Risk-Off**: VIX above 30  
- **Risk-On**: VIX below 15 and S&P 500 rising  
- **Stagflation Risk**: Crude oil above 90 and VIX elevated  
- **Neutral / Transitional**: Mixed signals across indicators  

This gives recruiters and technical reviewers a clear example of applied business logic rather than only data visualisation.

---

### 5. AI Macro Brief

The dashboard uses NVIDIA’s hosted LLM endpoint through the OpenAI-compatible API structure.

When the user clicks **Generate Macro Brief**, the app sends the latest macro data to the model and asks it to produce a professional analyst-style explanation.

The AI brief covers:

- S&P 500
- VIX
- Gold
- Crude Oil
- US 10-Year Yield
- Current market regime
- Combined macro outlook

This demonstrates practical use of generative AI for business-facing financial analysis.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application framework |
| yfinance | Financial market data retrieval |
| pandas | Data processing and transformation |
| Plotly Express | Interactive data visualisation |
| OpenAI SDK | API client structure |
| NVIDIA NIM API | AI macro brief generation |

---

## 🧩 Architecture Overview

```text
User opens Streamlit app
        ↓
App fetches macro data from Yahoo Finance
        ↓
Data is cleaned and stored in a pandas DataFrame
        ↓
Dashboard displays latest values and 30-day changes
        ↓
Plotly charts show six-month indicator trends
        ↓
Rule-based logic classifies the market regime
        ↓
User clicks “Generate Macro Brief”
        ↓
NVIDIA-hosted LLM generates professional macro commentary
        ↓
Dashboard displays AI-generated market outlook
```

---

## 📈 Example Use Case

A wealth management analyst wants to prepare a quick morning market note.

Instead of checking several platforms separately, they open the dashboard and immediately see:

- Whether equities are rising or falling
- Whether volatility is elevated
- Whether oil prices are signalling inflation pressure
- Whether gold is acting as a safe-haven asset
- Whether bond yields are moving meaningfully
- What overall macro regime the market is currently in

They can then generate an AI macro brief to support internal commentary or client-facing analysis.

---

## 🧪 Skills Demonstrated

This project demonstrates:

- Financial data collection from public APIs
- Time-series data handling
- Streamlit dashboard development
- Interactive charting with Plotly
- Macro indicator interpretation
- Rule-based decision logic
- Generative AI integration
- Prompt engineering for financial analysis
- Business problem framing
- AI-assisted decision support
- Building recruiter-friendly fintech portfolio projects

---


## 🧠 Future Improvements

This project can be extended into a stronger fintech product by adding:

- More macro indicators such as CPI, unemployment, dollar index, Fed funds rate, and credit spreads
- Historical regime backtesting
- Asset allocation suggestions based on market regime
- Portfolio risk scoring
- User-uploaded portfolio analysis
- Daily automated macro reports
- Email or Slack alerts
- Database storage for historical snapshots
- More advanced regime classification using machine learning
- Comparison between AI-generated commentary and rule-based signals
- Deployment on Streamlit Cloud, Hugging Face Spaces, or AWS

---

## 🏦 Commercial Potential

This could evolve into a lightweight SaaS tool for:

- Independent investors
- Financial educators
- Small advisory firms
- Fintech newsletters
- Trading communities
- Portfolio risk teams

Possible monetisation routes:

1. **Freemium dashboard**  
   Free macro snapshot with paid premium insights.

2. **AI market brief subscription**  
   Daily or weekly AI-generated macro summaries.

3. **Portfolio overlay tool**  
   Users upload portfolio holdings and receive macro risk exposure insights.

4. **B2B fintech widget**  
   Embed the macro regime engine into financial platforms.

---


## 📌 Project Status

Current version: **Prototype / MVP**

The core functionality is complete:

- Live data fetching
- Macro snapshot
- Interactive trend charts
- Market regime classification
- AI-generated macro brief

Next step: improve robustness, add more indicators, secure API handling, and deploy publicly.

---

## 👤 Author

Built as part of an AI and data portfolio focused on practical business intelligence, fintech analytics, and generative AI-powered decision-support systems.
