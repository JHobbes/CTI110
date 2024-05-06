#Jacob Fonke
#3/19/24
#P3HW1-Debugging code

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
grade_tot = sum(grades)
grade_count = len(grades)
# TO DO: determine lowest, highest , sum and average for grades
print()
print("------------Results-----------")
print(f"Lowest Grade:      {min(grades):.2f}")
print(f"Highest Grade:     {max(grades):.2f}")
print(f"Sum of Grades:     {grade_tot:.2f}")
print(f"Average:           {grade_tot/grade_count:.2f}")
print("-------------------------------------")
avg = grade_tot/grade_count
# determine letter grade for average


if avg >= 90:
    print("Your grade is: A")
elif avg >= 80:
    print("Your grade is: B")
elif avg >= 70:
    print("Your grade is: C")
elif avg >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")






