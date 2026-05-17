import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from openai import OpenAI

st.set_page_config(page_title="Macro Regime Dashboard", layout="wide", page_icon="🌍")
st.title("🌍 Macro Regime Dashboard")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

# Fetch macro data
@st.cache_data(ttl=3600)
def get_macro_data():
    tickers = {
        "S&P 500": "^GSPC",
        "Crude Oil": "CL=F",
        "Gold": "GC=F",
        "VIX": "^VIX",
        "US 10Y Yield": "^TNX"
    }
    data = {}
    for name, ticker in tickers.items():
        df = yf.download(ticker, period="6mo", interval="1d", progress=False)
        if not df.empty:
            close = df["Close"].squeeze()
            if isinstance(close, pd.Series):
                data[name] = close
    if data:
        result = pd.DataFrame(data)
        result.index = pd.to_datetime(result.index)
        return result
    return pd.DataFrame()

with st.spinner("Fetching macro data..."):
    df = get_macro_data()

if df.empty:
    st.error("Could not fetch data. Try again.")
else:
    latest = df.iloc[-1]
    prev = df.iloc[-30]

    st.subheader("Current Macro Snapshot")
    cols = st.columns(len(latest))
    for i, (name, val) in enumerate(latest.items()):
        change = ((val - prev[name]) / prev[name]) * 100
        cols[i].metric(name, f"{val:.2f}", f"{change:.1f}% (30d)")

    st.subheader("6-Month Trends")
    for col in df.columns:
        fig = px.line(df, y=col, title=col)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("📊 Market Regime")
    vix = latest.get("VIX", 20)
    sp_change = ((latest["S&P 500"] - prev["S&P 500"]) / prev["S&P 500"]) * 100

    if vix > 30:
        regime = "🔴 Risk-Off — High volatility. Defensive positioning suggested."
    elif vix < 15 and sp_change > 0:
        regime = "🟢 Risk-On — Low volatility, equities rising. Growth environment."
    elif latest.get("Crude Oil", 70) > 90 and vix > 20:
        regime = "🟡 Stagflation Risk — High oil + elevated volatility."
    else:
        regime = "🟠 Neutral / Transitional — Mixed signals across indicators."

    st.info(regime)

    st.subheader("🤖 AI Macro Brief")
    if st.button("Generate Macro Brief"):
        gold_change = ((latest['Gold'] - prev['Gold']) / prev['Gold'] * 100)
        oil_val = latest.get('Crude Oil', 'N/A')
        yield_val = latest.get('US 10Y Yield', 'N/A')

        summary = f"""
        Analyze each of these macro indicators individually and then give an overall outlook:

        1. S&P 500: {latest['S&P 500']:.2f}, 30-day change: {sp_change:.1f}%
        2. VIX (Volatility Index): {vix:.1f}
        3. Gold: {latest['Gold']:.2f}, 30-day change: {gold_change:.1f}%
        4. Crude Oil: {oil_val}
        5. US 10-Year Yield: {yield_val}
        6. Current Market Regime: {regime}

        For each indicator, explain what the current level means for markets.
        Then give a combined one-paragraph outlook.
        """

        with st.spinner("Generating brief..."):
            response = client.chat.completions.create(
                model="nvidia/nemotron-mini-4b-instruct",
                messages=[
                    {"role": "system", "content": "You are a senior macro analyst. Be specific, concise and professional. Always address each indicator separately before giving an overall view."},
                    {"role": "user", "content": summary}
                ],
                max_tokens=600
            )
            st.write(response.choices[0].message.content)