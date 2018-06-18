def main():
    input_var = menu()  
    if input_var == 'r':
        print('you selected {} '.format(input_var))
        names,wages,hours = read_employees()
    elif input_var == 'p':
        print('you selected {} '.format(input_var))
    elif input_var == 'd':
        print('you selected {} '.format(input_var))
        display_by_name()
    elif input_var == 'h':
        print('you selected {} '.format(input_var))
    elif input_var == 'l':
        print('you selected {} '.format(input_var))
    elif input_var == 'q':
        print('you selected {} '.format(input_var))
    else:
        print('Error')

def menu():
    #remember to put error msg if someone chooses something other than r at first
    #make into multi line string
    input_var = input('Pick a letter ')
    return input_var

def read_employees(filename='empwages.txt'):
    names=[]
    wages=[]
    hours=[]
    filename = input('Please enter the file name:')
    try:
        with open(filename,'r') as rf:
            for line in rf.readlines():
                lst = line.strip().split('\t')
                names.append(lst[0])
                wages.append(lst[1])  
                hours.append(float(lst[2])+float(lst[3])+float(lst[4])+float(lst[5])+float(lst[6]))
            print(names)
            print(wages)
            print(hours)
            return(names,wages,hours)
            print('File has been read')       
    except:
        print('Error reading file {} '.format(filename))
    main() 

def display_by_name():
    name = input('enter name ')
    ind = names.index(name)
    w = wages[ind]
    h = hours[ind]
    print(name)
    print(w)
    print(h)    

main()

def printPayroll():
    if not names:
        print(' Employee data has not been read ')
        print(' Please read the file before making this choice ')
    else:
        totalPayroll = 0
        print('\nName\tHours\tPay')
        print('-----\t-----\t-----')
        
# comput the pay for each employee and print the report

pay = hoursWorked[i]*wages[i]
print names[i],"\t",hoursWorked[i],"\t$",pay
totalPayroll = totalPayroll + pay
print("\nTotal payroll = $",totalPayroll)

#max or min total pay for week

def find_HighLow_PaidEmployee(highlow_choice):
    # display error if the lists are empty
    if not names:
        print("Employee data has not been read")
        print("Please read the file before making this choice")
    else:
        # check if the user wants high or low pay
        if highlow_choice == 'h':
            # set the highest as first element in list
            highestName = ""
            highest Wage = wages[0]*hoursWorked[0]
            # iterate the list
            for i in range(0,len(names)):
                # update the highestwage if a higher pay is found
                pay = wages[i]*hoursWorked[i]
                if pay >= highestWage:
                    highestName = names[i]
                    highestWage = pay
            #print the highest earned person
            print highestName,"earned $",highestWage

    # else if for low pay
    elif highlow_choice == "l"
        # set the lowest as first element in the list
        lowestName = ""
        lowestWage = wages[0]*hoursWorked[0]
        lowestWage = wages[0]
        #NEED TO FINISH








    
        







