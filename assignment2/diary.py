# Task 1: Diary
import traceback

try:
    with open("diary.txt", "a") as file:  # Open file in append mode
        first_entry = True  # Flag to check if it's the first input

        while True:
            # If it is the first input, prompt for "What happened today?"
            if first_entry:
                entry = input("What happened today? ")  
                first_entry = False  # Change the flag to False after the first input
            else:
                entry = input("What else? ")

            # Check if the user enters 'done for now'
            if entry.lower() == "done for now":
                file.write(entry + "\n")  # Write "done for now" to the file
                break  # Exit the loop after writing "done for now"

            # Write the user's entry to the file if it's not 'done for now'
            file.write(entry + "\n")

except Exception as e:
    # Handle exceptions and print the traceback
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = []
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")



#Task 2: Read a CSV File
import csv
import traceback

def read_employees():
    employees_data = {}
    rows = []
    
    try:
        # Open the CSV file for reading
        with open("../csv/minutes.csv", "r") as file:
            csv_reader = csv.reader(file)
            
            # Get the first row as field names
            employees_data["fields"] = next(csv_reader)  # The first row is the header
            
            # Read the rest of the rows
            for row in csv_reader:
                rows.append(row)
            
            # Add the rows to the dictionary under the key "rows"
            employees_data["rows"] = rows
        
        return employees_data
    
    except Exception as e:
        # Catch and handle any exceptions
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)

# Call the function and store the result in the 'employees' variable
employees = read_employees()

# Print out the employees data to verify it's working correctly
print(employees)


#Task 3: Find the Column Index
def column_index(field_name):
    return employees["fields"].index(field_name)

# Test
employee_id_column = column_index("employee_id")
print(employee_id_column)

#Task 4: Find the Employee First Name
def first_name(row_num):
    column_idx = column_index("first_name")
    return employees["rows"][row_num][column_idx]

# Test
print(first_name(0))  # Get first name of the first employee

#Task 5: Find the Employee:a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Test
print(employee_find(1001))

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Test
print(employee_find_2(1001))

#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

# Test
sorted_employees = sort_by_last_name()
print(sorted_employees)

#Task 8: Create a dict for an Employee
def employee_dict(row):
    return {employees["fields"][i]: row[i] for i in range(len(row)) if employees["fields"][i] != "employee_id"}

# Test
print(employee_dict(employees["rows"][0]))  # Test for the first row

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    return {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}

# Test
print(all_employees_dict())

#Task 10: Use the os Module
# custom_module.py
secret = "shazam!"
def set_secret(new_secret):
    global secret
    secret = new_secret

#Task 11: Creating Your Own Module
    #1.	Create custom_module.py:
        # custom_module.py
secret = "shazam!"

def set_secret(new_secret):
    global secret
    secret = new_secret
    #2.	In your main program:
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# Test
set_that_secret("new_secret_value")
print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    def read_file(file_name):
        minutes = {"fields": [], "rows": []}
        try:
            with open(file_name, mode='r') as file:
                csv_reader = csv.reader(file)
                minutes["fields"] = next(csv_reader)
                for row in csv_reader:
                    minutes["rows"].append(tuple(row))  # Convert rows to tuple
        except Exception as e:
            print("An exception occurred: ", e)
        return minutes

    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")
    return minutes1, minutes2

# Test
minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#Task 13: Create minutes_set
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])
    return minutes1_set.union(minutes2_set)

# Test
minutes_set = create_minutes_set()
print(minutes_set)

#Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

# Test
minutes_list = create_minutes_list()
print(minutes_list)

#Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])  # Sort by datetime
    with open("./minutes.csv", mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(minutes1["fields"])
        for row in minutes_list:
            csv_writer.writerow([row[0], row[1].strftime("%B %d, %Y")])
    return minutes_list

# Test
sorted_minutes = write_sorted_list()
print(sorted_minutes)
