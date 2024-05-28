
"""
⭐️⭐️⭐️  Functions ⭐️⭐️⭐️
- - function is a block of code design to perform particular task.
- - function is a block of code which only runs when it is called.
- - function can be used again and again.

- syntax:
    def function_name():
        statement(s)

"""

#⭐️  Creating a Function
def namaste():
    print("Namaste Nepal")
    
#⭐️ Calling a Function
namaste()
print("--"*20)


#⭐️ Parameter and Argument
def add(num1,num2):     # num1 and num2 are parameters
    print(num1+num2)
    
add(2,3)    # ya bata 2 and 3 arguments pass garako

# tabal banam 1 to 20 ko
def table(num):
    for i in range(1,num+1):
        print("table of",i)
        for j in range(1,11):
            print(i,"*",j,"=",i*j)
table(20)    
        
        
#⭐️ Number of Arguments: function le jatiota argumet expect garxa teti ota argument pathaunu parxa no more no less.
def mul(num1,num2):
    print(num1*num2)
    
mul(2,3)    # 2 arguments
# mul(2,3,4)  # 3 arguments , 2 ota positional argument aspect garxa but we are passing 3 arguments
# mul(2)       # 1 argument , 2 ota positional argument aspect garxa but we are passing 1 arguments
print("--"*20)

# ⭐️ Arbitrary Arguments, *args: if hamili tha xaina kati ota argument pass garne vani *args use garne, *args le unlimited argument accept garxa.
def add(*args):
    sum=0
    for i in args:
        sum+=i   # sum=sum+i
    print(sum)
    
add(2,3,8,9,10,20,30,40,50,60,70,80,90,100)
print("--"*20)

# Default Parameter Value
odd=[1,3,5,7,9]
def sum(list):
    sum=0
    for i in list:
        sum+=i
    print(sum)

sum(odd)
print("--"*20)

# return statement
def add(num1,num2):
    return num1+num2    # return le function bata value return garxa ani tyo value lai function call garda use garna milxa, return paxe ko code run hudaina.
    print("hello")      # yo print statement run hudaina.
print(add(2,3))

# pass Statement: function ma k kura garna xaina vani pass statement use garne. like khae return or print garnu xaina vani pass statement use garne.
def hello():
    pass
hello()

print("--"*20)

# ⭐️ Built in functions : built in function haru python ma pahile bata vako function haru hunxa.
# 1. print() : screen ma text or value print garxa.
print("hello world")

# 2. len(): yesla string, list, tuple, dictionary, set ko length dinxa.
print(len("hello world"))

# 3. Input(): user bata input linxa.
name=input("Enter your name: ")
print("Your name is",name)

# 4. type(): yesla data type dinxa.
print(type("hello world"))
print(type(10))

# 5. int(): yesla integer ma convert garne kaam garxa.
print(int(3.14))    # 3   3.14 lai 3 ma convert garxa.

# 6. float(): yesla float ma convert garne kaam garxa.
print(float(3))     # 3.0   3 lai 3.0 ma convert garxa.

# 7. str(): yesla string ma convert garne kaam garxa.
print(str(3))       # "3"   3 lai "3" ma convert garxa.

# 8. list(): yesla list ma convert garne kaam garxa.
name="manish"
print(list(name))   # ['m', 'a', 'n', 'i', 's', 'h']   string lai list ma convert garxa.

# 9. max(): yesla maximum value dinxa.
print(max(1,2,3,4,5,6,7,8,9,10))    # 10

# 10. min(): yesla minimum value dinxa.
print(min(1,2,3,4,5,6,7,8,9,10))    # 1

# 11. random(): yesla random value dinxa.
import random
print(random.random())      # 0.8457574959107739   0 to 1 samma ko random value dinxa.

        # lets print random number between 1 to 10
import random
print(random.randint(1,10))    
print(random.randint(20,25))
