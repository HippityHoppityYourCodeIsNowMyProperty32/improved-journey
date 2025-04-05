print("Welcome to the coffee shop!")

name = input("What is your name?\n")
menu= ["Cappuccino", "Black Coffee", "Espresso","Latte","Iced Latte","Iced Matcha" ]
print("Here is our menu: \n"+", ".join(menu))
order= input("What would you like to order today "+name+"? ")

if order=="Cappuccino" or "cappuccino":
 print ("That will be £3.50 then, "+name)

if order=="Black Coffee" or "Black coffee" or "black coffee" :
 print ("That will be £2.50 then, "+name)

if order=="Espresso" or "espresso":
 print ("That will be £2.00 then, "+name)

if order=="latte" or "Latte":
 print ("That will be £3.50 then, "+name)

if order=="Iced Latte" or "iced latte" or "Iced latte":
 print ("That will be £3.50 then, "+name)

if order=="Iced Matcha" or "Iced matcha" or "iced matcha" :
 print ("That will be £4.00 then, "+name)
 
