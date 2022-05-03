type = {
    'espresso': {'water': 50, 'coffee': 18, 'milk': 0, 'price': 1.50},
    'cappuccino': {'water': 200, 'coffee': 24, 'milk': 100, 'price': 2.50},
    'latte': {'water': 200, 'coffee': 24, 'milk': 150, 'price': 3.00}
}

machine_resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}


def report():
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"Coffee: {machine_resources['coffee']}g")
    print(f"Money: ${round(machine_resources['money'], 2)}")


def check_resource(coffee):
    # resources = list(machine_resources)
    # coffee_require = list(type[coffee])
    # for i in resources:
    #     if coffee_require[i] < machine_resources[i]:
    #         print(f"Sorry there is not enough {i}")
    #         return False
    if coffee['water'] > machine_resources['water']:
        print(f"Sorry there is not enough water")
        return False
    elif coffee['milk'] > machine_resources['milk']:
        print(f"Sorry there is not enough milk")
        return False
    elif coffee['coffee'] > machine_resources['coffee']:
        print(f"Sorry there is not enough coffee")
        return False
    return True


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dime = int(input("How many dime?: "))
    nickel = int(input("How many nickel?: "))
    penny = int(input("How many penny?: "))

    total = quarters * money['quarter'] + dime * money['dime'] + nickel * money['nickel'] + penny * money['penny']
    return round(total, 2)


def enough_coin(coffee, coin):
    if type[coffee]['price'] > coin:
        print("Sorry, that's not enough money. Money refunded")
        return False
    else:
        machine_resources['money'] += coin
        coin -= type[coffee]['price']

        machine_resources['water'] -= type[coffee]['water']
        machine_resources['milk'] -= type[coffee]['milk']
        machine_resources['coffee'] -= type[coffee]['coffee']

        print(f"Here is ${round(coin, 2)} in change")
        print(f"Here is your {coffee} . Thank you")
        return True


money = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25
}

is_on = True
while is_on:
    coffee_choice = input("What would you like? (espresso/cappuccino/latte)? ").lower()

    if coffee_choice == 'report':
        report()
    elif coffee_choice == 'off':
        print("Turning off machine...")
        is_on = False
    elif coffee_choice == 'espresso' or coffee_choice == 'cappuccino' or coffee_choice == 'latte':
        coffee_chosen = type[coffee_choice]
        if not check_resource(coffee_chosen):
            continue
        coins = insert_coins()
        if not enough_coin(coffee_choice, coins):
            continue
    else:
        print("Invalid choice. Please try again")


