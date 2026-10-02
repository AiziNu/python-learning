from menu import resources, MENU

profit = 0
def main():
    is_coffee_on = True
    print("Welcome to the Coffee Maker!")

    while is_coffee_on:
        choise = input("What would you like? (espresso/latte/cappuccino): ")
        if choise == "off":
            is_coffee_on = False
        elif choise == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[choise]
            if is_reasourses_available(drink['ingredients']):
                payment = calculate_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(choise, drink['ingredients'])


def is_reasourses_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]  > resources[item]:
            print("Sorry, you don't have enough resources to buy this coffee")
            return False
    return True

def calculate_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = drink_cost - money_received
        print(f"Here is your change: {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, you don't have enough money to buy this coffee. Money reterned")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

main()