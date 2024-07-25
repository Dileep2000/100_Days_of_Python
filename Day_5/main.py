# Loops

names = ['A', 'B', 'C', 'D', 'E', 'F']
for name in names:
    print(name)

for i in range(len(names)):
    print(i)

# Average height
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sum_of_heights = 0
no_of_students = 0
for height in student_heights:
  sum_of_heights += height
  no_of_students += 1
print(f'total height = {sum_of_heights}')
print(f'number of students = {no_of_students}')
print(f'average height = {round(sum_of_heights/no_of_students)}')

# We can also use len and sum functions which is alos same as above

# Maximum score
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
max = 0
for i in student_scores:
  if i > max:
    max = i
print(f'The highest score in the class is: {max}')
# max function also returns the maximum number in the list.

# Sum of even numbers
target = int(input())  # Enter a number between 0 and 1000
sum_of_even = 0
for i in range(2, target+1, 2):
  sum_of_even += i
print(sum_of_even)

# FizzBuzz
'''
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

Your program should print each number from 1 to 100 in turn and include number 100.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''
for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
