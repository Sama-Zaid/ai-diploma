number_of_team_members = int(input("Enter the Number of Members : "))
project_period = int(input("How Many Months will the Project take ? : "))
members_salary = float(input("What is the Salary of each employee ? : "))
project_cloud_cost = float(input("What is the cloud Cost ? : "))

total_salary_cost = number_of_team_members * project_period * members_salary
subtotal = total_salary_cost + project_cloud_cost
VAT = subtotal * 0.14

project_total_cost = subtotal + VAT

print(f"\nThe Project Total Cost is {project_total_cost: .2F}")