def get_income_tax(income):
    tax = 0

    tax_slabs = [
        (300000, 0.00),
        (700000, 0.05),
        (1000000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float('inf'), 0.30),
    ]

    prev_limit = 0

    for limit, rate in tax_slabs :
        if income > limit :
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (income - prev_limit) * rate
            break

    return f"₹{tax:,.2f}"

annual_income = float(input("Enter income: "))
total_tax = get_income_tax(annual_income)
print("Income Tax is ", total_tax)