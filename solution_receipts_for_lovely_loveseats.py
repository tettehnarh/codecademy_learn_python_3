"""
We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.

In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.
"""

# Lovely love seat product description
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""

# Lovely love seat product price
lovely_loveseat_price = 254.00

# Stylish sette product description
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

# Stylish sette product price
stylish_settee_price = 180.50

# Luxurious lamp product description
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

# Luxurious lamp product price
luxurious_lamp_price = 52.15

# Sales tax component
sales_tax = 0.088

# Customer one cart details

# Initialize total cost of products
customer_one_total = 0

# Initialize product description
customer_one_itemization = ""

# Customer one purchases lovely loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Customer one purchases luxurious lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization = customer_one_itemization + \
    "\n" + luxurious_lamp_description

# Customer one checkout process

# Calculate first customer tax
customer_one_tax = customer_one_total * sales_tax

# Add tax to customer one total
customer_one_total += customer_one_tax

# Print out receipt for first customer
print("Customer One Items:")
print("--------------------")
print(customer_one_itemization)
print("--------------------")
print("Customer One Total:")
print(round(customer_one_total, 3))
