
# Employee Payroll and Deduction Analysis System

try:
    employee_id = input("Enter Employee ID: ")
    employee_name = input("Enter Employee Name: ")

    basic_pay = float(input("Enter Basic Pay: ₹"))
    allowances = float(input("Enter Allowances: ₹"))
    overtime_hours = float(input("Enter Overtime Hours: "))
    overtime_rate = float(input("Enter Overtime Rate per Hour: ₹"))
    incentives = float(input("Enter Incentives: ₹"))
    if (basic_pay < 0 or allowances < 0 or
        overtime_hours < 0 or overtime_rate < 0 or
        incentives < 0):

        print("\nError: Salary components cannot be negative.")

    else:
        overtime_pay = overtime_hours * overtime_rate
        gross_salary = (
            basic_pay + allowances + overtime_pay + incentives
        )
        if gross_salary <= 10000:
            deduction = 0

        elif gross_salary <= 20000:
            deduction = (gross_salary - 10000) * 0.05

        else:
            deduction = (
                10000 * 0.05
                + (gross_salary - 20000) * 0.10
            )
        net_salary = gross_salary - deduction
        print("\n========================================")
        print("          EMPLOYEE SALARY SLIP")
        print("========================================")
        print("Employee ID:       ", employee_id)
        print("Employee Name:     ", employee_name)
        print("----------------------------------------")
        print("                 EARNINGS")
        print("----------------------------------------")
        print(f"Basic Pay:          ₹{basic_pay:,.2f}")
        print(f"Allowances:         ₹{allowances:,.2f}")
        print(f"Overtime Pay:       ₹{overtime_pay:,.2f}")
        print(f"Incentives:         ₹{incentives:,.2f}")
        print("----------------------------------------")
        print(f"Gross Salary:       ₹{gross_salary:,.2f}")
        print("----------------------------------------")
        print("                DEDUCTIONS")
        print("----------------------------------------")
        print(f"Total Deduction:    ₹{deduction:,.2f}")
        print("----------------------------------------")
        print(f"NET SALARY:         ₹{net_salary:,.2f}")
        print("========================================")

except ValueError:
    print("Error: Please enter valid numeric values.")
