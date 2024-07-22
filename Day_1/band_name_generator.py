"""
    Band name Genrator is a program that uses the city that you have lived in and your pet's name to generate possible band name.
    It helps you to understand how input, print and string concatination works in python.
    It is very simple and easy project to start with.
    There are many several different things to upgrade this project.
    You can calculate the number of ways to create a band name by asking user different questions.
    You can print some combinations of band names. Like reversing them and so many combinations.
"""
if __name__ == "__main__":
    print("Welcome to Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    print("Your band name could be "+city+" "+pet_name)
