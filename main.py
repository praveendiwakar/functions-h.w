def greet_cutomer():
    print("Welcome to the art supplies shop!")
    print("Get all the art supplies here")

greet_cutomer()

price_per_item = float(input("enter the price per item:"))
items_bought = int(input("enter the number of items bought:"))

def calculate_total(price,items):
    total = price*items
    return total
total_cost = calculate_total(price_per_item, items_bought)

rounded_total = round(total_cost)
print("your total is", rounded_total)


amount_paid = int(input("enter the amount paid:"))

def calculate_change(paid,total):
    change = paid - total
    return change
change_due = calculate_change(amount_paid,rounded_total)
print("The change is:", change_due)

def thankyou_message(items):
    if items >= 5:
        print("Great choice, you icked many art supplies!")
    else:
        print("Thanks for shopping at the art supplies store")

closing_message = thankyou_message(items_bought)
print("")
print("--ART SUPPLIES BILL--")
print("prcice per item:", price_per_item)
print("items bought:", items_bought)
print("total cost:", total_cost)
print("amount paid:", amount_paid)
print("change due:", change_due)




