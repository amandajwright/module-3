# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:55:47 2018

@author: 612383423
"""
### Chapter 8: Mobile Data Bundle purchase program

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        answer=input('''
                     Login successful. What do you want to do today? 
                     Press 1 to view your credit balance
                     Press 2 to purchase data
                     Press 3 to top up your account.
                     
                         ''')
        if answer == '1': 
            return checkBalance(balance)
        elif answer =='2': 
            if checkNumber():
                return buyData(balance)
            else:
                print ('sorry, those numbers do not match.')
                return checkNumber()
        elif answer == '3':
            return topupBalance(balance)
        else:
            return 'wrong option selected'
    else: 
        return 'locked out after 3 attempts'
    
    
def passwordCheck(truePasscode): 
    counter = 0
    while counter < 3: # Never ending loop
      try:
        attempt = (input('Please enter your 4-digit password: '))
        if attempt == truePasscode:
            return True
        elif checkType(attempt):
            counter += 1
        elif checkLength(attempt, 4):
            counter += 1
        else:
            counter += 1
            raise EOFError
#      except TypeError:
#        print("numbers only please.")
#        continue # This causes it to continue  
      except EOFError:
        print("Please input something....")
        continue # This causes it to continue
    return False

def checkLength(answer, length):
    try:
        if len(answer)!= length:
            raise ValueError
    except ValueError:
        print("{} digits only.".format(length))
#        continue
        return True   
    return False

def checkType(answer):
    try:
        if not answer.isdigit():
            raise TypeError
    except TypeError:
        print("numbers only please.")
#        continue
        return True   
    return False

def checkBalance(balance):
    if balance > 0:
        return ( 'Your balance is £{}'.format(balance))
    else: 
        return ('Your balance is insufficient: £{}'.format(balance))
    
    
def checkNumber():
    phone_number = input('Please enter your phone number: ')
    confirm_number = input ('Thanks. Please enter your number again to confirm: ')
    if phone_number == confirm_number:
        return True
    else:
        return False
    
def buyData(balance):
    print('Thanks for confirming your number. Your current balance is £{}'.format(balance))
    print('\nAs you can only purchase in multiples of £5, the max you can spend is...')
    highest_price(balance)
    user_pays = (input('How much do you want to spend on data? multiples of £5 only, please : '))
    new_balance = float(balance)-float(user_pays)
    new_balance_2dp = round(new_balance, 2)
    if float(user_pays) > float(balance):
        return ('Sorry, you don\'t have enough money to purchase. Transaction cancelled.') 
    elif (int(user_pays)%5)!=0:
        return ('Sorry, the amount you requested is not a multiple of £5.Transaction cancelled.')
    else: 
        return ('Purchase successful! Your new balance is £{}'.format(new_balance_2dp))
        
def highest_price(balance):
    int_balance = int(balance)
    for i in range (int_balance-5,int_balance):
        if(i%5==0):
            max = i
            print ('£',max)
            return max
        
def topupBalance (balance):
    user_topup = (input('Your current balance is £{}. How much do you want to top up? multiples of £5 only, please : '.format(balance)))
    new_topup_balance = float(balance)+float(user_topup)
    new_topup_balance_2dp = round(new_topup_balance, 2)
    if (int(user_topup)%5)!=0:
        return ('Sorry, the amount you requested is not a multiple of £5.Transaction cancelled.')
    else: 
        return ('Thanks for topping up! Your new balance is £{}'.format(new_topup_balance_2dp))
            
#highest_price(62)