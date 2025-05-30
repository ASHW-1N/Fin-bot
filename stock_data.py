import yfinance as yf

def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = info.get("currentPrice", None)

        if price:
            return f"📊 The current price of **{ticker}** is **${price}**."
        else:
            return f"Couldn't find current price for {ticker}."

    except Exception as e:
        return f"❌ Error retrieving stock data: {e}"
