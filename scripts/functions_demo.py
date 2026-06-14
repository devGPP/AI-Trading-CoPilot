watchlist = ["RELIANCE", "TCS", "INFY"]

def scan_stock(stock):
    print("Scanning", stock)

for stock in watchlist:
    scan_stock(stock)
    print("No Breakout found for", stock)