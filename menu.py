menu = {"pizza":300,
        "burger":200,
        "popcorn":200,
        "fries":140,
        "chips":110,
        "coke":80,
        "water":50}
cart=[]
total=0

#Print the menu for user
for x,y in menu.items():
    print(f"{x:8}: Rs.{y:.2f}")

#Adding to cart printing total
while True:
    food = input("Select an item from menu(q to quit): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)
    print(food,end=" ")
print()
print(f"Total is Rs.{total:.2f}")