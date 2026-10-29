import requests
response= requests.get("https://example.com")

class Employee:
    def __init__(self, name, position, salary, tax):
        self.name = name            # Public
        self._position = position  # Protected
        self.__salary = salary      # Private
        self.__tax = tax            # Private
        
    # Public method
    def getposition(self):
        return self._position
        
    # Public method
    def netsalary(self):
        return self.__salary - self.__tax

# --- Execution Code (Outside the Class) ---
# Creating an Employee Object
emp1 = Employee("Ismael", "CEO", 8000000, 400000)
        
# 1. Access public attribute
print("Employee Name:", emp1.name)
        
# 2. Access protected attribute
print("Employee Position:", emp1._position)
        
# 3. Access methods
print("Position from method:", emp1.getposition())
print("Net Salary:", emp1.netsalary())

print (response.status_code)