import random
if __name__ == "__main__":
    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/        
    """)
    print("Welcom to Hangman.\nYou have to save your partner from hanging by correctly guessing the random word. You have six lifes to guss the correct words.\nEach time you guess a word wrong your partner will loose a life and will die if he looses all his lifes.\n\nGo On and Happy Gaming!!!")
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
                print("""
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
                        """)
                print(f"You Loose. The word is {word}. Better luck next time.")
                break
            else:
                print(f"You still have {lifes} lifes left.")
        print(matches)
        print(stages[lifes])
        if "_" not in matches:
            print("""
 _   _  ___  _   ___      _____  _ __  
| | | |/ _ \| | | \ \ /\ / / _ \| '_ \ 
| |_| | (_) | |_| |\ V  V / (_) | | | |
 \__, |\___/ \__,_| \_/\_/ \___/|_| |_|
  __/ |                                
 |___/       
                    """)
            print(
                f"YaaY, You WON!! You guessed it correctly. The word is {word}")
