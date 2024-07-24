import random
# Random is used to generate random numbers and has many uses.

random_int = random.randint(0,1)

# Heads or Tails
head_or_tails = random.randint(0,1)
if head_or_tails == 0:
    print("Heads")
else:
    print("Tails")

# Random choice
names = ['X', 'Y', 'Z']
print(random.choice(names))

lists = []
lists.append(1)
lists.extend([2,3])
lists.insert(3,4)
lists.sort()
