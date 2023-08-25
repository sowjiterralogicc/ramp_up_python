# # import random

# # def generator_random(num_emp):
# #     while True:
# #         location=["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgon", "Hyderabad"]
# #         emp_id=random.randint(1,9999)
# #         emp_loc=random.choice(location)
# #         emp_sal=random.randint(20000,150000)
# #         yield emp_id, emp_loc, emp_sal

# # # print(emp_id)
# # # print(emp_loc)
# # # print(emp_sal)
# # num_emp=int(input("Enter employee detils: "))
# # generated_emp=generator_random(num_emp)
# # print(generated_emp)
# # for emp in generated_emp:
# #     emp_id, emp_loc, emp_sal = emp
# #     print(f"emp_id: {emp_id},emp_loc: {emp_loc},emp_sal: {emp_sal}")

# import random

# def generate_employee_details(num_employees):
#     location = ["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgon", "Hyderabad"]

#     for i in range(num_employees):
#         emp_id = random.randint(1, 9999)
#         emp_loc = random.choice(location)
#         emp_sal = random.randint(20000, 150000)
        
#         yield {
#             "Emp Id": emp_id,
#             "Emp Location": emp_loc,
#             "Emp Salary": emp_sal
#         }

# def main():
#     try:
#         num_employees = int(input("Enter the number of employee details to generate: "))
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         return
    
#     employee_generator = generate_employee_details(num_employees)
    
#     print("\nGenerated Employee Details:")
#     print("---------------------------")
    
#     for i in range(num_employees):
#         emp_id, emp_loc, emp_sal = next(employee_generator)
#         #print(f"Emp Id: {employee['Emp Id']}, Emp Location: {employee['Emp Location']}, Emp Salary: {employee['Emp Salary']}")
#         print(f"emp_id: {emp_id}, emp_loc: {emp_loc}, emp_sal: {emp_sal}")

# if __name__ == "__main__":
#     main()


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
#print(emp_generator)
# for i in range(num_emp):
#     emp_id, emp_loc, emp_sal = next(emp_generator)
#     print(f"emp_id: {emp_id}, emp_loc: {emp_loc}, emp_sal: {emp_sal}")
# for emp in emp_generator:
#     #print(f"emp_id: {emp['emp_id']},emp_loc: {emp['emp_loc']}, emp_sal: {emp['emp_sal']}")
#     print(emp)
for i in range(num_emp):
    emp=next(emp_generator)
    print(emp)