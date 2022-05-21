class Employee:
    MIN_SALARY=30000
    def __init__(self, name, salary=30000):
        self.name=name
        if salary>=Employee.MIN_SALARY:
            self.salary=salary
        else:
            self.salary=Employee.MIN_SALARY
    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            name=f.readline()
        return cls(name)
        
# Create an employee without calling Employee
emp=Employee.from_file("employee_data.txt")
print(type(emp))
print(emp.name)