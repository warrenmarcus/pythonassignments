#Warren Green
#006314031

#takes user input
x = int(input("enter a number:"))
i = x
print("list of divisors")

# This loop calculates the divisors of whatever number is chosen
while i>0:
    if x%i ==0:
        print (i)
        i -=1
    else:
        i -=1