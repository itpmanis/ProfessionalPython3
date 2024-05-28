
# ⭐️⭐️ Data Types ⭐️⭐️
# category that defines the type of data a variable can hold, like numbers, text, or true/false values.

# ⭐️ 1. Text Type: str
first_name = "Manish"    # can use single or double quotes
last_name = 'Kumar'
print(type(first_name))     # <class 'str'>
print(first_name + " " + last_name)     # Manish Kumar

# muktiple line string
address = """Kathmandu
Nepal"""
print(address)

# Strings are Arrays
print(address[0])   # K

# find length of string
print(len(address))     # 15

text = "my name is manish kumar yadav."
print("name" in text)   # True

# string slicing
ghar = "kathmandu"
# thm    # start from index 2 and end at index 5 (not included) last ko index-1
print(ghar[2:5])

# Slice From the Start
print(ghar[:5])  # kathm

# Slice To the End
print(ghar[1:])

# Negative Indexing
newHome = "Biratnagar"
print(newHome[-5:-2])   # atn

# Upper Case
a = "manish"
print(a.upper())    # MANISH

# Lower Case
b = "MANISH"
print(b.lower())    # manish

# Remove Whitespace
c = "  manish  "
print(c.strip())    # manish

# Replace String
d = "manish"
print(d.replace("m", "M"))   # Manish

# Split String
e = "manish kumar yadav"
print(e.split(" "))     # ['manish', 'kumar', 'yadav']

# concat string
f = "manish"
g = "kumar"
print(f+g)      # manishkumar

print("--"*20)

# ⭐️ 2. Numeric Types: int, float, complex
x = 4  # int: whole number, positive or negative, without decimals, of unlimited length
y = 4.0  # float: number, positive or negative, containing one or more decimals
z = 1j  # complex: number, written with a "j" as the imaginary part
print(type(x))      # <class 'int'>
print(type(y))      # <class 'float'>
print(type(z))      # <class 'complex'>
print(z)
print("--"*20)
print("--"*20)

# ⭐️ 3. Sequence Types: list, tuple, range

# 3.1 List: ordered and changeable. Allows duplicate members. index starts from 0
fruits = ["apple", "banana", "cherry", "apple"]
print(type(fruits))     # <class 'list'>
print(fruits)       # ['apple', 'banana', 'cherry', 'apple']
print(fruits[0])        # apple
print(fruits[1])        # banana
fruits[0] = "orange"
print(fruits)       # ['orange', 'banana', 'cherry', 'apple']
print("--"*20)

# 3.2 Tuple: ordered and unchangeable. Allows duplicate members. index starts from 0
fruits = ("apple", "banana", "cherry", "apple")
print(type(fruits))     # <class 'tuple'>
print(fruits)       # ('apple', 'banana', 'cherry', 'apple')
print(fruits[0])        # apple
# fruits[0]="orange"      # TypeError: 'tuple' object does not support item assignment

# 3.3 Range: ordered and immutable (unchangable). Represents a sequence of numbers. Index starts from 0.
numbers_range = range(6)
print(type(numbers_range))  # <class 'range'>
print(numbers_range)        # range(0, 6)
print(list(numbers_range))  # [0, 1, 2, 3, 4, 5]
print("--"*20)


# ⭐️ 4. Mapping Type: dict (dictionary) is a mapping type that allows you to store key-value pairs.
customer_details = {
    "name": "Manish",
    "age": 20,
    "address": "Kathmandu",
    "phone": "9804336000"
}
print(type(customer_details))   # <class 'dict'>
print(customer_details["name"])    # Output: Manish      access value using key
customer_details["married"] = False     # add new key-value pair
# {'name': 'Manish', 'age': 20, 'address': 'Kathmandu', 'phone': '9804336000', 'married': False}
print(customer_details)
# True     check if key exists in dictionary
print("name" in customer_details)
print(len(customer_details))    # 5     get length of dictionary
customer_details.pop("married")     # remove key-value pair
# {'name': 'Manish', 'age': 20, 'address': 'Kathmandu', 'phone': '9804336000'}
print(customer_details)
customer_details.clear()    # remove all key-value pairs
print(customer_details)     # {}
print("--"*20)


# ⭐️ 5. Set Types: set, frozenset
"""
1. Set (set):
    - A set is an unordered collection of unique elements.
    - It is mutable, meaning you can add or remove elements after creation.
    - Created using curly braces {} or the set() constructor.

"""
friends = {"manish", "dipesh", "bhanu", "sushant"}
print(type(friends))    # <class 'set'>
print(friends)      # {'manish', 'bhanu', 'sushant', 'dipesh'}
friends.add("bidhyanand")
print(friends)      # {'manish', 'bhanu', 'sushant', 'dipesh', 'bidhyanand'}
friends.remove("manish")
print(friends)      # {'bhanu', 'sushant', 'dipesh', 'bidhyanand'}
print("--"*20)

"""
    2. Frozen Set (frozenset):
        - A frozen set is an immutable version of a set.
        - Once created, you cannot add or remove elements from a frozenset.
"""
friends_frozen = frozenset([1, 2, 3, 4])
print(type(friends_frozen))     # <class 'frozenset'>
print(friends_frozen)       # frozenset({1, 2, 3, 4})
# friends_frozen.add(5)       # AttributeError: 'frozenset' object has no attribute 'add'

# ⭐️ 6. Boolean Type: bool
# boolean can have two values: True or False
is_active = True
is_admin = False
print(type(is_active))      # <class 'bool'>
print(is_active)        # True
print(is_admin)         # False
print(is_active == is_admin)    # False
print(is_active != is_admin)    # True

print("--"*20)

# ⭐️ 7. Binary Types: bytes, bytearray, memoryview
"""
  a.  Bytes (bytes):
        bytes is an immutable sequence of bytes.
        It is created using the b prefix or the bytes() constructor.
    """
x = b"Hello"
print(type(x))      # <class 'bytes'>
print(x)        # b'Hello'
print(x[0])     # 72        # ASCII value of H
print(x[1])     # 101
print(x[2])     # 108

y = bytes(5)
print(y)        # b'\x00\x00\x00\x00\x00'       # \x00 is null character
print("--"*20)

"""
b. Bytearray (bytearray):
    bytearray is a mutable sequence of bytes.
    It allows you to modify the elements after creation.
    Created using the bytearray() constructor.
"""
mutable_bytes = bytearray(b'Python')
print(mutable_bytes)  # Output: bytearray(b'Python')

mutable_bytes[0] = ord('J')  # Changing 'P' to 'J'
print(mutable_bytes)  # Output: bytearray(b'Jython')
print("--"*20)


"""
c.Memoryview (memoryview):
    memoryview provides a view of the internal memory of an object (such as bytes or bytearray) without copying.
    It allows you to access the data directly.
"""

byte_data = b'Python'
view = memoryview(byte_data)

# Accessing the memory directly
print(view[1])  # Output: 121 (ASCII code for 'y')
print("--"*20)


# ⭐️ Different python data types
first_name = "Manish"  # str
last_name = "Yadav"  # str
age = '20'  # str        uses quotes so it is string
country = "Nepal"  # str
phone_number = "9804336000"  # str
salary = 1000.00  # float
is_married = False  # bool
print("--"*20)


# lets print some output
print("First Name: ", type("Manish"))
print("Age: ", type(20))
print("Salary: ", type(1000.00))
print("Is Married: ", type(False))
print("Complex number: ", type(1+3j))
print("List: ", type(["Html", "Css", "Js", "Python", "React", "NextJs"]))
print("Tuple: ", type(("Html", "Css", "Js", "Python", "React", "NextJs")))
print("Set: ", type({"Html", "Css", "Js", "Python", "React", "NextJs"}))
print("Dictionary: ", type({"name": "Manish", "age": 20}))
print("--"*20)



# ⭐️⭐️⭐️ Exercise ⭐️⭐️⭐️
# Print the length of the company string using len() method and print().
name= "Manish Kumar Yadav"
print(len(name))    # 18
print("--"*20)

# Change all the characters to uppercase letters using upper() method.
print(name.upper())     # MANISH KUMAR YADAV

# Change all the characters to lowercase letters using lower() method.
print(name.lower())     # manish kumar yadav

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
string = "Coding For All"
print(string.capitalize())      # Coding for all    // sentence ko first letter lai capital banauxa.
print(string.title())       # Coding For All     // every word ko first letter lai capital banauxa.
print(string.swapcase())        # cODING fOR aLL     // capital lai lower case ma ani lower case lai capital ma convert garxa.
print("--"*20)

# Cut(slice) out the first word of Coding For All string.
name="Manish Kumar Yadav"
print(name.split(" ")[0])       # Manish        // split() method le string lai list ma convert garxa and list ko first element lai print garxa.
print(name.split(" ",1)[1])     # Kumar Yadav   //ya chi first space ko base ma string lai 2 parts ma divide garxa and list ko second element lai print garxa.

#  Check if string contains a word
print("Manish" in name)     # True

# Replace words
print(name.replace("Manish", "Itp"))     # Itp Kumar Yadav

# Split the string
print(name.split(" "))      # ['Manish', 'Kumar', 'Yadav']

# Splitting at commas
friends = "Manish, Dipesh, Bhanu, Sushant"
print(friends.split(","))       # ['Manish', ' Dipesh', ' Bhanu', ' Sushant']

# Indexing
print(name[0])    # M

# Last occurrence
print(name.rindex("a"))     # 16

# Index of 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))  # Output: 31

# Last index of 'because'
print(sentence.rindex('because'))  # Output: 47

# Slicing
print(sentence[31:47])  # Output: because because because


# Trimming whitespace
print('   Coding For All      '.strip())

# isidentifier() method : vanako string le identifier ho ki haina check garxa, vako string le variable name ho ki haina check garxa.
print("Manish Kumar Yadav".isidentifier())    # False
print("ManishKumarYadav".isidentifier())      # True 

# Join with hash and space
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))    # Django # Flask # Bottle # Pyramid # Falcon

# New line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")


# Tab escape sequence
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# String formatting
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Arithmetic operations
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")

# ⭐️⭐️⭐️ Exercise : List⭐️⭐️⭐️
# Declare an empty list
empty_list = []
print(empty_list)       # []

# Declare a list with more than 5 items
new_list = ["Manish", "Kumar", "Yadav", "Biratnagar", "Nepal"]
print(new_list)     # ['Manish', 'Kumar', 'Yadav', 'Biratnagar', 'Nepal']

# Find the length of your list
print(len(new_list))    # 5

# Get the first item, the middle item and the last item of the list
print("First Item: ", new_list[0])     # First Item:  Manish
print("Middle Item:", new_list[len(new_list)//2])     # Middle Item: Yadav
print("Last Item: ", new_list[-1])     # Last Item:  Nepal

# Declare a list called mixed_data_types
mixed_list = ["Manish", 20, 9804336000, True, 1000.00]
print(mixed_list)       # ['Manish', 20, 9804336000, True, 1000.0]

# Declare a list variable named it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)     # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(len(it_companies))    # 7
print(it_companies[0])      # Facebook    # first item
print(it_companies[len(it_companies)//2])     # Apple    # middle item
print(it_companies[-1])     # Amazon    # last item
print(it_companies[0:3])    # ['Facebook', 'Google', 'Microsoft']     # first 3 items 
print(it_companies[-3:])    # ['IBM', 'Oracle', 'Amazon']     # last 3 items
print(it_companies.index("Google"))     # 1     # index of Google
print(it_companies.append("Twitter"))   # None      # append() method le list ma item add garxa and return gardaina
print(it_companies)     # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']

# Insert an IT company in the middle of the companies list
print(it_companies.insert(len(it_companies)//2, "Tiktok"))     
print(it_companies)     # ['Facebook', 'Google', 'Microsoft', 'Tiktok', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']
print("--"*20)
# Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[it_companies[0]== it_companies[0].upper()])    

# Join the it_companies with a string '#; '
print("#; ".join(it_companies))     # Facebook#; Google#; Microsoft#; Tiktok#; Apple#; IBM#; Oracle#; Amazon#; Twitter

# Check if a certain company exists in the it_companies list.
print('Microsoft' in it_companies)

# Sort the list using sort() method
it_companies.sort()

# Reverse the list in descending order using reverse() method
it_companies.reverse()

# Slice out the first 3 companies from the list
first_three = it_companies[:3]

# Slice out the last 3 companies from the list
last_three = it_companies[-3:]

# Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:
    middle_companies = it_companies[middle_index]

# Remove the first IT company from the list
it_companies.pop(0)

# Remove the middle IT company or companies from the list
if len(it_companies) % 2 == 0:
    it_companies.pop(middle_index - 1)
    it_companies.pop(middle_index - 1)
else:
    it_companies.pop(middle_index)

# Remove the last IT company from the list
it_companies.pop()

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

# Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')
print(full_stack)


# # List of 10 students' ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print("Min Age: ", min_age)     # Min Age:  19
print("Max Age: ", max_age)     # Max Age:  26

# Find the average age
total_age = sum(ages)
number_of_students = len(ages)
average_age = total_age / number_of_students
print("Average Age: ", average_age)     # Average Age:  22.8


# Find the range of the ages
age_range = max_age - min_age
print("Age Range: ", age_range)     # Age Range:  7

# Compare the value of (min - average) and (max - average)
min_average = min_age - average_age
max_average = max_age - average_age
print("Min - Average: ", min_average)     # Min - Average:  -3.8
print("Max - Average: ", max_average)     # Max - Average:  3.2

# Find the middle countries in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_countries = countries[len(countries) // 2 - 1:len(countries) // 2 + 1]
print(middle_countries)     # ['USA', 'Finland']

# ⭐️⭐️⭐️ Exercise : Touple ⭐️⭐️⭐️

# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of siblings
brothers = ('manish', 'nirajan')
sisters = ('shruti', 'shruti2')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)     # ('manish', 'nirajan', 'shruti', 'shruti2')

# How many siblings do you have?
num_siblings = len(siblings)    # 4
print("Number of siblings:", num_siblings)   # Number of siblings: 4

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father = 'Rambabu'
mother = 'Manju'
family_members = siblings + (father, mother)
print(family_members)   # ('manish', 'nirajan', 'shruti', 'shruti2', 'Rambabu', 'Manju'


# Unpack siblings and parents from family_members
brother1, brother2, sister1, sister2, father, mother = family_members
print("Brother1: ", brother1)   # Brother1:  manish
print("Brother2: ", brother2)   # Brother2:  nirajan
print("Sister1: ", sister1)     # Sister1:  shruti
print("Sister2: ", sister2)     # Sister2:  shruti2
print("Father: ", father)       # Father:  Rambabu
print("Mother: ", mother)       # Mother:  Manju

# Create fruits, vegetables, and animal products tuples
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('meat', 'milk', 'eggs')

# Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)    # ('apple', 'banana', 'orange', 'carrot', 'broccoli', 'spinach', 'meat', 'milk', 'eggs')

# Change the tuple to a list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items
middle_index = len(food_stuff_tp) // 2
middle_items = food_stuff_tp[middle_index] if len(food_stuff_tp) % 2 != 0 else food_stuff_tp[middle_index - 1:middle_index + 1]

# Slice out the first three items and the last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)  # Output: False
print('Iceland' in nordic_countries)  # Output: True


# ⭐️⭐️⭐️ Exercise : Set ⭐️⭐️⭐️

# Given set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
it_companies.update({'LinkedIn', 'Salesforce'})

# Remove one of the companies from the set it_companies
it_companies.remove('Facebook')

# What is the difference between remove and discard
# The difference between remove() and discard() is that remove() will raise a KeyError if the element is not present in the set, while discard() won't raise any error.


# Sets A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Join A and B
union_AB = A.union(B)
print(union_AB)     # {1, 2, 3, 4, 5, 6, 7, 8}  // duplicate elements are removed

# Find A intersection B
intersection_AB = A.intersection(B)
print(intersection_AB)      # {4, 5}    // common elements

# Is A subset of B
subset_check = A.issubset(B)
print(subset_check)     # False //subset vanako every element of A is in B

# Are A and B disjoint sets
disjoint_check = A.isdisjoint(B)

# Join A with B and B with A
A_B = A.union(B)
B_A = B.union(A)

# What is the symmetric difference between A and B
symmetric_difference_AB = A.symmetric_difference(B)

# Delete the sets completely
del A, B

# Exercises: Level 3

# Given list of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Convert the ages to a set
ages_set = set(ages)



# ⭐️⭐️⭐️ Exercise : Dictionary ⭐️⭐️⭐️

# give set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)     # {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter'}

# Insert multiple IT companies at once to the set it_companies
it_companies.update({'LinkedIn', 'Salesforce'})

# Remove one of the companies from the set it_companies
it_companies.remove('Facebook')

# What is the difference between remove and discard
# The difference between remove() and discard() is that remove() will raise a KeyError if the element is not present in the set, while discard() won't raise any error.


# Sets A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Join A and B
union_AB = A.union(B)

# Find A intersection B
intersection_AB = A.intersection(B)

# Is A subset of B
subset_check = A.issubset(B)

# Are A and B disjoint sets
disjoint_check = A.isdisjoint(B)

# Join A with B and B with A
A_B = A.union(B)
B_A = B.union(A)

# What is the symmetric difference between A and B
symmetric_difference_AB = A.symmetric_difference(B)

# Delete the sets completely
del A, B

# Exercises: Level 3

# Given list of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Convert the ages to a set
ages_set = set(ages)

# Compare the length of the list and the set
# The set will have fewer elements if there are duplicate ages in the list, as sets only contain unique elements.

# Exercises: Level 4

# Difference between string, list, tuple, and set:
# String: Ordered collection of characters. Immutable.
# List: Ordered collection of elements. Mutable.
# Tuple: Ordered collection of elements. Immutable.
# Set: Unordered collection of unique elements. Mutable.

# Unique words in the given sentence
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
num_unique_words = len(unique_words)
print("Number of unique words:", num_unique_words)

