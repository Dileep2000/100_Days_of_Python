import random
if __name__ == "__main__":
    stages = [
        '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        ''', '''
        +---+
        |   |
            |
            |
            |
            |
        =========
        '''
    ]
    words = ["Apple", "Ball", "Cat", "Dog", "Eagle", "Frog", "Goat", "Horse", "India", "Jungle", "Kitten", "Lizard", "Mammal",
             "Net", "Owl", "Parrot", "Queen", "Render", "Snow", "Tiger", "Universe", "Viruses", "Wind", "Xerox", "Yellow", "Zebra"]
    # with open("./Day_7/random_words.txt", "r") as word:
    #     words.extend(word.readlines())
    # words = list(map(lambda x: x.replace("\n",""), words))
    word = random.choice(words).lower()
    gusses = []
    matches = []
    lifes = 6
    for _ in word:
        matches += "_"
    print(word)
    while "_" in matches:
        guess = input("Guess a letter: ").lower()
        if guess in gusses:
            print(
                f"You have already guessed this letter. Please try with another letter.")
        else:
            gusses.append(guess)
            for i in range(len(word)):
                if guess == word[i]:
                    matches[i] = guess
                    break
        if guess not in word:
            print(
                f"You lost a life. {guess} is not in the word. please try guessing another letter.")
            lifes -= 1
            if lifes == 0:
                print(stages[0])
                print("You Loose.")
                break
            else:
                print(f"You still have {lifes} lifes left.")
        print(matches)
        print(stages[lifes])
        if "_" not in matches:
            print(
                f"YaaY, You WON!! You guessed it correctly. The word is {word}")