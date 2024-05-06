#Jacob Fonke
#3/14/24
#P2HW2
#Grade Averages

'''Ask user to imput their grades for Modules 1-6
Store inputs in a list
Display from the list:
lowest grade
highest grade
sum of grades
grades' average'''

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
print()
print("----------Results----------")
print(f"Lowest Grade: {min(grades):.2f}")
print(f"Highest Grade: {max(grades):.2f}")
print(f"Sum of Grades: {sum(grades):.2f}")
print(f"Average: {sum(grades)/len(grades):.2f}")
