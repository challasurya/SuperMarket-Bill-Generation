from datetime import datetime

# Input the customer's name
name = input("Enter your name: ")

# List of available items
list_items = '''
Rice_pr   Rs 60/kg
Rice_od   Rs 40/kg
Sugarpr   Rs 50/kg
Sugarod   Rs 30/kg
Chilli*   Rs 300/kg
Salt_pr   Rs 50/kg
Salt_od   Rs 30/kg
Oil_pre   Rs 600/lit
Oil_ord   Rs 300/lit
Milk_tp   Rs 100/lit
Paneer_   Rs 250/kg
Boost     Rs 5/each
Chocola   Rs 5/each
Biscuit   Rs 10/each
Maggi     Rs 10/each
Sauce     Rs 15/each
'''

# Initialize variables
price = 0
pricelist = []  # Stores tuples of (item, quantity, rate, price)
totalprice = 0
finalamount = 0
ilist = []  # Item names
qlist = []  # Quantities
plist = []  # Prices

# Dictionary for item rates
items = {
    "Rice_pr": 60,
    "Rice_od": 40,
    "Sugarpr": 50,
    "Sugarod": 30,
    "Chilli*": 300,
    "Salt_pr": 50,
    "Salt_od": 30,
    "Oil_pre": 600,
    "Oil_ord": 300,
    "Milk_tp": 100,
    "Paneer_": 250,
    "Boost": 5,
    "Chocola": 5,
    "Biscuit": 10,
    "Maggi": 10,
    "Sauce": 15
}

# Display items list if the user requests it
option = int(input("For the list of items, press 1: "))
if option == 1:
    print(list_items)

# Take user input for items and quantities
while True:
    inp1 = int(input("If you want to buy, press 1 or press 2 to exit: "))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your item: ")
        quantity = int(input("Enter quantity: "))
        if item in items.keys():
            price = quantity * items[item]
            pricelist.append((item, quantity, items[item], price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
        else:
            print("Sorry, the item you entered is not available.")
    else:
        print("Invalid input. Please enter 1 to buy or 2 to exit.")

# Calculate GST and final amount
gst = (totalprice * 5) / 100  # 5% GST
finalamount = gst + totalprice

# Generate the bill
bill = input("Proceed to bill the items? (yes or no): ").lower()
if bill == "yes":
    if finalamount != 0:
        print("=" * 25, "Vamsy Supermarket", "=" * 25)
        print(" " * 28, "Mandapeta")
        print("Name:", name, " " * 30, "Date:", datetime.now())
        print("-" * 75)
        print("SNo", " " * 10, "Items", " " * 10, "Quantity", " " * 10, "Price")
        for i in range(len(pricelist)):
            print(i + 1, " " * 10, ilist[i], " " * 10, qlist[i], " " * 16, plist[i])
        print("-" * 75)
        print(" " * 50, "Total Amount:", "Rs", totalprice)
        print("GST Amount:", " " * 50, "Rs", gst)
        print(" " * 50, "Final Amount:", "Rs", finalamount)
        print("=" * 75)
    else:
        print("No items were purchased.")
else:
    print("Thank you for visiting!")
