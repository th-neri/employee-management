import database

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
                print("4. Update employee informations")
                print("5. Delete employee")
                print("6. Go back")

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
                        position = employee[3]
                        salary = employee[4]
                        entry_date = employee[5]

                        print(f'\nID NUMBER: {employee_id}')
                        print("-" * employee_id)
                        print(f'NAME: {name} | EMAIL: {email} | POSITION: {position} | SALARY: {salary} | ENTRY DATE: {entry_date}')

                elif choice == "2":
                    print("\n---REGISTER EMPLOYEE---")

                    try:
                        employee_name = input("Write the employee name: ")
                        email = input("Write the employee email: ")
                        position = input("Write the employee position: ")
                        salary = float(input("Write the employee salary: ").strip())
                        entry_date = input("Entry date(YYYY-MM-DD): ").strip()
                    except ValueError:
                        print("\nInvalid salary input.")
                        continue

                    if not employee_name or not email or not position or not entry_date:
                        print("\nAll the fields have to be filled.")
                        continue

                    if salary <= 0:
                        print("\nSalary must be greater than 0.")
                        continue

                    if not "@" in email:
                        print("\nInvalid email.")
                        continue

                    database.add_employee(connection, employee_name, email, position, salary, entry_date)
                elif choice == "3":
                    pass
                elif choice == "4":
                    while True:
                        print("\n---UPDATE EMPLOYEE INFORMATIONS OPTIONS---")
                        print("1. Update employee name")
                        print("2. Update employee email")
                        print("3. Update employee position")
                        print("4. Update employee salary")
                        print("5. Go back")

                        choice = input("Enter with your choice using a number: ").strip()

                        if choice == "1":
                            print("\n---UPDATE EMPLOYEE NAME---")

                            try:
                                employee_id = int(input("Enter the employee ID you want to change the name: "))
                            except ValueError:
                                print("\nInvalid input.")
                                continue

                            if not database.get_employee(connection, employee_id):
                                print("\nID not found. Try a valid ID number.")
                                continue

                            employee_name = input("Update the name of the employee: ")

                            if not employee_name:
                                print("\nYou have to fill the field.")
                                continue

                            confirm = input("Are you sure you want to update the employee name? (Y/N): ").strip().lower()
                            
                            if confirm == "n":
                                print("\nCancelled.")
                                continue
                            elif confirm == "y":
                                database.update_employee_name(connection, employee_id, employee_name)
                                print("\nEmployee name changed succesfully!")
                            else:
                                print("\nInvalid input. Use Y or N.")
                                continue
                        elif choice == "2":
                            pass
                        elif choice == "3":
                            pass
                        elif choice == "4":
                            pass
                        elif choice == "5":
                            print("Going back to the main page...")
                            break
                        else:
                            print("\nInvalid number.")
                            continue
                elif choice == "5":
                    pass
                elif choice == "6":
                    print("\nGoing back to the main page...\n")
                    break
                else:
                    print("\nInvalid number.")
                    continue
        elif choice == "2":
            pass
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