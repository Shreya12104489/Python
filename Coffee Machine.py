MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


money=0
user_choice=0
drink=0


def check_resources():
  if resources["water"]<drink["ingredients"]["water"]:
    print("Sorry there is not enough water.")
    choice()
  elif resources["milk"]<drink["ingredients"]["milk"]:
    print("Sorry there is not enough milk.")
    choice()
  elif resources["coffee"]<drink["ingredients"]["coffee"]:
    print("Sorry there is not enough coffee.")
    choice()
  else:
    coins()

  
def update_resources():
  global resources, drink
  resources["water"] -= drink["ingredients"]["water"]
  resources["milk"] -= drink["ingredients"]["milk"]
  resources["coffee"] -= drink["ingredients"]["coffee"]
  choice()

  
def coins():
  global money, drink, user_choice
  coffee='''☕'''
  print("Please insert coins.")
  quarters = int(input("how many quarters?: "))
  dimes = int(input("how many dimes?: "))
  nickles = int(input("how many nickles?: "))
  pennies = int(input("how many pennies?: "))
  total_money = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
  cost = drink["cost"]
  if cost>total_money:
    print("Sorry that's not enough money. Money refunded")
    choice()
  else:
    money += cost
    refund = round((total_money - cost), 2)
    print(f"Here is ${refund} in change.")
    print(f"Here is your {user_choice} {coffee}. Enjoy!")
    update_resources()


def choice():
  global resources, money, MENU, drink, user_choice
  user_choice=input("What would you like? (espresso/latte/cappuccino): ")
  if user_choice == "off":
    return 0
  elif user_choice == "report":
    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}')
    choice()
  else:
    drink=MENU[user_choice]
    check_resources()


choice()



