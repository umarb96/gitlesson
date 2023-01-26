#Challenge 5
#Create a variable called time, 
# A variable called place_of_work
# A variable called town_of_home
# Create an if statement that prints where someone is at times of the day. 
#For example if it is 7 I’m at home , 
# if it is 8 I’m commuting or if it is 9 I am at work

time = 8
place_of_work = "Manchester"
town_of_home = "Wilmslow"
if time in range(9,17):
    print(place_of_work)
elif time in range (18,24) or time in range(0):
    print(town_of_home)
else:
    print("I'm commuting")