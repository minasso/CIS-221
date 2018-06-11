def main():
    '''
    This function takes user input and performs the appropriate subroutine.
    '''
    # Declare global variables for the three lists
    global names
    global wages
    global hours
    # Continuous loop for displaying menu
    while True:
        # Calls menu and stores result as input_var
        input_var = menu()
        if input_var == 'r':
            filename = input('Please enter the file name: ')
            read_employees(filename)
        elif input_var == 'p':
            print_payroll()
        elif input_var == 'd':
            name_to_display = input('Choose a name to display: ')
            display_by_name(name_to_display)
        elif input_var == 'h':
            high_low_paid_employee('h')
        elif input_var == 'l':
            high_low_paid_employee('l')
        elif input_var == 'q':
            print('Goodbye')
            return
        else:
            print('Error')

def menu():
    '''
    This function takes an input from the user and returns it to the main function.
    '''
    input_str = '''Menu of choices:
                (r)ead employee data
                (p)rint employee payroll
                (d)isplay an employee by name
                find (h)ighest paid employee
                find (l)owest paid employee
                (q)uit\n''' 
    while True:
        input_var = input(input_str)
        if input_var in ['p','d','h','l']:
            try:
                names
                return input_var
            except NameError:
                # If names is not defined, show error message
                print('Employee data has not been read. \nPlease read file before making this choice.')
                continue
        elif input_var in ['q','r']:
            return input_var
        else:
            # If user gives any other input, show error message
            print('Invalid choice. Please try again')

def read_employees(filename):
    '''
    This function reads in employee data from a file, stores data in 3 separate
    lists (names,wages,hours) and orders data by employee name.
    '''
    # Declare global variables
    global names
    global wages
    global hours
    names = []
    wages = []
    hours = []
    # Empty list to store each line in file
    lst=[]
    try:
        with open(filename,'r') as rf:
            for line in rf.readlines():
                lst.append(line.strip())
        # Sort list by employee name
        lst=sorted(lst)
        # For each line, Split by tab character to get name,wage,etc.
        for elem in lst:
            l = elem.split('\t')
            names.append(l[0])
            wages.append(float(l[1]))  
            hours.append(float(l[2])+float(l[3])+float(l[4])+float(l[5])+float(l[6]))
        print('File has been read')
        return          
    except IndexError:
        # Error msg for file with improper formatting
        print('Bad data in file {}'.format(filename))
        return
    except FileNotFoundError:
        # Error msg for file doesn't exist
        print('Error reading file {}'.format(filename))
        return

def display_by_name(name):
    '''
    This function displays hours, wage, and total pay for a single employee.
    '''
    # Changing input to title case
    name = name.title()
    # Find the index of the selected employee
    ind = names.index(name)
    # Use index to find the employee's wage and hrs
    w = float(wages[ind])
    h = float(hours[ind])
    # Mult wage and hours to find the total pay
    tot = h*w   
    print('{} worked {} hours at ${:6.2f} per hour, and earned ${:6.2f}'.format(name,h,w,tot))

def high_low_paid_employee(var): 
    '''
    This function displays the employee with the highest or lowest total pay.
    '''
    # Use zip to multiply the two lists pairwise
    tot = [a*b for a,b in zip(wages,hours)]
    if var == 'h':
        # Find index of the employee whose total pay equals the max total pay
        ind = tot.index(max(tot))  
    elif var == 'l':
        # Find index of the employee whose total pay equals the max total pay
        ind = tot.index(min(tot))
    else:
        # Error msg for invalid choice
        print('must choose h or l')
    print('{} earned ${:6.2f}'.format(names[ind],tot[ind]))   

def print_payroll():
    '''
    This function prints out the names, hours, and total pay for all employees.
    '''
    # Use zip to multiply the elements in the two lists pairwise
    pay = [(a*b) for a,b in list(zip(wages,hours))]  
    # Format the pay as a string with 2 decimal places
    str_pay = ['${:6.2f}'.format(item) for item in pay]
    # Form tuples for each employee that contains name, hours, and pay
    tuples = list(zip(names,hours,str_pay))
    # Set layout and headers for table
    layout = "{!s:7} {!s:7} {!s:7}"
    headers = ["Name","Hours","Pay"]
    # Use '*'' for tuple unpacking to return just the items of the list
    print (layout.format(*headers))
    print('----\t-----\t---')
    for item in tuples:
        print (layout.format(*item))
    total = sum(pay)
    print('\n')
    print('Total payroll = ${}'.format(total))

main()
