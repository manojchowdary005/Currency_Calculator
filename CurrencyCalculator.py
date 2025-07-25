import requests


# Function to get exchange rates from the API
def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/bfd566dc5d5ae43618152727/latest/{base_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['conversion_rates'].get(target_currency)

        if exchange_rate:
            return exchange_rate
        else:
            print(f"Error: Unable to find conversion rate for {target_currency}.")
            return None
    else:
        print(f"Error: {response.status_code}. Unable to fetch exchange rates.")
        return None


# Function to convert currency
def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        converted_amount = amount * exchange_rate
        return converted_amount
    return None


# User input for conversion
def main():
    print("Welcome to the Currency Converter!")
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()

    try:
        amount = float(input(f"Enter the amount in {base_currency}: "))
    except ValueError:
        print("Invalid input! Please enter a valid number for the amount.")
        return

    converted_amount = convert_currency(amount, base_currency, target_currency)

    if converted_amount:
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")


if __name__ == "__main__":
    main()
