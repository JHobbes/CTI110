#Jacob Fonke
#2/21/24
#P2HW1
#Travel Expenses

'''Ask user to enter their budget
Ask user to enter travel destination
Ask user for amount they will spend on gas
Ask user for amount they will spend on accommodation
Ask user for amount they will spend on food
Add expenses
Subtract expenses from budget
Display results'''

print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
dest = input("Enter your travel destination: ")
print()
gas_cost = float(input("How much do you think you will spend on gas? "))
print()
hotel_cost = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food_cost = float(input("Last, how much do you need for food? "))
print()
print("----------Travel Expenses----------")
print("Location: ", dest)
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas_cost:.2f}")
print(f"Accomodation: ${hotel_cost:.2f}")
print(f"Food: ${food_cost:.2f}")
print("-----------------------------------")
print()
print()

remaining_bal = budget - gas_cost - hotel_cost - food_cost
print(f"Remaining Balance:${remaining_bal:.2f}")
