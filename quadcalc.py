import math
from time import sleep

#Initial title block and instructions
print("Welcome to the Quadratic Equation Calculator, Monkey Edition")
print("Please enter the parameters of your quadratic equation")
print("-----------------------------------------------")

#Input parameters
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

#Determine if the equation is quadratic and calculate the discriminant
if a == 0:
    print("Enter a quadratic equation you trained monkey!")
    input("Press Enter to exit")
    exit()
else: 
    D = int(b**2 - 4*a*c)

print("Calculating")
sleep(1)

#Determine the number of solutions, if no solutions, print error message
if D == 0:
    D1 = (-b/(2*a))
    print("The solution is", D1)
elif D > 0:
    S1 = (-b+math.sqrt(D))/(2*a)
    S2 = (-b-math.sqrt(D))/(2*a)
    e = int(input("There are solutions, how many decimal places do you want to round to? "))
    S11 = round(S1, e)
    S22 = round(S2, e)
    print("The solutions are,", S11, "and", S22)
else:
    print("No real solutions since D =", D, ". Sorry man.")

input("Press Enter to exit")