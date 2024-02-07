
# ⭐️⭐️⭐️ Casting ⭐️⭐️⭐️
# Casting is converting one data type to another in programming.

# ⭐️ int to float
int_num = 5
print("int_num: ", int_num)    # int 5
float_num = float(int_num)
print("float_num: ", float_num)    # float 5.0
print("--"*20)

# ⭐️ float to int
float_num = 5.0
print("float_num: ", float_num)    # float 5.0
int_num = int(float_num)
print("int_num: ", int_num)    # int 5
print("--"*20)

# ⭐️ int to str
int_num = 5
print("int_num: ", int_num)    # int 5
str_num = str(int_num)
print("str_num: ", str_num)    # str 5
print("--"*20)

# ⭐️ str to int
str_num = "5"
print("str_num: ", str_num)    # str 5
int_num = int(str_num)
print("int_num: ", int_num)    # int 5

str_num = "manish"
print("str_num: ", str_num)    # str manish
# int_num = int(str_num)
# print("int_num: ", int_num)   # ValueError: invalid literal for int() with base 10: 'manish'
print("--"*20)

# ⭐️ str to float
str_num = "5"
print("str_num: ", str_num)    # str 5
float_num = float(str_num)
print("float_num: ", float_num)    # float 5.0
print("--"*20)

# ⭐️ str to list
str_num = "manish"
print("str_num: ", str_num)    # str manish
list_num = list(str_num)
print("list_num: ", list_num)    # list ['m', 'a', 'n', 'i', 's', 'h']
print("--"*20)

# ⭐️⭐️⭐️ Operators ⭐️⭐️⭐️
# Operator vanako kura lai operate garna ko lagi use garinxa.
x = 5
# ya x vanako variable ho = vanako assignment operator ho 5 vanako value ho

# 1. Assignment Operators:
# a. =
x = 5
print(x)        # 5

# b. +=
x += 3      # x = x + 3
print(x)        # 8

# c. -=
x -= 3      # x = x - 3
print(x)        # 5

# d. *=
x *= 3      # x = x * 3
print(x)        # 15

# e. /=
x /= 3      # x = x / 3
print(x)        # 5.0

# f. %=
x %= 3      # x = x % 3
print(x)        # 2.0

# g. //=
x //= 3      # x = x // 3
print(x)        # 0.0

# h. **=
x **= 3      # x = x ** 3
print(x)        # 0.0


# 2. Arithmetic Operators:
a = 5
b = 6

# a. Addition: +

print(a+b)      # 11

# b. Subtraction: -
print(a-b)      # -1

# c. Multiplication: *
print(a*b)      # 30

# d. Division: /
print(a/b)      # 0.8333333333333334

# e. Modulus: %
print(a % b)      # 5

# f. Exponentiation: **
print(a**b)     # 15625

# g. Floor Division: //
print(a//b)     # 0 (5/6=0.8333333333333334)

# h.  Floating numbers
print("Floating point numbers PI: ", 3.14)   # 3.14
print('Floating Point Number, gravity', 9.81)   # 9.81

# i. Complex numbers
print('Complex number: ', 1 + 1j)   # (1+1j)
print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))  # (2+0j)


# 3. Comparison Operators:

# a. ==
x = 5
y = 3
print(x == y)       # False

# b. !=
print(x != y)       # True

# c. >
print(x > y)        # True

# d. <
print(x < y)        # False

# e. >=
print(x >= y)       # True

# f. <=
print(x <= y)       # False


# 4. Logical Operators:
# a. and
x = 5
print(x > 3 and x < 10)     # True

# b. or
print(x > 3 or x < 4)       # True

# c. not
# False  : not le true lai false ma convert garxa and false lai true ma convert garxa
print(not (x > 3 and x < 10))


# 5. Identity Operators:
# a. is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)       # True
print(x is y)       # False

# b. is not
print(x is not z)       # False
print(x is not y)       # True

# ⭐️⭐️⭐️ Exercise ⭐️⭐️⭐️
# Calculating area of a circle
radius = 10
pi = 3.14
area = pi * radius ** 2
print("Area of circle is: ", area)      # 314.0
print("--"*20)

# Calculating area of a rectangle
length = 10
width = 5
area = length * width
print("Area of rectangle is: ", area)      # 50

# Calculating a weight of an object
mass = 50
gravity = 9.81
weight = mass * gravity
print("Weight of an object is: ", weight)      # 490.5

# Calculate the density of a liquid
mass = 50
volume = 20
density = mass / volume
print("Density of a liquid is: ", density)      # 2.5

# Comparing something gives either a True or False
print(True == True)    # True
print(False == False)    # True
print(True == False)    # False
print(True != False)    # True
print("--"*20)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle
base = int(input("Enter base of triangle: "))
height = int(input("Enter height of triangle: "))
area = 0.5 * base * height
print("Area of triangle is: ", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle
a = int(input("Enter side a of triangle: "))
b = int(input("Enter side b of triangle: "))
c = int(input("Enter side c of triangle: "))
perimeter = a + b + c
print("Perimeter of triangle is: ", perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("Area of rectangle is: ", area)
print("Perimeter of rectangle is: ", perimeter)


# Get radius of a circle using prompt. Calculate the area and circumference of the circle
radius = int(input("Enter radius of circle: "))
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print("Area of circle is: ", area)
print("Circumference of circle is: ", circumference)
print("--"*20)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = int(input("Enter x: "))
y = 2 * x - 2
x_intercept = (y + 2) / 2
y_intercept = 2 * x_intercept - 2
print("Slope is: ", y)
print("x-intercept is: ", x_intercept)
print("y-intercept is: ", y_intercept)
print("--"*20)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2 - y1) / (x2 - x1)
print("Slope is: ", slope)
euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Euclidean distance is: ", euclidean_distance)
print("--"*20)


# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
per_hour_rate = int(input("Enter per hour rate: "))
hours = int(input("Enter hours: "))
per_day = per_hour_rate * hours
print("Per day pay is: ", per_day)
print("pay per week is: ", per_day * 7)
print("pay per month is: ", per_day * 30)
print("pay per year is: ", per_day * 365)
print("--"*20)