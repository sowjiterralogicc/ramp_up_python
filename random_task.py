
import random
location=["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgon", "Hyderabad"]
num_emp=int(input("Enter employee details: "))

def employee_details(num_emp):
    for i in range(num_emp):
        emp_id=random.randint(1,9999)
        emp_loc=random.choice(location)
        emp_sal=random.randint(20000,150000)
        #yield emp_id, emp_loc, emp_sal
        yield f"{{'emp_id': {emp_id}, 'emp_loc': {emp_loc}, 'emp_sal': {emp_sal}}}"
emp_generator=employee_details(num_emp)
for i in range(num_emp):
    emp=next(emp_generator)
    print(emp)
