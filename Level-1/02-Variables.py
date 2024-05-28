# ⭐️⭐️⭐️⭐️⭐️ Variables ⭐️⭐️⭐️⭐️⭐️
"""
- Variable are nothing but a container which store data in the memory.
- Variable vanako yuta box ho jasle data lai store garcha. 
"""

# ⭐️ Variable declaration
# Syntax: variable_name = value
name = "Manish"  # We can use single or double quotes
age = 20  # aru programing languages jasto ; semicolon use garna mildaina
print(name)  # print() function le hamro data lai console ma display garcha
print("--" * 20)

# Pyhhon ma variable declare garne keyword xaina. so we can declare name directly without using any keyword
x = 4
x = "Manish"
print(x)
print("--" * 20)

# ⭐️ lets assign some variable and print it
first_name = "Manish"
last_name = "Yadav"
country = "Nepal"
city = "Biratnagar"
age = 20
is_married = False
skills = ["Html", "Css", "Js", "Python", "React", "NextJs"]
personal_info = {
    "first_name": "Manish",
    "last_name": "Yadav",
    "country": "Nepal",
    "city": "Biratnagar",
}

print("First Name: ", first_name)
# len() function le string ko length nikalxa
print("first name length: ", len(first_name))
print("Last Name: ", last_name)
print("last name length: ", len(last_name))
print("Country: ", country)
print("City: ", city)
print("Age: ", age)
print("Married: ", is_married)
print("Skills: ", skills)
print("Personal Info: ", personal_info)
print("--" * 20)

# ⭐️ Declare multiple variables in one line
name, age, country, is_married = "Manish", 20, "Nepal", False
print(name, age, country, is_married)

# ⭐️ Casting : Type define garna ko lagi
# Syntax: variable_name = data_type(value)
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
print("x: ", x, "y: ", y, "z: ", z)
print("--" * 20)

# ⭐️ Check variable type
# Syntax: type(variable_name)
print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'float'>

# ⭐️⭐️ Variable Name ⭐️⭐️
"""
- Start with a Letter or Underscore: _name or name
- Followed by Letters, Digits, or Underscores: name_1 or name_2
- Case-Sensitive: name, Name, and NAME are three different variables
- Avoid Python Keywords: if, else, for, while, etc.
- Use Descriptive Names: name is better than n, student_name is better than s_n
- Avoid Single Underscores at the Start: _name is a valid name but it has a special meaning in Python
- Use Snake Case: student_name, phone_number, etc.
"""

# Valid variable name
name = "Manish"
first_name = "Manish"
first_name_1 = "Manish"
MyName = "Manish"

# Invalid variable name

# 1name="Manish"      # Variable name can't start with number
# first-name="Manish" # Variable name can't contain hyphen
# first name="Manish" # Variable name can't contain space

# ⭐️ Multi Words Variable Names
# 1. Camel Case: firstName, lastName, phoneNumber, etc.
phoneNumber = +9779804336000
firstName = "Manish"
# 2. Pascal Case: FirstName, LastName, PhoneNumber, etc.
LastName = "Yadav"
# 3. Snake Case: first_name, last_name, phone_number, etc.
middle_name = "Kumar"

# ⭐️ Assigning value to multiple variables
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# ⭐️ One Value to Multiple Variables
x1 = y1 = z1 = "Manish"
print(x1, y1, z1)  # Manish Manish Manish

# ⭐️ Unpack a Collection: List, Tuple, etc. ko data lai variable ma assign garna
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # 1 2 3

# a1,b1,c1,d1= numbers # ValueError: not enough values to unpack (expected 4, got 3)

# ⭐️ Output Variables: print() function le praye output variable lai console ma display garcha
x = "awesome"
print("Python is " + x)  # Python is awesome

first_name = "Manish"
last_name = "Yadav"
# 2 ota string jodda concat garxa    # Manish Yadav
print(first_name + " " + last_name)

w = 2
e = 3
print(w + e)  # 2 ota no ma operstion perform hunxa            # 5

# ⭐️⭐️ Global Variables ⭐️⭐️
# variables that can be accessed from any part of your Python code, both inside and outside functions
company = "Itp"


def myFunc():
    print("Company name is " + company)


myFunc()  # Company name is Itp

# ⭐️⭐️ Local Variables ⭐️⭐️
# variables that are created inside a function


def myFunc():
    name = "Manish"
    print("My name is " + name)


myFunc()  # My name is Manish
# print(name)     # NameError: name 'name' is not defined


# getting input from user
full_name = input("Enter your full name: ")
age = input("Enter your age: ")
print("Your name is " + full_name + " and you are " + age + " years old")


# Exercise
# 1. Using the len() built-in function, find the length of your first name
first_name = "Manish"
print(len(first_name))  # 6
print("_" * 20)

# 2. Compare the length of your first name and your last name
first_name = "Manish"
last_name = "Yadav"
print(len(first_name) == len(last_name))  # False
print("_" * 20)

"""
3. Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division

"""
num_one = 5
num_two = 4
total = num_one + num_two
print("Total :", total)

diff = num_two - num_one
print("Diff :", diff)

product = num_one * num_two
print("Product :", product)

division = num_one / num_two
print("Division :", division)

remainder = num_one % num_two
print("Remainder :", remainder)

exp = num_two**num_one
print("Exp :", exp)

floor_division = (
    num_one // num_two
)  # floor division vanako 5/4=1.25 huncha tara floor division ma 1 matra aauxa
print("Floor Division :", floor_division)


"""
4.The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
"""
radius = 30
PI = 3.14
area_of_circle = PI * radius * radius
print("Area of circle :", area_of_circle)

circum_of_circle = 2 * PI * radius
print("Circum of circle :", circum_of_circle)

radius = int(input("Enter radius :"))
area_of_circle = PI * radius * radius
print("Area of circle :", area_of_circle)

# 5. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name :")
last_name = input("Enter your last name :")
country = input("Enter your country :")
age = input("Enter your age :")

print("First Name :", first_name)
print("Last Name :", last_name)
print("Country :", country)
print("Age :", age)

# 6. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help("keywords")
