#1
r = float(input("Input circle radius? "))
area = 3.14 * r * r
print("Circle area =", area)

#2
c = int(input("Input the temperature in Celsius?"))
f = (c * 9/5) + 32
print(f"{c} (C) = {f} (F)")

#3
n = int(input("Input a number? "))
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
if is_prime == True:
    print(f"{n} is a prime number")
else:
    print(f"{n} is a not prime number")

#4
n = int(input("Enter a number: "))
sum_divisors = 0
for i in range(1, n):
    if n % i == 0:
        sum_divisors = sum_divisors + i
if sum_divisors == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a not perfect number")

#5
color_list = ["Blue", "Yellow", "Red"]
user_color = input("What is your favorite color? ")
found = False
for i in range(len(color_list)):
    if color_list[i] == user_color:
        print(f"Your colod is at index {i} in my list")
        found = True
        break

if found == False:
    print("Sorry, I could not find your color")

#6
range1 = list(range(7))
print("range1", range1)

range2 = list(range(1, 11, 3))
print("range2", range2)

range3 = list(range(5, 0, -1))
print("range3", range3)

range4 = list(range(6, -3, -2))
print("range4", range4)

#7
def remove_dollar_sign(s):
    new_string = s.replace("$", "")
    return new_string

#8
def extract_even(l):
    even_list = []
    for num in l:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

#9
def calculate_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

#10
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

#11
import math

x1 = float(input("Input x1: "))
y1 = float(input("Input y1: "))

x2 = float(input("Input x2: "))
y2 = float(input("Input y2: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance =", distance)

#12
def print_pattern(m, n):
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print() 