import database
from datetime import datetime

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while True:
        print("---EMPLOYEE MANAGEMENT SYSTEM---")
        print("1. Employee options")
        print("2. Department options")
        print("3. Reports")
        print("4. Exit")

        choice = input("Enter with your choice using a number: ").strip()

        if choice == "1":
            while True:
                print("\n---EMPLOYEE OPTIONS---")
                print("1. View employees")
                print("2. Register employee")
                print("3. Search employee")
                print("4. Change employee informations")
                print("5. Go back")

                choice = input("Enter with your choice using a number: ").strip()

                if choice == "1":
                    print("\n---EMPLOYEES LIST---")

                    employees = database.show_employees(connection)

                    if not employees:
                        print("\nNo employees available.")
                        continue

                    for employee in employees:
                        employee_id = employee[0]
                        name = employee[1]
                        email = employee[2]
                        department_name = employee[3]
                        position = employee[4]
                        salary = employee[5]
                        entry_date = employee[6]

                        print(f'\nID NUMBER: {employee_id}')
                        print("-" * 13)
                        print(f'DEPARTMENT: {department_name} | NAME: {name} | EMAIL: {email} | POSITION: {position} | SALARY: ${salary:,.2f} | ENTRY DATE: {entry_date}')

                elif choice == "2":
                    print("\n---REGISTER EMPLOYEE---")

                    try:
                        employee_name = input("Write the employee name: ").strip()
                        email = input("Write the employee email: ").strip()
                        department_id = int(input("Write the department ID: "))
                        position = input("Write the employee position: ").strip()
                        salary = float(input("Write the employee salary: ").strip())
                    except ValueError:
                        print("\nInvalid input. Use numbers for the department ID or salary.")
                        continue

                    try:
                        entry_date = input("Entry date(YYYY-MM-DD): ").strip()
                        datetime.strptime(entry_date, "%Y-%m-%d")
                    except ValueError:
                        print("\nInvalid date format. Use YYYY-MM-DD.")
                        continue

                    if not employee_name or not email or not position or not entry_date:
                        print("\nAll the fields have to be filled.")
                        continue

                    if not database.get_department(connection, department_id):
                        print("\nID not found. Try a valid ID number.")
                        continue

                    if not "@" in email or "." not in email:
                        print("\nInvalid email address.")
                        continue

                    if salary <= 0:
                        print("\nSalary must be greater than 0.")
                        continue

                    database.add_employee(connection, employee_name, email, department_id, position, salary, entry_date)
                    print("\nEmployee data added successfully!")

                elif choice == "3":
                    while True:
                        print("\n---SEARCH OPTIONS---")
                        print("1. Search by ID")
                        print("2. Search by name")
                        print("3. Search by email")
                        print("4. Go back")

                        choice = input("Enter with your choice using a number: ").strip()

                        if choice == "1":
                            print("\n---SEARCH EMPLOYEE BY ID---")

                            try:
                                employee_id = int(input("Enter the employee ID you searching for: "))
                            except ValueError:
                                print("\nInvalid input.")
                                continue

                            if not database.get_employee(connection, employee_id):
                                print("\nID not found. Try a valid ID number.")
                                continue

                            employee = database.search_employee_by_id(connection, employee_id)

                            employee_name, email, department_name, position, salary, entry_date = employee

                            print(f'\nDEPARTMENT: {department_name} | NAME: {employee_name} | EMAIL: {email} | POSITION: {position} | SALARY: ${salary:,.2f} | ENTRY DATE: {entry_date}')
                        
                        elif choice == "2":
                            print("\n---SEARCH EMPLOYEE BY NAME---")

                            employee_name = input("Enter with name you searching for: ").strip()

                            employees = database.search_employee_by_name(connection, employee_name)

                            if not employees:
                                print("\nNo employees found.")
                                continue

                            for employee in employees:
                                employee_name, email, department_name, position, salary, entry_date = employee

                                print(f'\nNAME: {employee_name} | DEPARTMENT: {department_name} | EMAIL: {email} | POSITION: {position} | SALARY: ${salary:,.2f} | ENTRY DATE: {entry_date}')
                        elif choice == "3":
                            print("\n---SEARCH EMPLOYEE BY EMAIL---")

                            email = input("Enter with the email you searching for: ").strip()

                            employee = database.search_employee_by_email(connection, email)

                            if not employee:
                                print("\nEmail not found.")
                                continue

                            employee_name, email, department_name, position, salary, entry_date = employee

                            print(f'\nDEPARTMENT: {department_name} | NAME: {employee_name} | EMAIL: {email} | POSITION: {position} | SALARY: ${salary:,.2f} | ENTRY DATE: {entry_date}')

                        elif choice == "4":
                            print("\nGoing back to the main page...")
                            break
                        else:
                            print("\nInvalid number.")
                            continue

                elif choice == "4":
                    while True:
                        print("\n---UPDATE EMPLOYEE INFORMATIONS OPTIONS---")
                        print("1. Update employee name")
                        print("2. Update employee email")
                        print("3. Update employee position")
                        print("4. Update employee salary")
                        print("5. Remove employee informations")
                        print("6. Go back")

                        choice = input("Enter with your choice using a number: ").strip()

                        if choice == "1":
                            print("\n---UPDATE EMPLOYEE NAME---")

                            try:
                                employee_id = int(input("Enter the employee ID you want to update the name: "))
                            except ValueError:
                                print("\nInvalid input.")
                                continue

                            if not database.get_employee(connection, employee_id):
                                print("\nID not found. Try a valid ID number.")
                                continue

                            employee_name = input("Update the name of the employee: ").strip()

                            if not employee_name:
                                print("\nYou have to fill the field.")
                                continue

                            confirm = input("Are you sure you want to update the employee name? (Y/N): ").strip().lower()
                            
                            if confirm == "n":
                                print("\nCancelled.")
                                continue
                            elif confirm == "y":
                                database.update_employee_name(connection, employee_id, employee_name)
                                print("\nEmployee name updated succesfully!")
                            else:
                                print("\nInvalid input. Use Y or N.")
                                continue

                        elif choice == "2":
                            print("\n---UPDATE EMPLOYEE EMAIL---")

                            try:
                                employee_id = int(input("Enter the employee ID you want to update the email: "))
                            except ValueError:
                                print("\nInvalid input.")
                                continue

                            if not database.get_employee(connection, employee_id):
                                print("\nID not found. Try a valid ID number.")
                                continue

                            email = input("Update the email of the employee: ").strip()

                            if not email:
                                print("\nYou have to fill the field.")
                                continue

                            if not "@" in email or "." not in email:
                                print("\nInvalid email address.")
                                continue

                            confirm = input("\nAre you sure you want to update the employee email? (Y/N): ").strip().lower()

                            if confirm == "n":
                                print("\nCancelled.")
                                continue
                            elif confirm == "y":
                                database.update_employee_email(connection, employee_id, email)
                                print("\nEmployee email changed successfully!")
                            else:
                                print("\nInvalid input. Use Y or N.")
                                continue

                        elif choice == "3":
                            print("\n---UPDATE EMPLOYEE POSITION---")

                            try:
                                employee_id = int(input("Enter the employee ID you want to update the position: "))
                            except ValueError:
                                print("\nInvalid input.")
                                continue

                            if not database.get_employee(connection, employee_id):
                                print("\nID not found. Try a valid ID number.")
                                continue

                            position = input("Update the position of the employee: ").strip()

                            if not position:
                                print("\nYou have to fill the field.")
                                continue

                            confirm = input("\nAre you sure you want to update the employee position? (Y/N): ").strip().lower()

                            if confirm == "n":
                                print("\nCancelled.")
                                continue
                            elif confirm == "y":
                                database.update_employee_position(connection, employee_id, position)
                                print("\nEmployee position changed successfully!")
                            else:
                                print("\nInvalid input. Use Y or N.")
                                continue

                        elif choice == "4":
                            print("\n---UPDATE EMPLOYEE SALARY---")

                            try:
                                employee_id = int(input("Enter the employee ID you want to update the salary: "))
                            except ValueError:
                                print("\nInvalid input.")
                                continue

                            if not database.get_employee(connection, employee_id):
                                print("\nID not found. Try a valid ID number.")
                                continue

                            try:
                                salary = float(input("Update the salary of the employee: "))
                            except ValueError:
                                print("\nInvalid input. Use numbers for the salary.")
                                continue

                            if not salary:
                                print("\nYou have to fill the field.")
                                continue

                            if salary <= 0:
                                print("\nSalary must be greater than 0.")
                                continue

                            confirm = input("\nAre you sure you want to update the employee salary? (Y/N): ").strip().lower()

                            if confirm == "n":
                                print("\nCancelled.")
                                continue
                            elif confirm == "y":
                                database.update_employee_salary(connection, employee_id, salary)
                                print("\nEmployee salary changed successfully!")
                            else:
                                print("\nInvalid input. Use Y or N.")
                                continue

                        elif choice == "5":
                            print("\n---REMOVE EMPLOYEE INFORMATIONS---")

                            try:
                                employee_id = int(input("Enter the employee ID you want to remove: "))
                            except ValueError:
                                print("\nInvalid input.")
                                continue

                            if not database.get_employee(connection, employee_id):
                                print("\nID not found. Try a valid ID number.")
                                continue

                            confirm = input("\nAre you sure you want to remove the employee informations? (Y/N): ").strip().lower()

                            if confirm == "n":
                                print("\nCancelled.")
                                continue
                            elif confirm == "y":
                                database.delete_employee(connection, employee_id)
                                print("\nEmployee removed successfully!")
                            else:
                                print("\nInvalid input. Use Y or N.")
                                continue 

                        elif choice == "6":
                            print("\nGoing back to the main page...")
                            break
                        else:
                            print("\nInvalid number.")
                            continue
                
                elif choice == "5":
                    print("\nGoing back to the main page...\n")
                    break
                else:
                    print("\nInvalid number.")
                    continue

        elif choice == "2":
            while True:
                print("\n---DEPARTMENT OPTIONS---")
                print("1. View departments")
                print("2. Add departments")
                print("3. Update department name")
                print("4. Remove department")
                print("5. Go back")

                choice = input("Enter with your choice using a number: ").strip()

                if choice == "1":
                    print("\n---DEPARTMENTS LIST---")

                    departments = database.show_departments(connection)

                    if not departments:
                        print("\nNo departments available.")
                        continue

                    for department in departments:
                        department_id = department[0]
                        department_name = department[1]

                        print(f'\nDEPARTMENT ID NUMBER: {department_id}')
                        print("-" * 24)
                        print(f'DEPARTMENT NAME: {department_name}')

                elif choice == "2":
                    print("\n---ADD NEW DEPARTMENT---")

                    department_name = input("Write the new department name: ").strip()

                    if not department_name:
                        print("\nThe field has to be filled.")
                        continue

                    database.add_department(connection, department_name)
                    print("Department added successfully!")

                elif choice == "3":
                    print("\n---UPDATE DEPARTMENT NAME---")

                    departments = database.show_departments(connection)

                    if not departments:
                        print("\nNo departments available.")
                        continue

                    for department in departments:
                        department_id = department[0]
                        department_name = department[1]

                        print(f'\nDEPARTMENT ID NUMBER: {department_id} | DEPARTMENT NAME: {department_name}')
                    
                    try:
                        department_id = int(input("\nEnter the department ID you want to update the name: "))
                    except ValueError:
                        print("\nInvalid input.")
                        continue

                    if not database.get_department(connection, department_id):
                        print("\nID not found. Try a valid ID number.")
                        continue

                    department_name = input("Update the name of the department: ").strip()

                    if not department_name:
                        print("\nYou have to fill the field.")
                        continue

                    confirm = input("\nAre you sure you want to update the department name? (Y/N): ").strip().lower()

                    if confirm == "n":
                        print("\nCancelled.")
                        continue
                    elif confirm == "y":
                        database.update_department_name(connection, department_id, department_name)
                        print("\nDepartment name updated successfully!")
                    else:
                        print("\nInvalid input. Use Y or N.")
                        continue

                elif choice == "4":
                    print("\n---REMOVE DEPARTMENT---")

                    departments = database.show_departments(connection)

                    if not departments:
                        print("\nNo departments available.")
                        continue

                    for department in departments:
                        department_id = department[0]
                        department_name = department[1]

                        print(f'\nDEPARTMENT ID NUMBER: {department_id} | DEPARTMENT NAME: {department_name}')

                    try:
                        department_id = int(input("\nEnter the department ID you want to remove: "))
                    except ValueError:
                        print("\nInvalid input.")
                        continue

                    if not database.get_department(connection, department_id):
                        print("\nID not found. Try a valid ID number.")
                        continue

                    confirm = input("\nAre you sure you want to remove the department? (Y/N): ").strip().lower()

                    if confirm == "n":
                        print("\nCancelled.")
                        continue
                    elif confirm == "y":
                        database.delete_department(connection, department_id)
                        print("\nDepartment removed successfully!")
                    else:
                        print("\nInvalid input. Use Y or N.")
                        continue
                    
                elif choice == "5":
                    print("\nGoing back to the main page...\n")
                    break
                else:
                    print("\nInvalid number.")
                    continue

        elif choice == "3":
            pass

        elif choice == "4":
            print("\nLeaving...\n")
            connection.close()
            break

        else:
            print("\nInvalid number.")
            continue

menu()