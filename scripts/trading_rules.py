capital = 100000
risk_per_trade = 1000
market_open = False

if market_open and risk_per_trade <= 1000:
    print("Trade allowed")
else:
    print("Trade rejected")