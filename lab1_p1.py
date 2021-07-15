#Warren Green
#006314031

#this program takes the user's name and age and with that calculates
#what year they were born in.


from datetime import date

name = input("please enter your name: ")
age = int(input ("please enter your age: "))
today = date.today()
print ("Your name is ", name, "and you were born in", today.year - age)
