def main():
    input_var = menu()  
    if input_var == 'r':
        print('you selected {}'.format(input_var))
        names,wages,hours = read_employees()
    elif input_var == 'p':
        print('you selected {}'.format(input_var))
    elif input_var == 'd':
        print('you selected {}'.format(input_var))
        display_by_name()
    elif input_var == 'h':
        print('you selected {}'.format(input_var))
    elif input_var == 'l':
        print('you selected {}'.format(input_var))
    elif input_var == 'q':
        print('you selected {}'.format(input_var))
    else:
        print('Error')

def menu():
    #remember to put error msg if someone chooses something other than r at first
    #make into multi line string
    input_var = input('Pick letter')
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
        print('Error reading file {}'.format(filename))
    main() 

def display_by_name():
    name = input('enter name')
    ind = names.index(name)
    w = wages[ind]
    h = hours[ind]
    print(name)
    print(w)
    print(h)    

main()
