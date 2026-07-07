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
                            department_id INTEGER NOT NULL,
                            position TEXT NOT NULL,
                            salary REAL NOT NULL,
                            entry_date TEXT NOT NULL,
                            FOREIGN KEY(department_id) REFERENCES departments(department_id)
                       )
                       """)
    
        connection.execute("""
                        CREATE TABLE IF NOT EXISTS departments (
                            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            department_name TEXT NOT NULL
                       )
                       """)
    

#-----DEPARTMENTS FUNCTIONS-----
def add_department(connection, department_name):
    with connection:
        connection.execute("INSERT INTO departments(department_name) VALUES(?); ", (department_name,))

def show_departments(connection):
    with connection:
        return connection.execute("SELECT * FROM departments ORDER BY department_name").fetchall()
    
def get_department(connection, department_id):
    with connection:
        return connection.execute("SELECT 1 FROM departments WHERE department_id=?", (department_id,)).fetchone()
    
def update_department_name(connection, department_id, department_name):
    with connection:
        connection.execute("UPDATE departments SET department_name=? WHERE department_id=?", (department_name, department_id))
    
def delete_department(connection, department_id):
    with connection:
        connection.execute("DELETE FROM departments WHERE department_id=?", (department_id,))


#-----EMPLOYEES FUNCTIONS-----
def add_employee(connection, employee_name, email, department_id, position, salary, entry_date):
    with connection:
        connection.execute("""INSERT INTO employees(employee_name, email, department_id, position, salary, entry_date)
                              VALUES(?, ?, ?, ?, ?, ?); """, (employee_name, email, department_id, position, salary, entry_date)
                            )
        
def show_employees(connection):
    with connection:
        return connection.execute("""SELECT  
                                        e.employee_id,
                                        e.employee_name,
                                        e.email,
                                        d.department_name,
                                        e.position,
                                        e.salary,
                                        e.entry_date
                                    FROM employees e
                                    JOIN departments d ON e.department_id = d.department_id
                                    ORDER BY e.employee_name;
                                """).fetchall()
    
def get_employee(connection, employee_id):
    with connection:
        return connection.execute("SELECT 1 FROM employees WHERE employee_id=?", (employee_id,)).fetchone()
    
def search_employee_by_id(connection, employee_id):
    with connection:
        return connection.execute("""SELECT 
                                        e.employee_name, 
                                        e.email, 
                                        d.department_name, 
                                        e.position, 
                                        e.salary, 
                                        e.entry_date 
                                    FROM employees e
                                    JOIN departments d ON e.department_id = d.department_id
                                    WHERE e.employee_id=?
                                 """, (employee_id,)).fetchone()
    
def search_employee_by_name(connection, employee_name):
    with connection:
        return connection.execute("""SELECT
                                        e.employee_name,
                                        e.email,
                                        d.department_name,
                                        e.position,
                                        e.salary,
                                        e.entry_date
                                    FROM employees e
                                    JOIN departments d 
                                    ON e.department_id = d.department_id
                                    WHERE e.employee_name LIKE ?
                                    ORDER BY e.employee_name;
                                 """, (f"%{employee_name}%",)).fetchall()
    
def search_employee_by_email(connection, email):
    with connection:
        return connection.execute("""SELECT
                                        e.employee_name,
                                        e.email,
                                        d.department_name,
                                        e.position,
                                        e.salary,
                                        e.entry_date
                                    FROM employees e
                                    JOIN departments d 
                                    ON e.department_id = d.department_id
                                    WHERE e.email=?
                                  """, (email,)).fetchone()
    
def update_employee_name(connection, employee_id, employee_name):
    with connection:
        connection.execute("UPDATE employees SET employee_name=? WHERE employee_id=?", (employee_name, employee_id))

def update_employee_email(connection, employee_id, email):
    with connection:
        connection.execute("UPDATE employees SET email=? WHERE employee_id=?", (email, employee_id))
     
def update_employee_position(connection, employee_id, position):
    with connection:
        connection.execute("UPDATE employees SET position=? WHERE employee_id=?", (position, employee_id))

def update_employee_salary(connection, employee_id, salary):
    with connection:
        connection.execute("UPDATE employees SET salary=? WHERE employee_id=?", (salary, employee_id))

def delete_employee(connection, employee_id):
    with connection:
        connection.execute("DELETE FROM employees WHERE employee_id=?", (employee_id,))  


def total_employees(connection):
    with connection:
        return connection.execute("SELECT COUNT(*) FROM employees").fetchone()[0]

def total_departments(connection):
    with connection:
        return connection.execute("SELECT COUNT(*) FROM departments").fetchone()[0] 
    
def highest_salaries(connection):
    with connection:
        return connection.execute("""SELECT 
                                            employee_name, salary FROM employees
                                            ORDER BY salary DESC
                                            LIMIT 3
                                  """).fetchone()
def lowest_salaries(connection):
    with connection:
        return connection.execute("""SELECT
                                            employee_name, salary FROM employees
                                            ORDER BY salary ASC
                                            LIMIT 3""")
    
def average_salary(connection):
    with connection:
        return connection.execute("SELECT AVG(salary) FROM employees").fetchone()[0]
    
def employees_per_department(connection):
    with connection:
        return connection.execute("""SELECT
                                            d.department_name
                                            COUNT(e.employee_id)
                                        FROM departments d
                                        LEFT JOIN employees e
                                        ON d.department_id = e.department_id
                                        GROUP BY d.department_name
                                        ORDER BY d.department_name
                                  """).fetchall()
    
def payroll_by_department(connection):
    with connection:
        return connection.execute("""SELECT
                                            d.department_name
                                            COALESCE(SUM(e.salary), 0)
                                        FROM departments d
                                        LEFT JOIN employees e 
                                        ON department_id = e.department_id
                                        GROUP BY d.department_name
                                        ORDER BY d.department_name
                                  """).fetchall()

