if __name__ == "__main__":
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ". |
    |___________________ | _._"  ,. .` ` `` ,  `"-._"-._   ". '__ | ___________________
            |           | o`"=._` , "` `; .". ,  "-._"-._;;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    *******************************************************************************
    ''')
    print()
    print("Welcome to treasure Island.")
    print("Your mission is to find the treasure.")
    print("You are at a cross road. Where do you want to go? Type \"Left\" or \"Right\"")
    left_or_right = input()
    if left_or_right.lower() == "left":
        print("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
        swim_or_wait = input()
        if swim_or_wait.lower() == "wait":
            print("You arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which color do you choose?")
            color = input()
            if color.lower() == "yellow":
                print('''
                        .-'"'-.
   / #     \
  : #       :   .-'"'-.
   \       /   / #     \
    \     /   : #       :
     `'q'`     \       /
       (        \     /
        ) .-'"'-.`'q'`
       ( /       \ (
        )         : ) .-'"'-.
       ( \       / ( /       \
          \     /   )         :
           `'q'`   ( \       /
             (        \     /
              )        `'q'`
             (           )
              )         (
                        )
                ''')
                print("You won the tresure. Well done.")
            else:
                print(
                    "You have chosen the wrong door and fell into fire. Better luck next time.")
        else:
            print("You lost. A crocodile is in the lake and have eaten you.")
    else:
        print("You lost. You fell into a hole.")
