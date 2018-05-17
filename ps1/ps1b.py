annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04

month = 0
while current_savings < total_cost*portion_down_payment:
    monthly_roi = current_savings*r/12
    current_savings = current_savings + monthly_roi + portion_saved * annual_salary/12
    month += 1
    if month % 6 == 0:
        annual_salary += semi_annual_raise*annual_salary
    else:
        continue
print("Number of months:", month)

# a = int(input("Enter value of a:"))
# b = int(input("Enter value of b:"))
# while a > b:
#     print("a > b")
#     b += 2
# if a - b == 0:
#     print("a - b = 0")
# else:
#     print("OK")
