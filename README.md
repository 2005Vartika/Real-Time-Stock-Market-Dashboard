# 📈 Real-Time Stock Market Dashboard

## **Project Overview**
A web-based dashboard to track and visualize real-time stock market data. Users can view live stock prices, historical trends, and recent price data interactively.

**Technologies Used:**
- Python
- Streamlit (Web dashboard)
- Pandas (Data handling)
- Plotly (Interactive charts)
- yfinance (Fetch stock data)

**Outcome:**
- Real-time stock price tracking
- Historical price charts
- Simple, interactive web dashboard

---

## **Features**
- Enter any stock ticker (e.g., AAPL, TSLA) to track its performance.
- View latest closing price.
- Interactive historical price chart for selected time periods (1d, 5d, 1mo, 6mo, 1y, 5y, max).
- Table view of recent stock data.

---

## **Setup Instructions**

### 1. Create a virtual environment (optional but recommended)
```bash
python -m venv stock_env
```

### 2. Activate the virtual environment
```bash
# Windows
stock_env\Scripts\activate

# macOS/Linux
source stock_env/bin/activate
```
### **3. Install dependencies**
```bash
pip install -r requirements.txt

# Or, if requirements.txt is not available:
pip install streamlit pandas plotly yfinance
```
### **4. Run the dashboard**
```bash
streamlit run app.py
