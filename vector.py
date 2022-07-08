import cmath

print("Welcome to Vector, a 3-space vector calculator")
print("Vector can preform various operations on a maximum of three vectors")
print("-----------------------------------------------")

print("Input Vector 1 by each component")
a1 = int(input("A1: "))
b1 = int(input("B1: "))
c1 = int(input("C1: "))

v1 = [a1, b1, c1]
print("Vector 1:", v1)

print("-----------------------------------------------")

print("Input Vector 2 by each component")
a2 = int(input("A2: "))
b2 = int(input("B2: "))
c2 = int(input("C2: "))

v2 = [a2, b2, c2]
print("Vector 2:", v2)

print("-----------------------------------------------")

print ("Operations:")
print ("1 - Vector Dot Product")
print ("2 - Vector Addition")  
print ("3 - Vector Subtraction")
choice = int(input("Select operation you would like to preform: "))

print("-----------------------------------------------")

if choice == 1:
    print("Vector Dot Product")
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Vector Dot Product:", v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])
elif choice == 2:
    print("Vector Addition")
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Vector Addition:", v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2])
elif choice == 3:
    print("Vector Subtraction")
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Vector Subtraction:", v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2])
