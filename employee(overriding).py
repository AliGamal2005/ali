class Employee:
    def __init__(self,name,role,base_salary):
        self.name=name
        self.role=role
        self.base_salary=base_salary

    def display_info(self):
        print(f"{self.name} is {self.role}")

    def get_salary(self):
        return self.base_salary


class manager(Employee):
    def __init__(self,name,base_salary,bonus):
        super().__init__(name,"manager",base_salary)
        self.bonus=bonus

    def get_salary(self):
        return self.base_salary+self.bonus
    
    
class developer(Employee):
    hour_pay=15
    def __init__(self,name,base_salary,add_hours):
        super().__init__(name,"developer",base_salary)
        self.add_hours=add_hours
        

    def get_salary(self):
        return self.base_salary+self.add_hours*developer.hour_pay

      


emp1=Employee("ali","engineer",2000)
emp1.display_info()
print("slary  is:" ,emp1.get_salary())
print("__________________________________")
emp2=manager("ahmed",2500,1000)
emp2.display_info()
print("salary is:", emp2.get_salary())
print("__________________________________")
emp3=developer("mohamed",2000,7)
emp3.display_info()
print("salary is:", emp3.get_salary())