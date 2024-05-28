
"""  
                    ⭐️⭐️⭐️ Control Flow  ⭐️⭐️⭐️
- Sabai code ek choti ma run garna chahdaenam so control flow use garxau.
- Control flow le hamile code ko flow lai control garnasakxau.
- Control flow ko example: if, Elif,  etc

"""

# Python Conditions and If statements
"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

# if statement
a=18
if a>=18: print("You are eligible to vote.")  
print("--"*20)
# if else statement
if a>=18:
    print("You are eligible to vote.")
else :
    print("You are not eligible to vote.")
    print("--"*20)
    
# if elif else statement
if a>=18:
    print("You are eligible to vote.")
elif a==17:
    print("You are not eligible to vote.")
else :
    print("You are not eligible to vote.")
    
print("--"*20)

temp=30
if temp<10:
    print("It's cold outside.")
elif temp>=10 and temp<30:
    print("It's warm outside.")
else:
    print("It's hot outside.")
    
    print("--"*20)
    
    
# Short Hand If
if a>10: print("a is greater than 10")

# Short Hand If ... Else
temperture=15
print("It's cold outside.") if temperture<10 else print("It's warm outside.")


# Ternary Operators, or Conditional Expressions.
age=18
print("You are eligible to vote.") if age>=18 else print("You are not eligible to vote.")

# And
a=10
b=20
c=30
if a>b and a>c:
    print("a is the largest number.")
    
# Or

if a>b or a>c:
    print("a is the largest number.")
    
# not
if not a>b:
    print("a is not greater than b.")
    
# pass : if statement cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

if a>b:
    pass


print("--"*20)


# ⭐️⭐️⭐️ Loops ⭐️⭐️⭐️
# Python has two primitive loop commands:
# 1. while loops
"""
    syntax:
        while condition:
            statement(s)

"""
    
i=1
while i<6:      # less than 6 xa vane 5 samma matra loop hunxa 6 ma terminate hunxa
        print(i)
        i+=1    # i=i+1
print("--"*20)


# break: while contition true vayane loop break hunxa
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
print("--"*20)
    
# continue: while condition true vayane loop continue hunxa
i=0
while i<6:
    i+=1
    
    if i==3:
        continue
    print(i)
    
print("--"*20)

# else: while condition false vayane else block execute hunxa
i=0
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")
print("--"*20)
    
    
# 2. for loops
"""
    syntax:
        for variable in sequence:
            statement(s)
"""
cities= ["Kathmandu", "Pokhara", "Biratnagar", "Birgunj", "Dharan"]
for city in cities:
    print(city)
print("--"*20)

# Looping Through a String
name="Manish"
for x in name:
    print(x)
print("--"*20)

# Break Statement
countries= ["Nepal", "India", "China", "Japan", "USA"]
for country in countries:
    print(country)
    if(country=="China"):
        break
print("--"*20)
    
# Continue Statement
countries= ["Nepal", "India", "China", "Japan", "USA"]
for country in countries:
    if(country=="China"):
        continue
    print(country)
print("--"*20)
    
  
# range() function
for x in range(6):
    print(x)
print("--"*20)

for x in range(2,6):
    print(x)
print("--"*20)

for x in range(2,30,3):     # 3 ko difference ma
    print(x)
print("--"*20)

# Nasted Loops
countries= ["Nepal", "India", "China"]
cities= ["Kathmandu", "Delhi", "Beijing"]

for country in countries:
    for city in cities:
        print(country, city)
print("--"*20)