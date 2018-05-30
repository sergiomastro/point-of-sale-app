#shopping_cart.py
#Sergio Mastrogiovanni

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017



import datetime

checkout_start_at = datetime.datetime.now()
product_ids=[]

#user enters data

while True:
    product_id = (input("Welcome! Please enter a product identifier. Enter DONE when finished: "))
    while True:
        try:
            product_id = int(product_id)
            break
        except ValueError:
            if product_id=="DONE":
                break
            print("Invalid Entry. Please try again:")
            product_id = (input("Welcome! Please enter a product identifier. Enter DONE when finished: "))
    if product_id=="DONE":
        break
    elif int(product_id)>0 and int(product_id)<21:
        product_ids.append(product_id)
    else:
        print("Please enter a product from 1-20:")




print("--------------------")
print("SERGIO'S GROCERY")
print("--------------------")
print("Phone Number: 555-555-5555")
print("Website: nyu.edu/grocery")
print("Checkout Date and Time: "+ str(checkout_start_at.strftime("%A, %B %d, %Y at %I:%M%p"))) #from datetime
print()

print("Shopping Cart Items:")

def matching_product(product_identifier):
    products_list = [p for p in products if p["id"] == product_identifier] #list of items in products
    return products_list[0]

raw_total = 0
print("PURCHASE ITEMS")
for pid in product_ids:
    product = matching_product(int(pid))
    raw_total = raw_total + product["price"] # could use raw_total += product["id"]
    price_usd = "(${0:.2f})".format(product["price"])
    print("++" + product["name"] + price_usd)

raw_total_price = "(${0:.2f})".format(raw_total)
tax_amount = "(${0:.2f})".format(raw_total*.08875)
total_price = "(${0:.2f})".format(raw_total*1.08875)
print("--------------------")
print("Subtotal: "+ raw_total_price)
print("Tax: "+tax_amount)
print("Total: "+total_price)
print()
print("--------------------")
print("Thanks for shopping with us!")
print("--------------------")

