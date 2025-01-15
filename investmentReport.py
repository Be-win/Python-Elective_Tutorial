def investment_report(deposit_amount, interest, years):
    for i in range(1, years + 1):
        opening_bal = deposit_amount
        interest_amount = deposit_amount * (interest / 100)
        deposit_amount += interest_amount
        print("%-6d %-16.2f %-10.2f %-16.2f" % (i, opening_bal, interest_amount, deposit_amount))


deposit = float(input("Enter the initial deposit amount: "))
interest_rate = float(input("Enter the interest rate: "))
year = int(input("Enter the number of years to be calculated: "))

print("%-6s %-16s %-10s %-16s" % ("Year","Opening_Balance", "Interest", "Closing_Balance"))

investment_report(deposit, interest_rate, year)