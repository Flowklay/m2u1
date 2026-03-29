class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f'Name: {self.__name}')

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f'Company: {self.company}')

    def work(self):
        print(f'{self.name} works')

bob = Employee('bob','rsd')
bob.work()
bob.display_info()

#class person:
    #def __init__(self, name,age):
        #self.name = name
        #self.age = age
    
    #def disp(self):
        #print(f"{self.name}, {self.age}")
    
    #def __str__(self):
        #return f"{self.name}, {self.age}"
    
#tom = person('tom', 23)
#print(tom)
#tom.disp_info()

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, oth):
        return Vector(self.x + oth.x, self.y + oth.y)

    def __sub__(self, oth):
        return Vector(self.x - oth.x, self.y - oth.y)

v1 = Vector(3, 5)
v2 = Vector(1,1)
v3 = v1 + v2
print(f" {v3.x}, {v3.y}")