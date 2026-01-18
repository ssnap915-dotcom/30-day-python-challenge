print("--- PYTHON FUNCTIONS ---\n")

#1. SIMPLE FUNCTION
def greet():
    print("Hello, Developer!")
greet()
print()   

#2. FUNCTION WITH PARAMETERS
def greet_person(name):
    print(f"Hello, {name}!")
greet_person("Bhone")  
greet_person("Myint")
print() 

#3.FUNCTION WITH RETURN
def add(a,b):
    return a + b
result = add(5,3)
print(f"5 + 3 = {result}\n")

#4. FUNCTION WITH DEFAULT PARAMETERS
def introduce(name, age=25):
    print(f"My name is {name}, I'm {age} years old")
introduce("Bhone")
introduce("Myint",30)
print()    

#5. FUNCTION WITH MULTIPLE RETURNS
def calculate(a,b):
    sum_result = a + b
    diff = a - b
    product = a * b
    return sum_result,diff,product
s, d, p = calculate(10,5)
print(f"Sum: {s}, Difference: {d}, Product: {p}\n")

# 6. PRACTICAL EXAMPLE
def is_valid_age(age):
    """Check if age is valid for programming"""
    if age < 0:
        return  False, "Age cannot be negative"
    elif age < 10:
        return False, "Too young to start professionally"
    elif age > 100:
        return False, "Age seems unrealistic"
    else:
        return True, "Perfect age to code!"
valid, message = is_valid_age(26)
print(f"Age 26 : {message}\n")    