import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/bfd566dc5d5ae43618152727/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        if target_currency in data['conversion_rates']:
            return data['conversion_rates'][target_currency]
        else:
            print("Invalid target currency.")

    else:
        print(f"Error: {data['error-type']}")


def convert_currency():
    print("Welcome to the Currency Converter!")

    base_currency = input("Enter the base currency (e.g., USD, EUR, GBP): ").upper()
    target_currency = input("Enter the target currency (e.g., USD, EUR, GBP): ").upper()
    try:
        amount = float(input(f"Enter the amount in {base_currency}: "))
    except ValueError:
        print("Please enter a valid number for the amount.")
        return

    rate = get_exchange_rate(base_currency, target_currency)

    if rate:
        converted_amount = amount * rate
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}.")
    else:
        print("Conversion failed. Please try again.")


if __name__ == "__main__":
    convert_currency()
