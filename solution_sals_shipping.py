"""
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers.
Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Ground Shipping Premium

Flat charge: $125.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Write a shipping.py Python program that asks the user for the weight of their package and
then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.
"""
# Initialize variables
weight = 41.5
flat_charge_gnd_shipping = 20
flat_charge_drone_shipping = 0
cost = 0

# Ground Shipping
if weight > 10:
    cost = weight * 4.75 + flat_charge_gnd_shipping
    print(f"Cost of ground shipping of {weight} lb is ${cost}")
elif weight > 6:
    cost = weight * 4.00 + flat_charge_gnd_shipping
    print(f"Cost of ground shipping of {weight} lb is ${cost}")
elif weight > 2:
    cost = weight * 3.00 + flat_charge_gnd_shipping
    print(f"Cost of ground shipping of {weight} lb is ${cost}")
else:
    cost = weight * 1.50 + flat_charge_gnd_shipping
    print(f"Cost of ground shipping of {weight} lb is ${cost}")

premium_gnd_shipping = 125.00

print("Premium ground shipping is " + "$" + str(premium_gnd_shipping))

# Drone Shipping
if weight > 10:
    cost = weight * 14.25 + flat_charge_drone_shipping
    print(f"Cost of drone shipping of {weight} lb is ${cost}")
elif weight > 6:
    cost = weight * 12.00 + flat_charge_drone_shipping
    print(f"Cost of drone shipping of {weight} lb is ${cost}")
elif weight > 2:
    cost = weight * 9.00 + flat_charge_drone_shipping
    print(f"Cost of drone shipping of {weight} lb is ${cost}")
else:
    cost = weight * 4.50 + flat_charge_drone_shipping
    print(f"Cost of drone shipping of {weight} lb is ${cost}")
