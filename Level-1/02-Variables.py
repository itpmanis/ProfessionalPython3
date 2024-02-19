"""

 ⭐️⭐️ Variables ⭐️⭐️
- Variable are nothing but a container which store data in the memory.
- Variables act like boxes that store data in memory.

 ⭐️⭐️ Variable Name ⭐️⭐️
- Start with a Letter or Underscore: _name or name
- Followed by Letters, Digits, or Underscores: name_1 or name_2
- Case-Sensitive: name, Name, and NAME are three different variables
- Avoid Python Keywords: if, else, for, while, etc.
- Use Descriptive Names: name is better than n, student_name is better than s_n
- Avoid Single Underscores at the Start: _name is a valid name but it has a special meaning in Python
- Use Snake Case: student_name, phone_number, etc.

"""

# ⭐️ Variable declaration
# Syntax: variable_name = value
full_name = "Itp Manish"        # String Variable
age = 25                        # Integer Variable

# Printing the values stored in variables using the print() function.
print(full_name)                # Output: Itp Manish
print(age)                      # Output: 25

# Python allows you to reassign a variable to a different data type.
age = "Twenty Five"             # previous value of age was 25 (integer) but now it is "Twenty Five" (string)

# Demonstrating the dynamic typing feature of Python:
# Variables can change types after they have been set.
print(age)                      # Output: Twenty Five


# Valid variable names:
fullName="Itp Manish"           # Camel Case
full_name="Itp Manish"          # Snake Case
_full_name="Itp Manish"         # Underscore Case but not recommended due to special meaning in Python, starts with underscore
full_name_1="Itp Manish"        # Snake Case with number

# Invalid variable names:
# 1full_name="Itp Manish"        # Cannot start with a digit
# full-name="Itp Manish"         # Cannot use hyphen
# full name="Itp Manish"         # Cannot use space
# full@name="Itp Manish"         # Cannot use special characters except underscore
# full name="Itp Manish"         # Cannot use space
