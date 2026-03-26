import pandas as pd

# Load the Excel file
employee_df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
def employees_in_automotive():
    automotive = employee_df[employee_df['Department'] == 'Automotive']
    print("Employees in Automotive domain:\n", automotive)

# b) Employee details by ID
def employee_by_id(emp_id):
    emp_details = employee_df[employee_df['Employee ID'] == int(emp_id)]
    if not emp_details.empty:
        print("Employee Details:\n", emp_details)
    else:
        print("No employee found with ID:", emp_id)

# d) List of all Developers
def list_developers():
    developers = employee_df[employee_df['Designation'].str.contains("Developer", case=False)]
    print("List of Developers:\n", developers)

# Example usage
if __name__ == "__main__":
    employees_in_automotive()
    employee_by_id(102)   # Replace with user input if needed
    list_developers()