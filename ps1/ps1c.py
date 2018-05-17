starting_annual_salary = float(input("Enter the starting annual salary: "))

semi_annual_raise = .07
r = .04
portion_down_payment = .25
total_cost = 1000000
target_months = 36
current_savings = 0.0
down_payment = total_cost * portion_down_payment
lower = down_payment - 100
upper = down_payment + 100

month = 0
step = 1

annual_salary = starting_annual_salary
while current_savings < total_cost * portion_down_payment:
    # print(current_savings)
    # print(savings_rate)
    monthly_roi = current_savings * r / 12.0
    current_savings += monthly_roi + 1.0 * annual_salary / 12.0
    month += 1
    # print(month)
    # print(monthly_roi)
    # print(current_savings)
    if month % 6 == 0:
        annual_salary += semi_annual_raise * annual_salary
    else:
        continue
if month <= target_months:
    pass
else:
    print("It is not possible to pay the down payment in three years.")
    exit()

start = 0
stop = 10000
bisect = (start + stop)/2
savings_rate = bisect/10000
current_savings = 0.0
month = 0
while month != target_months or current_savings >= upper or current_savings <= lower :
    annual_salary = starting_annual_salary
    current_savings = 0.0
    month = 0
    # print("Step", step)
    while current_savings < total_cost*portion_down_payment:
        # print(current_savings)
        # print(savings_rate)
        monthly_roi = current_savings*r/12.0
        current_savings += monthly_roi + savings_rate * annual_salary/12.0
        month += 1
        # print(month)
        # print(monthly_roi)
        # print(current_savings)
        if month % 6 == 0:
            annual_salary += semi_annual_raise*annual_salary
        else:
            continue
    if month == target_months:
        if lower <= current_savings <= upper:
            print("Best savings rate:", savings_rate)
        elif current_savings <= lower:
            start = savings_rate * 10000
            stop = stop
            bisect = (start + stop) / 2
            savings_rate = bisect / 10000
            # print(month)
            # print(savings_rate)
            step += 1
        else:
            start = start
            stop = savings_rate * 10000
            bisect = (start + stop) / 2
            savings_rate = bisect / 10000
            # print(month)
            # print(savings_rate)
            step += 1
    elif month > target_months:
        start = savings_rate * 10000
        stop = stop
        bisect = (start + stop)/2
        savings_rate = bisect/10000
        # print(month)
        # print(savings_rate)
        step += 1
    else:
        start = start
        stop = savings_rate * 10000
        bisect = (start + stop)/2
        savings_rate = bisect/10000
        # print(month)
        # print(savings_rate)
        step += 1
print("Steps in bisection search:", step)
