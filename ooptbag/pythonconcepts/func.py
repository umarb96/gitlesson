#Activity 1
#Create a function that takes two parameters for 
# name and age, and outputs a Birthday message 
# “ Happy Birthday ‘name’ I hear you are ‘age’ today!”



def birthday_greeting(name,age):
    print(f"Happy birthday {name} I hear you are {age} today!")
   
birthday_greeting("Sarah", "20")

#Create a function that takes two parameters: 
# size and type of drink, and 
# then outputs the drinks order. 

def drink_order (size, type):
    print(f" you have ordered a {size} {type}")
drink_order("large", "Coca cola")

#Activity 2
#Here is a function that takes a parameter. 
#Parameters are responsible for functions to be able to work on different data inputs. 
#Edit the code below to include two more parameters and 
#a running order count when the function is called.


order_count = 0

def take_order(topping, topping2, topping3):
     global order_count
     print(f"Pizza with {topping}, {topping2}, {topping3}")
     order_count += 1
     print(f"order numer: {order_count}")
     
     take_order("sweetcorn" , "olives", "onions")
     take_order("sweetcorn", "olives", "onions")
     take_order("sweetcorn", "olives", "onions")



#Create a cash machine program that takes a pin number and amount. 
#Outputs cash is being dispensed 
#if the pin is correct and there is enough money to withdraw. 
#Finally outputs the new balance

if 

actual_pin - 