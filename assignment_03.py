"""
Q1: Write a program that prompts the user for a meal: breakfast, lunch,
or dinner. Then using if statements and else statements print the user a
message recommending a meal. For example, if the meal was breakfast, you could
say something like, “How about some bacon and eggs?” The user may enter
something else in, but you only have to respond to breakfast, lunch, or dinner.
"""

# Prompt the user for a meal
meal = input("Pick a meal to see its menu: | breakfast | lunch | dinner | : ")

# Check for meal type and print the menu
if meal == "breakfast":
    print("| bacon | eggs | pancakes | waffles | ")
elif meal == "lunch":
    print("| turkey sandwich | soup | burger | ")
elif meal == "dinner":
    print("| tacos | pizza | seafood | chicken | ")
else:
    print("Invalid Meal Selection. Please try again!")


"""
Q2: The mailroom has asked you to design a simple payroll program that 
calculates a student employee’s gross pay, including any overtime wages. If 
any employee works over 20 hours in a week, the mailroom pays them 1.5 times 
their regular hourly pay rate for all hours over 20. You should take in the 
user’s input for the number of hours worked, and their rate of pay.
"""

# Function to calculate total, regular and overtime pay
def calculate_pay(hours_worked, pay_rate):
    if hours_worked > 20:
        overtime_hours = hours_worked - 20
        regular_pay = 20 * pay_rate
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        total_pay = regular_pay + overtime_pay
    else:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
        total_pay = hours_worked * pay_rate
    return regular_pay, overtime_pay, total_pay

# Prompt the user for hours worked and pay rate
hours_worked = int(input("Enter the total number of hours worked in 1 week: "))
pay_rate = float(input("Enter the hourly pay rate: "))

regular_pay, overtime_pay, total_pay = calculate_pay(hours_worked, pay_rate)

print("Regular Pay: $", regular_pay)
print("Overtime Pay: $", overtime_pay)
print("Total Pay: $", total_pay)
print("Estimated Yearly Salary (52 weeks): $" + str(total_pay * 52))

"""
Q3: Write a function named times_ten. The function should accept an argument 
and display the product of its argument multiplied times 10.
"""

# Function to multiply a number by 10
def times_ten(number):
    product = number * 10
    return (product)

#
number = int(input("Enter the number to multiply by 10: "))

product = times_ten(number)

print("The product of", number, "and 10 is", product)

"""
Q4: Find the errors, debug the program, and then execute to show the output.
"""

def main():
    calories1 = int(input("How many calories are in the first food? "))
    calories2 = int(input("How many calories are in the second food? "))
    show_calories(calories1, calories2)


def show_calories(calories1, calories2):
    total_calories = calories1 + calories2
    print("The total calories you ate today", format(total_calories, '.2f'))

main()


"""
Q5: Write a program that uses any loop (while or for) that calculates the 
total of the following series of numbers: 1/30 + 2/29 + 3/28 ............. + 
30/1
"""

# Initialize the numerator and denominator
numerator = 1
denominator = 30

# Initialize the total
total = 0

for i in range(30):
    total = total + (numerator / denominator)
    numerator = numerator + 1
    denominator = denominator - 1

print("The total for this loop is: ", total)

"""
Q6: Write a function that computes the area of a triangle given its base and 
height. The formula for an area of a triangle is:
AREA = 1/2 * BASE * HEIGHT

"""
# Function to calculate the area of a triangle
def triangle_area(base, height):
    area = 0.5 * base * height
    return area

# Prompt the user for the base and height of the triangle
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))

area = triangle_area(base, height)

print("The area of the triangle is", area)


