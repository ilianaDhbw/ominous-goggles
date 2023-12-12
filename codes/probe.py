start_price = 4.80
km = int(input("Bitte Kilometer eingeben: "))
if km > 5:
    costs = 1.8
else: 
    costs=2.1

total=start_price + costs * km

print("Deine Kosten sind:",total )