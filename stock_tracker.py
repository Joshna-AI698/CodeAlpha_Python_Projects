stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 150, "MSFT": 420, "AMZN": 190}
portfolio = []
grand_total = 0

print("=" * 40)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")
for stock in stock_prices:
    print(stock, "  -$", stock_prices[stock])

while True:
    stock_name = input("\n Enter stock name(or 'Done' to finish): ")
    if stock_name == "Done":
        break
    if stock_name not in stock_prices:
        print("Stock not found! please choose from available stock.")
        continue
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number for quantity.")
        continue
    price = stock_prices[stock_name]
    total_investment = price * quantity
    grand_total = grand_total + total_investment

    portfolio.append(
        {
            "stock": stock_name,
            "price": price,
            "quantity": quantity,
            "total": total_investment,
        }
    )
    print("Added successfully!!")
    print("Investment for", stock_name, ":", total_investment)

print("\n" + "=" * 40)
print("         PORTFOLIO SUMMARY")
print("=" * 40)

if len(portfolio) == 0:
    print("No stocks were added.")
else:
    for item in portfolio:
        print(
            item["stock"],
            "| Price:",
            item["price"],
            "| Quantity:",
            item["quantity"],
            "|Total:",
            item["total"],
        )
    print("-" * 40)
    print("GRAND TOTAL INVESTEMENT:", grand_total)
    with open("portfolio_summary.txt", "w") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 30 + "\n")
        for item in portfolio:
            file.write(
                f"{item['stock']} | Price:{item['price']} |"
                f"Quantity: {item['quantity']} | Total: {item['total']}\n"
            )
        file.write("=" * 30 + "\n")
        file.write(f"Grand Total Investment: {grand_total}\n")
    print("\nSummary saved to portfolio_summary.txt")

print("\nThank you for using Stock Portfolio Tracker!")
