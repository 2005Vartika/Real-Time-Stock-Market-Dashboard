import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Title
st.title("📈 Real-Time Stock Market Dashboard")
st.write("Track live stock prices and historical trends.")

# Sidebar for user input
st.sidebar.header("Select Stock & Time Period")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)", "AAPL")
period = st.sidebar.selectbox("Select Period", ["1d","5d","1mo","6mo","1y","5y","max"])

# Fetch stock data
data = yf.Ticker(ticker_symbol)
df = data.history(period=period)

# Check if data is available
if df.empty:
    st.error("No data found. Please check the ticker symbol.")
else:
    # Display latest price
    latest_price = df['Close'][-1]
    st.subheader(f"Latest Closing Price for {ticker_symbol}: ${latest_price:.2f}")

    # Plot historical closing price
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'))
    fig.update_layout(title=f"{ticker_symbol} Historical Closing Price", xaxis_title="Date", yaxis_title="Price ($)")
    st.plotly_chart(fig)

    # Show data table
    st.subheader("Historical Data")
    st.dataframe(df.tail(10))

