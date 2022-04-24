def interest():
    while True:
        # initialize first value
        p = int(input("Enter the starting principal, 0 to quit: "))
        # the program stops if p <= 0. If not, compute the result.
        if p <= 0:
            print("program existing...", end="\n")
            break
        r = float(input("Enter the annual interest rate:  "))
        n = int(input("How many times the interest compound in a year? "))
        t = int(input("For how many years will the account earn interest? "))
        total = p * (1 + float(r / 100) / n) ** (n * t)
        interest = total - p
        print("At the end of ", "{:.1f}".format(n), "years you will have ", "{:,.2f}".format(total),
              "with interest earned", "{:.2f}".format(interest))
