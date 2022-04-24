def mortgage():
        while True:
            # initialize first value
            loanAmount = int(input("Enter the loan amount, 0 to quit: "))
            # the program stops if p <= 0. If not, compute the result.
            if loanAmount <= 0:
                print("program existing...", end="\n")
                break
            interestRate = float(input("Enter the loan interest rate:  "))
            loanTerm = int(input("Enter the loan term (number of years): "))

            monthlyRate = (interestRate / 100) / 12
            numPayments = loanTerm * 12
            monthlyPayment = loanAmount * monthlyRate \
                             * pow((1 + monthlyRate), numPayments) \
                             / (pow((1 + monthlyRate), numPayments) - 1)
            totalPayment = monthlyPayment * (loanTerm * 12)
            interestPaid = totalPayment - loanAmount


            print("For the loan amount of $ ", "{:,.2f}".format(loanAmount), " for ", loanTerm, " years with interest rate of ",  "{:,.2f}".format(interestRate))
            print("The monthly payment is $ ", "{:,.2f}".format(monthlyPayment))
            print("Total amount paid is $ ", "{:,.2f}".format(totalPayment))
            print("Total interest paid is $ ", "{:,.2f}".format(interestPaid))



