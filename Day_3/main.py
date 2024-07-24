# Control flow and Conditional statements

# Even or odd
num = int(input())

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# BMI Calculator

height = float(input())
weight = int(input())
bmi = weight/(height*height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")


# Leap Year

# Which year do you want to check?
year = int(input())
if year % 100 == 0:
    if year % 400 == 0:
        print("Leap year")
    else:
        print("Not leap year")
else:
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Not leap year")

# Python Pizza
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N
bill = 0
if size == "L":
    bill += 25
elif size == "M":
    bill += 20
else:
    bill += 15

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# Love Calculator

print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
name1 = name1.lower()
name2 = name2.lower()
score_1 = 0
score_2 = 0
for i in "true":
    score_1 += name1.count(i) + name2.count(i)
for i in "love":
    score_2 += name1.count(i) + name2.count(i)
score = score_1*10 + score_2

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
