# Data Types

# Integers
integer = 123

# Floats

weight = 126.3

# Strings

name = "Dileep"

# Boolean

married = False

# Type error is an error when there is a specific type of data is expected but other data type is given. Like concatination of int and strings.

# print("My age is "+ 24) will give an Type Error.

# type

print(type(1))  # it will print the data type of the data passed.

# Data type casting

# This will print string calss as we converted int into string.
print(type(str(1)))

# Sum of digits in a number

num = input()
num_sum = 0
for i in num:
    num_sum += int(i)

print(num_sum)

# Mathematical operations

# 3*3 Multiplication
# 3/3 Division
# 3-3 Subtraction
# 3+3 Addition
# 3**3 Exponentiation(Power)

# PEMDAS
# () Paranthesis
# ** Exponent
# * Multiplication
# / Division
# + Addition
# - Subtraction

# Calculation will go left to right if there are equal importance

# BMI Calculator

weight = float(input("Enter your weight"))
height = float(input("Enter your height"))
bmi = weight/height**2
print(bmi)

# round funtion will round the flaot into specified decimal places. By default it will give integer.
# F strings

print(f'Your BMI Index is {bmi}')
