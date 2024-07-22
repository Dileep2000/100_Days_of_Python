"""
    Tip Calculator is a simple program that will calculate the amount to be paid by each person after tipping certain percentage of the the total amount.

    This is just to understand different data types, type converstion, mathematical operations and string formating using f string.

    Further more we can also use this simple program to make a well known app called splitwise where you enter the amount and it will automatically divide the amount with each person.

"""
if __name__ == "__main__":
    print("Welcome to tip calculator!")
    bill = float(input("What was the total bill? $"))
    tip_perc = int(
        input("How much tip would tou like to give? 10%, 12% or 15%? "))
    no_of_people = int(input("How many people to split the bill? "))
    each_person_bill = round((bill + (bill * tip_perc / 100))/no_of_people, 2)
    print(f"Each person should pay: ${each_person_bill}")
