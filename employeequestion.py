class Employee:
    
    company_name="TechNova Solutions"
    def __init__(self,emp_name,emp_id,salary):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.salary=salary

    def detail(self):
        print(f"employee name :{self.emp_name}")
        print(f"employee id :{self.emp_id}")
        print(f"employee salary :{self.salary}")
        print(f"company name:{Employee.company_name}")

class Developer(Employee):
    
    def __init__(self, emp_name, emp_id, salary,programming_language):
        super().__init__(emp_name, emp_id, salary)
        self.programming_language=programming_language
        
    def detail(self):
        super().detail()
        print(f"programming language:{self.programming_language}")

class Manager(Employee):
    
    def __init__(self, emp_name, emp_id, salary,team_size):
        super().__init__(emp_name, emp_id, salary)
        self.team_size=team_size

    def detail(self):
        super().detail()
        print(f"team size :{self.team_size}")

dv=Developer("samil","sd102",35000,"python")
ma=Manager("sabu","mn201",40000,10)

print("\n developer details")
dv.detail()

print("\n manager details")
ma.detail()
Employee.company_name="Zyvion Technologies"  

print("\n after changing company name")
print("\n developer details")
dv.detail()

print("\n manager details")
ma.detail()