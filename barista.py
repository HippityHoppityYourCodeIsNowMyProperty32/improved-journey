print("Welcome to the coffee shop")
name = input("What is your name? ")
menu = ["Black coffee", "Frappuccino","Flat White","Latte","Americano"]
print("Hello,here is our menu " + name)
print(menu)
order = input("What would you like to drink "+ name + "? ").lower()

if order == "black coffee":
    print("Good choice, that will be £2.50")
elif order == "frappuccino":
    print("Good choice, that will be £4.50")
elif order == "flat white":
    print("Good choice, that will be £2.80")
elif order == "latte":
    print("Good choice, that will be £2.75")
elif order == "americano":
    print("Good choice, that will be £2.50")
else:
    print("Sorry, we don't sell that here")