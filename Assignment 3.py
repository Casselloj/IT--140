hours_worked = float(input("Enter the number of hours worked: "))

if hours_worked <= 40:
    regular_pay = hours_worked * 20
    overtime_pay = 0
else:
    regular_pay = 40 * 20
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * 30
total_pay = regular_pay + overtime_pay
print("The weekly paycheck is $", total_pay)

input("Press enter to exit")
