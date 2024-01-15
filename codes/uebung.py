import re

transactions=[
    {"type":"purchase","amount":50,"date":"2024-01-14"},
    {"type":"sale","amount":30.5,"date":"2024-01-15"}
]


transaction_type = transactions[0]["type"]
transaction_amount = transactions[0]["amount"]
transaction_date = transactions[0]["date"]


def sum_up(my_type):

    amount_values = [transaction["amount"] for transaction in transactions if transaction["type"]== my_type]
    return(sum(amount_values))

income = sum_up("purchase")
expenses =sum_up("sale")
print("income=", income)
print("expenses=",expenses)

if (income<expenses): print("You made money")
else: print("you lost money")

def find_all(my_key,my_value):
    values = [transaction for transaction in transactions if transaction[my_key]==my_value]
    return(values)


my_transactions = find_all("date","2024-01-14")
print(my_transactions)
print(len(my_transactions))