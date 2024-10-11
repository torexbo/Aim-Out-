# payment.py
# Main script for processing bKash payments

import requests
from config import BKASH_MERCHANT_NUMBER, API_KEY, SECRET_KEY

def bkash_payment(amount, customer_number):
    url = "https://api.bkash.com/payment"
    
    payload = {
        "merchantNumber": BKASH_MERCHANT_NUMBER,
        "amount": amount,
        "customerNumber": customer_number,
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Secret-Key": SECRET_KEY,
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("Payment successful:", response.json())
    else:
        print("Payment failed:", response.text)

if __name__ == "__main__":
    amount = float(input("Enter the amount to pay: "))
    customer_number = input("Enter the customer's bKash number: ")
    bkash_payment(amount, customer_number)
