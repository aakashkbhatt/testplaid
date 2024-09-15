import testplaid

with open("merchants.txt", "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Perform an operation on each line
        print(line.strip())  # strip() removes extra newline characters
        merchant_name = line.strip()

        client_id = ""
        secret = ""
        account_type = "credit"
        transactions = [
            {
                "id": "1",
                "description": merchant_name,
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
        response_data = callplaid.enrich_transactions(client_id, secret, account_type, transactions)
        print(response_data)
