class FullTimeEmployee:

    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee:

    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Freelancer:

    def __init__(self, name, number_project, project_price):
        self.name = name
        self.number_project = number_project
        self.project_price = project_price

    def calculate_salary(self):
        return self.number_project * self.project_price


obj1 = FullTimeEmployee("samil", 5000)
obj2 = PartTimeEmployee("sabu", 100, 12)
obj3 = Freelancer("aju", 3, 10000)

obj = [obj1, obj2, obj3]

for ob in obj:
    print("Name:", ob.name)
    print("Salary:", ob.calculate_salary())
    