class Stock:

    def __init__(self, name, price):
        self.name = name
        self.price = price


reliance = Stock("RELIANCE", 1450)

print(reliance.name)
print(reliance.price)