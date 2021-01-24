# Program to demonstrate the use of lists and the associated actions.

employees = ['Jane', 'John', 'Ian', 'Billy', 'Padraic', 'Chris', 'Andy', 'Liam' ]

choice = ''

while choice != 'q':

    choice = input("Select [A]dd, [R]emove, [D]isplay, [C]lear, [S]ort or [Q]uit: ").lower()

    if choice == 'a':
        employees.append(input("Enter a new employee: ").title())

    elif choice == 'r':
        who = input("Enter name of employee you wish to remove: ").title()
        if who in employees:
            employees.remove(who)
            print("Employee removed.")
        else:
            print("Employee not found. Try Again.")

    elif choice == 'd':
        print("Employees: ", employees)

    elif choice == 'c':
        confirm = input("WARNING:\nAre you sure you want to clear your list? Y/N: ").lower()
        if confirm == 'y':
            employees.clear()
            print("List cleared.")
        else:
            continue

    elif choice == 's':
        print(sorted(employees))

    elif choice == 'q':
        break

    else:
        print("Invalid option entered.\n")
    
    print()