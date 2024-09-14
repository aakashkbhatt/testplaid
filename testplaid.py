import requests

def enrich_transactions(client_id, secret, account_type, transactions):
    url = "https://sandbox.plaid.com/transactions/enrich"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "client_id": client_id,
        "secret": secret,
        "account_type": account_type,
        "transactions": transactions
    }

    response = requests.post(url, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"


client_id = ""
secret = ""
account_type = "credit"
transactions = [
    {
        "id": "1",
        "description": "PURCHASE WM SUPERCENTER #1700",
        "amount": 72.10,
        "direction": "OUTFLOW",
        "iso_currency_code": "USD",
        "location": {
            "city": "Poway",
            "region": "CA"
        },
        "mcc": "5310",
        "date_posted": "2022-07-05"
    }
]

# Call the function
response_data = enrich_transactions(client_id, secret, account_type, transactions)
print(response_data)