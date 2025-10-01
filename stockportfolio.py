def stock_portfolio_tracker():
    # Hardcoded stock prices (USD)
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 320,
        "GOOGL": 140,
        "AMZN": 135
    }

    portfolio = {}
    total_value = 0

    print("\n=== Stock Portfolio Tracker ===")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Stock not available in price list.")
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        value = stock_prices[stock] * qty
        portfolio[stock] = portfolio.get(stock, 0) + qty
        total_value += value

        print(f"Added {qty} shares of {stock} worth ${value}")

    print("\n=== Portfolio Summary ===")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares (Value: ${qty * stock_prices[stock]})")
    print(f"\nTotal Investment Value: ${total_value}")

    save = input("\nDo you want to save this report to a file? (y/n): ").lower()
    if save == "y":
        with open("portfolio.txt", "w") as f:
            f.write("=== Portfolio Summary ===\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares (Value: ${qty * stock_prices[stock]})\n")
            f.write(f"\nTotal Investment Value: ${total_value}\n")
        print("✅ Report saved as 'portfolio.txt'.")

if __name__ == "__main__":
    stock_portfolio_tracker()
