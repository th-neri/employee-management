import sqlite3

def connect():
    connection = sqlite3.connect("employee_management.db")
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def create_tables(connection):
    with connection:
        connection.execute("""
                        CREATE TABLE IF NOT EXISTS employees (
                            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            employee_name TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            position TEXT NOT NULL,
                            salary REAL NOT NULL,
                            entry_date TEXT NOT NULL
                       )
                       """)
    
        connection.execute("""
                        CREATE TABLE IF NOT EXISTS departments (
                            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            department_name TEXT NOT NULL
                       )
                       """)
    
        connection.execute("""
                        CREATE TABLE IF NOT EXISTS employee_department (
                            employee_id INTEGER,
                            department_id INTEGER,
                            FOREIGN KEY(employee_id) REFERENCES employees(employee_id),
                            FOREIGN KEY(department_id) REFERENCES departments(department_id)
                       )
                       """)


def add_departmwent(connection, department_name):
    with connection:
        connection.execute("INSERT INTO departments(department_name) VALUES(?); ", (department_name,))


def add_employee(connection, employee_name, email, position, salary, entry_date):
    with connection:
        connection.execute("""INSERT INTO employees(employee_name, email, position, sale, entry_date)
                              VALUES(?, ?, ?, ?, ?); """, (employee_name, email, position, salary, entry_date)
                            )
        
def show_employees(connection):
    with connection:
        return connection.execute("SELECT * FROM employees").fetchall()
    
def update_employee_name(connection, employee_id, employee_name):
    with connection:
        connection.execute("UPDATE employeers SET employee_name=? WHERE employee_id=?", (employee_name, employee_id))

def update_employee_email(connection, employee_id, email):
    with connection:
        connection.execute("UPDATE employees SET email=? WHERE employee_id", (email, employee_id))
     
def update_employee_position(connection, employee_id, position):
    with connection:
        connection.execute("UPDATE employees SET position=? WHERE employee_id", (position, employee_id))

def update_employee_salary(connection, employee_id, salary):
    with connection:
        connection.execute("UPDATE employees SET salary=? WHERE employee_id", (salary, employee_id))

def delete_employee(connection, employee_id):
    with connection:
        connection.execute("DELETE * FROM employees WHERE employee_id=?", (employee_id,))   

