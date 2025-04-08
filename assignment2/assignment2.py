import csv
import traceback
import os
from datetime import datetime
import custom_module

# ===== TASK 2: READ EMPLOYEES =====
print("\n=== TASK 2: ===")
def read_employees():
    employees = {"fields": [], "rows": []}
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            employees["fields"] = next(reader)
            employees["rows"] = [row for row in reader]
        return employees
    except Exception as e:
        traceback.print_exc()
        exit(1)

employees = read_employees()
print(f"Employees Data: {employees}")

# ===== TASK 3: COLUMN INDEX =====
print("\n=== TASK 3: ===")
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")
print(f"Employee ID Column Index: {employee_id_column}")

# ===== TASK 4: FIRST NAME =====
print("\n=== TASK 4: ===")
def first_name(row_num):
    return employees["rows"][row_num][column_index("first_name")]

print(f"First name of employee 0: {first_name(0)}")

# ===== TASK 5: FIND EMPLOYEE =====
print("\n=== TASK 5: ===")
def employee_find(employee_id):
    def employee_match(row):
        return row[employee_id_column] == str(employee_id)
    return list(filter(employee_match, employees["rows"]))

employee_found = employee_find(1)
print(f"Employee found with ID 1: {employee_found}")

# ===== TASK 6: FIND EMPLOYEE WITH LAMBDA =====
print("\n=== TASK 6: ===")
def employee_find_2(employee_id):
    return list(filter(lambda row: row[employee_id_column] == str(employee_id), employees["rows"]))

employee_found_2 = employee_find_2(1)
print(f"Employee found with ID 1 (Lambda): {employee_found_2}")

# ===== TASK 7: SORT BY LAST NAME =====
print("\n=== TASK 7: ===")
def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]

sorted_by_last_name = sort_by_last_name()
print(f"Employees Sorted by Last Name: {sorted_by_last_name}")

# ===== TASK 8: EMPLOYEE DICT =====
print("\n=== TASK 8: ===")
def employee_dict(row):
    return {
        employees["fields"][i]: row[i]
        for i in range(len(row))
        if employees["fields"][i] != "employee_id"
    }

employee_dict_result = employee_dict(employees["rows"][0])
print(f"Employee Dict for First Employee: {employee_dict_result}")

# ===== TASK 9: ALL EMPLOYEES DICT =====
print("\n=== TASK 9: ===")
def all_employees_dict():
    return {
        row[employee_id_column]: employee_dict(row)
        for row in employees["rows"]
    }

all_employees = all_employees_dict()
print(f"All Employees as Dict: {all_employees}")

# ===== TASK 10: OS MODULE =====
print("\n=== TASK 10: ===")
def get_this_value():
    return os.getenv('THISVALUE', None)

this_value = get_this_value()
print(f"Value of THISVALUE environment variable: {this_value}")

# ===== TASK 11: CUSTOM MODULE =====
print("\n=== TASK 11: ===")
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# (Assuming you need to set a secret; this would print confirmation if the module is used correctly)
set_that_secret("new_secret_123")
print("Secret set through custom_module.")

# ===== TASK 12: READ MINUTES =====
print("\n=== TASK 12: ===")
def read_minutes():
    def read_file(filename):
        data = {"fields": [], "rows": []}
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data["fields"] = next(reader)
            data["rows"] = [tuple(row) for row in reader]
        return data
    
    minutes1 = read_file('minutes.csv')
    minutes2 = {"fields": minutes1["fields"], "rows": minutes1["rows"][:10]}  # First 10 rows as sample
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(f"Minutes Data (Full): {minutes1}")
print(f"Minutes Data (Sample, first 10 rows): {minutes2}")

# ===== TASK 13: CREATE MINUTES SET =====
print("\n=== TASK 13: ===")
def create_minutes_set():
    return set(minutes1["rows"]).union(set(minutes2["rows"]))

minutes_set = create_minutes_set()
print(f"Minutes Set (Union of both): {minutes_set}")

# ===== TASK 14: CONVERT TO DATETIME =====
print("\n=== TASK 14: ===")
def create_minutes_list():
    return [
        (row[0], datetime.strptime(row[1], "%B %d, %Y"))
        for row in minutes_set
    ]

minutes_list = create_minutes_list()
print(f"Minutes List with Dates: {minutes_list}")

# ===== TASK 15: WRITE SORTED LIST =====
print("\n=== TASK 15: ===")
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    with open('minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date"])
        writer.writerows(
            (name, date.strftime("%B %d, %Y"))
            for name, date in minutes_list
        )
    return [
        (name, date.strftime("%B %d, %Y"))
        for name, date in minutes_list
    ]

sorted_minutes = write_sorted_list()
print(f"Sorted Minutes List: {sorted_minutes}")
