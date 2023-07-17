#import another_module
#print(another_module.another_variable)

from turtle import Turtle,Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(300)

#my_screen = Screen()
#print(my_screen.canvheight)
#print(my_screen.canvwidth)
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pickachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)

class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        print("The user  being created")


user_1 = User("001", "nata")
user_2 = User("002", "jack")

print(user_2.username)