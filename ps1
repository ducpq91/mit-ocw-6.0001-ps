total_cost = float(input("Enter the cost of your dream home:"))
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04

month = 0
while current_savings < total_cost*portion_down_payment:
    monthly_roi = current_savings*r/12
    current_savings = current_savings + monthly_roi + portion_saved * annual_salary/12
    month += 1
print("Number of months:", month)
