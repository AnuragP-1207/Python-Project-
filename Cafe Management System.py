menu = {
    "pizza":40,
    "pasta":100,
    "Burger":120,
    "Salad":88,
    "Coffee":97
    }

print("welcome to python Restaurant")
print("Pizza: $40\nPasta: $100\nBurger: $120\nSalad: $88\nCoffee: $97 ")

total_order = 0

item_1 = input("Enter the name of Item you Want to Order = ")
if item_1 in menu:
    total_order += menu[item_1]
    print("Ordered item has been added to your order", item_1)
else:
    print("This item is not Yet")

another_order = input("Do you want to add another item (Yes | No)")
if another_order == "Yes":
    item_2 = input("Enter the name of Item you Want to Order = ")
    if item_2 in menu:
        total_order += menu[item_2]
        print("Ordered item  has been added to your order", item_2)
    else:
        print("This item is not Yet")


print("The total amount of items to pay is ", total_order)
