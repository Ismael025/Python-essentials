   ###if you want to tell all employees together that there is no work today!!!!!!!
   
def greet_employee(names):
    for name in names:
     #return 'Hello'+ name.title() +'!'
     print (f"Hello, {name} There is no work today!")

employee =['Peter','Ismael', 'Jack', 'maliam', 'manase', 'kaleb', 'gedeion']
greet_employee(employee)

print()
### the same way to print as follow............
print ('='*6, "this is the other way to print above information ", '='*6)
print()
employee = {
    'employee1': 'Peter',
    'employee2': 'Ismael',
    'employee3': 'Jack',
    'employee4': 'Maliam',
    'employee5': 'Manase',
    'employee6': 'Kaleb',
    'employee7': 'Gedeion'
}

greet_employee(employee.values())