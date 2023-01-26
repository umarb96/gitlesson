
my_list = ["red", "green","yellow"]


print(my_list)


#activity

fav_footballers=["Ronaldo", "Rooney", "Zidane"]
print(fav_footballers)

#Loop

coffee_order = ["americano", "cortado", "espresso", "cappuccino"]

for i in coffee_order:
    print(i)
    
for i in range(10):
    print(i)

num = 0
while num <10 :
    num = num + 1
    print(num)

#Activity 1

#Create a list of 4 favourite countries to visit.
#Use a for loop to show each country in the list.
#Create a function called country_check() that checks 
#if the 3rd country in the list is Spain.
#If it is print  “Yaaay Spain is 3rd in your list of fave countries”. 
#If it isn’t print “Boo, I can’t believe Spain isn’t your 3rd fave country!” 

fav_countries = ["Spain", "USA", "Brazil", "Morocco"]
for i in fav_countries:
    print(i)

    def country_check():
        if fav_countries[2] == "Brazil":
            print ("Yaay Brazil is 3rd in your list of fav counrtires")
        else:
            print("Boo. I can't believe Brazil isn't your 3rd face country")

#Activity 2
#If you can create a for loop to output 0-9, 
#how can you create one to count backwards 9-0? 
#You will have to use your research skills to find out how to do this.  
 
for i in range(9, -1, -1):
    print(i)

#Activity 3
print("Umar")
for i in range(10):
    print(i)

#Activity 4
#Create a for loop that outputs “Hello World” 12 times. 
#Now convert this into a while loop that does the same thing.

for i in range(12):
    print ("hello world")
    print("")
i=0

while i < 12:
        print("hello world")
        i += 1

#Activity 5

#Create a variable, use a loop to generate 
# a random number between 1 and 30 six times. 
# For each random number generated, 
# check if this number is divisible by 7 or not.

import random 
for i in range (6):
    num = random.randint(1, 30)
    if num%7 == 0:
        print(f"{num} is divisible by 7")
else:
    print(f"(num) is NOT divisible by 7")

#activity

import random

cards = ["Diamonds","Heart", "Spades", "Club"]

my_card = "Heart"

current_card = random.choice(cards)

while current_card != my_card:
    print(current_card)
    current_card = random.choice(cards)

    print(f" You have foun")