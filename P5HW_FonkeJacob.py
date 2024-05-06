#Jacob Fonke
#4/17/24
#P5HW Math Quiz
import random
def opt_one():
    num_guess = 0
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    opt_1_ans = num_1 + num_2
    print(f"Find the sum of {num_1} + {num_2}")
    ans_1 = int(input("Enter answer: "))
    num_guess = num_guess + 1
    while ans_1 != opt_1_ans:
        if ans_1 < opt_1_ans:
            print("Sorry, guess is too low.")
            num_guess = num_guess + 1
        if ans_1 > opt_1_ans:
            print("Sorry, guess is too high.")
            num_guess = num_guess + 1
        ans_1 = int(input("Enter answer: "))
        
    print(f"Congratulations! Your answer is correct.")
    print("Number of guesses:", num_guess)


def opt_two():
    num_guess = 0
    num_3 = random.randint(100, 200)
    num_4 = random.randint(1, 99)
    opt_2_ans = num_3 - num_4
    print(f"Find the difference of {num_3} - {num_4}")
    num_guess = num_guess + 1
    ans_2 = int(input("Enter answer: "))
    while ans_2 != opt_2_ans:
        if ans_2 < opt_2_ans:
            print("Sorry, guess is too low.")
            num_guess = num_guess + 1
        if ans_2 > opt_2_ans:
            print("Sorry, guess is too high.")
            num_guess = num_guess + 1
        ans_2 = int(input("Enter answer: "))
        
    print(f"Congratulations! Your answer is correct.")
    print("Number of guesses: ", num_guess)






def menu():
    print("Main Menu")
    print("-------------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()
    option = " "
    while option != "3":
        if option == "1":
            opt_one()
        elif option == "2":
            opt_two()    

        option = input("Please choose one of the menu options: ")



def main():
    #Display main menu
    print("Welcome to Math Quiz")
    print()
    print()
    menu()
    

    

    



#Call the main
main()
print("Thank you for playing...")
print("Bye!!")
