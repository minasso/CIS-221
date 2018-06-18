from tkinter import * # Import tkinter
    
class LoanCalculator:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Loan Calculator") # Set title
        
        Label(window, text = "Annual Interest Rate").grid(row = 1, 
            column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2, 
            column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 3, 
            column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 4, 
            column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 5, 
            column = 1, sticky = W)
        
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, 
            justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, 
            justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, 
            justify = RIGHT).grid(row = 3, column = 2)

        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable = 
            self.monthlyPaymentVar).grid(row = 4, column = 2, 
                sticky = E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable = 
            self.totalPaymentVar).grid(row = 5, 
                column = 2, sticky = E)

        btComputePayment = Button(window, text = "Compute Payment", 
            command = self.computePayment).grid(
                row = 6, column = 2, sticky = E)
        btSaveLoanInfo = Button(window, text = "Save Loan to File", 
            command = self.saveLoan).grid(
                row = 6, column = 3, sticky = E)
        btAmortization = Button(window, text = "Compute Amortization Schedule", 
            command = self.displayTable).grid(
                row = 6, column = 4, sticky = E)

        # text = Text(window)
        # text.insert(INSERT, "Hello.....")
        # text.grid(row=8,column=1,sticky=W)

        window.mainloop() # Create an event loop

    def displayTable(self):
        import locale
        locale.setlocale( locale.LC_ALL, '' )
        balance = float(self.loanAmountVar.get())
        # print(format("Payment #", "<15s"), format("Interest", "<15s"), format("Principal Pmt", "<15s"), format("Remaining Prin", "<15s"))
        print("Payment #\tInterest\tPrincipal Pmt\tRemaining Prin")
        for i in range(1, int(self.numberOfYearsVar.get()) * 12 + 1):
            interest = float(self.annualInterestRateVar.get())/1200 * balance
            # print(type(interest))
            principal = float(self.monthlyPaymentVar.get()) - interest
            balance = balance - principal
            # print(format(i, "<15d"), format(interest, "<15.2f"), format(principal, "<15.2f"), format(balance, "<15.2f"))
            print(i,locale.currency(interest),'\t',locale.currency(principal),'\t',locale.currency(balance))

    def getMonthlyPayment(self,
        loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1
        - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;

    def computePayment(self):
        try:
            monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), 
            float(self.annualInterestRateVar.get()) / 1200, 
            int(self.numberOfYearsVar.get()))
            self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
            totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
                * int(self.numberOfYearsVar.get())
            self.totalPaymentVar.set(format(totalPayment, '10.2f'))

        except:
            #need to make dialog box for error
            print('error')
            from tkinter import messagebox
            messagebox.showerror("Calculation Error", "Please make sure to enter numeric values for interest rate, years, and loan amount")
    
    def saveLoan(self):
            # from tkinter import messagebox
            # messagebox.showinfo('Loan Recipient','Enter the name of the loan recipient')
            from tkinter import simpledialog
            loanRecipientVar = simpledialog.askstring("Loan Recipient", "Enter the name of the loan recipient")
            with open('{} loan document.txt'.format(loanRecipientVar),'w') as wf:
                wf.write('\t\t\t')
                wf.write('Loan Document for {}'.format(loanRecipientVar))
                wf.write('\t\t\t')
                wf.write('\n')
                wf.write('\t\t\t')
                wf.write('----------------------------')
                wf.write('\n')
                wf.write("Loan Amount: ${:6.2f}".format(float(self.loanAmountVar.get())))
                wf.write('\t')
                wf.write("Interest rate: {}%".format(self.annualInterestRateVar.get()))
                wf.write('\t')
                wf.write("Nbr Years: {}".format(self.numberOfYearsVar.get()))
                wf.write('\n')
                wf.write("Monthly Payment: ${:6.2f}".format(float(self.monthlyPaymentVar.get())))
                wf.write('\t')
                wf.write("Total Payment: ${:6.2f}".format(float(self.totalPaymentVar.get())))
                wf.write('\n')
                wf.write('\n')
                wf.write("Amortization Schedule")

LoanCalculator()  