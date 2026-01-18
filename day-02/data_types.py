print("--- PYTHON DATA TYPED ---\n")

# 1. STRINGS
name = "Python Developer"
print(f"String: {name}")
print(f"Length: {len(name)}")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"First 6 chars: {name[:6]}\n")

#2. NUMBERS
#Integer
age = 26
print(f"Integer: {age}")
print(f"Type: {type(age)}\n")

#Float
price = 99.99
print(f"Float: {price}")
print(f"Type: {type(price)}\n")

#3. BOOLEAN
is_learning = True
is_expert = False
print(f"Boolean: {is_learning}")
print(f"Am I learning? {is_learning}")
print(f"Am I Expert? {is_expert}\n")

#4. TYPE CONVERSION
num_string = "100"
num_int = int(num_string)
print(f"String '{num_string}' converted to int : {num_int}")
print(f"Type: {type(num_int)}\n")


