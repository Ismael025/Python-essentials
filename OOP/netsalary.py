class Employee:
    def __init__(self, id, salary, department=None):
        self.id =id
        self.salary = salary
        self.department = department

    def tax(self):
        return self.salary * 0.2

    def netsalary(self):
        return self.salary - self.tax()

emp1 = Employee(101, 400000,'IT')

#print(emp1.id, emp1.salary,emp1.department)
print('the netsalary for: ',emp1.id, 'is',emp1.netsalary())        