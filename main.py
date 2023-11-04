import os
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
coins = {
  'quarters': 0.25,
  'dimes': 0.10,
  'nickles': 0.05,
  'penies': 0.01
}
power = 'on'
def coffee_machine():
  def user_choice():
    print(resources)
    print(f"Money: {money}")
    user_prompt = input("What would you like?' (espresso/latte/cappuccino)': ")
    if user_prompt == 'off':
      print('action has completed...')
      return 'off'  
    elif user_prompt == 'espresso':
      print('action has completed...')
      return 'espresso'
    elif user_prompt == 'latte':
      print('action has completed...')
      return 'latte'
    elif user_prompt == 'cappuccino':
      print('action has completed...')
      return 'cappuccino'  
    elif user_prompt == 'report':
      print('action has completed...')
      return 'report'
  u_c = user_choice()
  if u_c == 'off':
    def power(user_choice):
      if user_choice == 'off':
        print('Good bye!')
        exit(1)
    power(u_c)
  elif u_c == 'report':
    def report_resources(user_choice):
      if user_choice == 'report':
        print(resources)
        exit(1)
    report_resources(u_c)
  elif u_c == 'espresso' or u_c == 'latte' or u_c == 'cappuccino':
    def check_resources(u_c):
      if u_c == 'cappuccino' or u_c == 'latte':
        if MENU[u_c]['ingredients']['water'] <= resources['water'] and MENU[u_c]['ingredients']['coffee'] <= resources['coffee'] and MENU[u_c]['ingredients']['milk'] <= resources['milk']:
          print('action has completed...')          
          return 'status ok!'          
        else:          
          print('Sorry there is not enough resources...')          
          return 'status not enough resources'  
      elif u_c == 'espresso':  
        if MENU[u_c]['ingredients']['water'] <= resources['water'] and MENU[u_c]['ingredients']['coffee'] <= resources['coffee']:  
          print('action has completed...')  
          return 'status ok!'        
        else:  
         print('Sorry there is not enough resources...')
         return 'status not enough resources'  
  is_checked = check_resources(u_c)
  def process_coins(is_checked, u_c):
    global money
    if is_checked == 'status ok!':
      quarters = int(input('How many quarters: '))
      dimes = int(input('How many dimes: '))
      nickles = int(input('How many nickles: '))
      penies = int(input('How many penies: '))
 
      sum_of_coins = (coins['quarters'] * quarters) + (coins['dimes'] * dimes) + (coins['nickles'] * nickles) + (coins['penies'] * penies)
      if sum_of_coins == MENU[u_c]['cost']:
        money += sum_of_coins
        return 'transaction ok!'
      elif sum_of_coins < MENU[u_c]['cost']:
        print("Sorry thats not enough money. Money refunded")
        return 'transaction not ok!'
      elif sum_of_coins > MENU[u_c]['cost']:
        change = sum_of_coins - MENU[u_c]['cost']
        money += sum_of_coins - change
        print(f'Here is your change: {round(change, 2)}')
        return 'transaction ok!'
  process_coins_checked = process_coins(is_checked,u_c)
  def make_coffee(process_coins_checked):
    if process_coins_checked == 'transaction ok!':
      if u_c == 'espresso':
        water = resources['water'] - MENU[u_c]['ingredients']['water']
        resources['water'] = water
        coffee = resources['coffee'] - MENU[u_c]['ingredients']['coffee']
        resources['coffee'] = coffee
        print(resources)
        print(f"Money: {money}")
      if u_c == 'latte' or u_c == 'cappuccino':
        water = resources['water'] - MENU[u_c]['ingredients']['water']
        resources['water'] = water
        coffee = resources['coffee'] - MENU[u_c]['ingredients']['coffee']
        resources['coffee'] = coffee
        milk = resources['milk'] - MENU[u_c]['ingredients']['milk']
        resources['milk'] = milk
        print(resources)
        print(f"Money: {money}")
      return f"Here is your {u_c}. Enjoy!"
  coffee = make_coffee(process_coins_checked)
  print(coffee)
power = 'on'
while power == 'on':
  choice = input('Would you like to have a coffee? "yes" or "no"\n')
  if choice == 'yes':
    os.system('clear')
    coffee_machine()
  if choice == 'no':
    break
  if power == 'off':
    break 