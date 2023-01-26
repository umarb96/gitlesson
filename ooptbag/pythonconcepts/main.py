from room import Room

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom =  Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")

dining_hall = Room("dining_room")
dining_hall.set_description("A large room with ornate golden decorations")



#kitchen.describe()

kitchen.link_room(dining_hall, "south")   
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

#dining_hall.get_details()

current_room = kitchen 

while True: 
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command) 



