from tkinter import * 

class LoanCalculator:
    
    def __init__(self):
        window = Tk() 
        window.title("Loan Calculator")
        # Labels
        Label(window, text = "Annual Interest Rate").grid(row = 1, 
            column = 2, sticky = E)
        Label(window, text = "Number of Years").grid(row = 2, 
            column = 2, sticky = E)
        Label(window, text = "Loan Amount").grid(row = 3, 
            column = 2, sticky = E)
        Label(window, text = "Monthly Payment").grid(row = 4, 
            column = 2, sticky = E)
        Label(window, text = "Total Payment").grid(row = 5, 
            column = 2, sticky = E)
        # Variables
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, 
            justify = RIGHT).grid(row = 1, column = 3, sticky = W)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, 
            justify = RIGHT).grid(row = 2, column = 3, sticky = W)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar,
             justify = RIGHT).grid(row = 3, column = 3, sticky = W)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable = 
            self.monthlyPaymentVar).grid(row = 4, column = 3,sticky=W)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable = 
            self.totalPaymentVar).grid(row = 5, column = 3,sticky=W)
        # Text Box Widget
        self.text = Text(window)
        self.text.grid(row=8,column=1,columnspan=4) 
        # Buttons
        btComputePayment = Button(window, text = "Compute Payment", 
            command = self.computePayment).grid(
                row = 6, column = 2, sticky = E)
        btSaveLoanInfo = Button(window, text = "Save Loan to File", 
            command = self.saveLoan).grid(
                row = 6, column = 3,sticky=W)
        # Loop
        window.mainloop() # Create an event loop

    def saveLoan(self):
        '''
        This function saves loan information to a file when a button is clicked.
        '''
        from tkinter import simpledialog
        # Ask for the loan recipient's name to use for name of file
        loanRecipientVar = simpledialog.askstring("Loan Recipient", "Enter the name of the loan recipient")
        with open('{} loan document.txt'.format(loanRecipientVar),'w') as wf:
            wf.write('\t\t\tLoan Document for {}\t\t\t\n\t\t\t'.format(loanRecipientVar))
            wf.write('----------------------------\n')
            wf.write("Loan Amount: ${:6.2f}\t".format(float(self.loanAmountVar.get())))
            wf.write("Interest rate: {}%\t".format(self.annualInterestRateVar.get()))
            wf.write("Nbr Years: {}\n".format(self.numberOfYearsVar.get()))
            wf.write("Monthly Payment: ${:6.2f}\t".format(float(self.monthlyPaymentVar.get())))
            wf.write("Total Payment: ${:6.2f}\n\n".format(float(self.totalPaymentVar.get())))
            # Retrieve loan info from text box widget
            loan_info = self.text.get("1.0",END)
            wf.write(loan_info)
            
    def getMonthlyPayment(self,
        loanAmount, monthlyInterestRate, numberOfYears):
        '''
        This function calculates the monthly payment of the loan to be fed into the compute payment
        function.
        '''
        monthlyPayment = loanAmount * monthlyInterestRate / (1
        - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;
    
    def computePayment(self):
        '''
        This function computes the monthly payment and total payment for  loan when a button
        is pressed. It also calls the display table function in order to output the amortization 
        schedule to the screen It also writes an error message if inputs are not numerical.
        '''
        try:
            # Calculate monthly payment
            monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), 
            float(self.annualInterestRateVar.get()) / 1200, 
            int(self.numberOfYearsVar.get()))
            self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
            # Calculate total payment
            totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberOfYearsVar.get())
            # Set total payment variable
            self.totalPaymentVar.set(format(totalPayment, '10.2f'))
            # Call display table to output amortization schedule
            self.displayTable()
        except:
            # Error msg
            from tkinter import messagebox
            messagebox.showerror("Calculation Error",
            "Please make sure to enter numeric values for interest rate, years, and loan amount")       
               
    def displayTable(self):
        '''
        This function displays the amortization schedule for a loan in a text box widget.
        '''
        # Write text into text box widget
        self.text.insert(INSERT, "Amortization Schedule\n")
        # Import locale to deal with currency formatting
        import locale
        locale.setlocale( locale.LC_ALL, '' )
        balance = float(self.loanAmountVar.get())
        # Use string formatting to match the width of the 80 character text box widget
        output_str = '{:<20s}{:<20s}{:<20s}{:<20s}'.format("Payment #","Interest","Principal Pmt","Remaining Prin")
        self.text.insert(END,output_str)
        # Calculate each line of the amortization schedule
        for i in range(1, int(self.numberOfYearsVar.get()) * 12 + 1):
            interest = float(self.annualInterestRateVar.get())/1200 * balance
            principal = float(self.monthlyPaymentVar.get()) - interest
            balance = balance - principal
            # Write each line of amortization schedule to the text box widget
            self.text.insert(END,'{:<20d}{:<20s}{:<20s}{:<20s}'.format(i,locale.currency(interest,grouping=True),
            locale.currency(principal,grouping=True),locale.currency(balance,grouping=True)))        

LoanCalculator()  