from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


while True:
	user_input = input(f"​What would you like?: {menu.get_items()}: ")
	if user_input == "off":
		break
	elif user_input == "report":
		coffee.report()
		money.report()
	else:
		drink_info = menu.find_drink(user_input)
		if drink_info:
			if coffee.is_resource_sufficient(drink_info):
				if money.make_payment(drink_info.cost):
					coffee.make_coffee(drink_info)