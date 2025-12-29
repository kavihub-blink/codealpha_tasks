#stock Portfolio Tracker

#Predefined stock prices(buil_in data)
stock_prices={"APPL":180,"TSLA":250,"GOOGL":140,"MSFT":320}
print("Welcome to StocK Portfolio Tracker")

total_investment=0

while True:
    stock_name=input("Enter stock name(or type 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    
    if stock_name not in stock_prices:
        print("Stock not available.")
        continue
    
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Please enter a valid number>")
        continue
    
    investment_value=stock_prices[stock_name]*quantity 
    total_investment +=investment_value
    
    print(f"Added {stock_name} | Quantity: {quantity} | Value:$ {investment_value}")
    print("\n Total Investment Value: $",total_investment)
    print("Thank you for using Stock Portfolio Tracker !")
    
    