MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": [300, "ml"],
    "milk": [200, "ml"],
    "coffee": [100, "g"],
	"money": [0, "$"]
}

currency = {
	"quarters": 0.25,
	"dimes": 0.1,
	"nickles": 0.05,
	"pennies" : 0.01
}

def check_resources(resources, required) -> bool:
	for ingredient, amount in required["ingredients"].items():
			if resources[ingredient][0] - amount < 0:
				print(f"Sorry, there is not enough {ingredient}")
				return False
	return True

def calculate_change(cost):
	total_input = 0
	for coin_type, coin_value in currency.items():
		total_input += float(input(f"How many {coin_type}: ")) * coin_value
	return total_input-cost, total_input

while True:
	user_input = input("What would you like? (espresso, latte, cappuccino): ")

	if user_input == "off": break
	# output current resources
	if user_input == "report":
		print("\n".join(
			f"{resource.capitalize()}: {amount[0]}{amount[1]}" if amount[1]!= "$"
			else f"{resource.capitalize()}: {amount[1]}{amount[0]}"
			for resource, amount in resources.items()))
	# compute order and check for resources
	if user_input in MENU.keys():
		if check_resources(resources, MENU[user_input]):
			change, income = calculate_change(MENU[user_input]["cost"])
			if change < 0: print("Sorry that's not enough money. Money refunded.​")
			else:
				if change > 0:
					print(f"Here is ${change:.2f} dollars in change.")
				for ingredient, amount in MENU[user_input]["ingredients"].items():
					resources[ingredient][0] -= amount
				resources["money"][0] += income
				print(f"Here is your {user_input}. Enjoy!")
