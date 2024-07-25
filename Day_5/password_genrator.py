import string, random
if __name__ == '__main__':
    print("Welcome to password Generator!")
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    alphabets = string.ascii_letters
    numbers = string.digits
    other_characters = string.punctuation
    no_of_characters = int(input("What is the length of the password would you like? "))
    no_of_alphabets = int(input("Number of characters would you like in the password? "))
    no_of_digits = int(input("Number of digits would you like in the password? "))
    print(f"The other characters would be symbols from {other_characters}")
    password_chars = []
    for i in range(no_of_alphabets):
        password_chars.append(alphabets[random.randint(0,len(alphabets)-1)])
    for i in range(no_of_digits):
        password_chars.append(numbers[random.randint(0, len(numbers)-1)])
    for i in range(no_of_characters-no_of_alphabets-no_of_digits):
        password_chars.append(other_characters[random.randint(0, len(other_characters)-1)])
    random.shuffle(password_chars)
    print("".join(password_chars))