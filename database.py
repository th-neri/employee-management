import sqlite3

connection = sqlite3.connect("employee_management.db")

with connection:
    connection.execute("""
                        CREATE TABLE IF NOT EXISTS employees (
                            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            employee_name TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            position TEXT NOT NULL,
                            sale REAL NOT NULL,
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