class Animal:
    zooname="safari zoo"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eat(self):
        print(f"{self.name} is eating..")

    def sleep(self):
        print(f"{self.name} is sleeping..")

class mammal(Animal):
    def __init__(self,name,age,weight):
        super().__init__(name,age)
        self.weight=weight


    def walk(self):
        print(f"{self.name} is walking..")

class bird(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def fly(self):
        print(f"{self.name} is flying..")


class fish(Animal):
    def __init__(self,name,age,length,nb_fin):
        super().__init__(name,age)
        self.length=length
        self.nb_fin=nb_fin
    def swim(self):
        print(f"{self.name} is swimming..")   

lion=mammal("lio",6,20)
print(f"{lion.name} has{lion.age} years old")
print(f" it has {lion.weight} kg")
print(f" it lives in {mammal.zooname}")
lion.eat()

canary=bird("sunny",3,"white")
print(f"{canary.name} has{canary.age} years old")
print(f"his colour is{canary.color}")
print(f" it lives in {mammal.zooname}")
canary.fly()

orangefish= fish("nemo", 2, 15, 4)
print(f"{orangefish.name} has {orangefish.age} years old")
print(f" has {orangefish.length} cm")
print(f"  has {orangefish.nb_fin} fin")
print(f" it lives in {mammal.zooname}")
orangefish.swim()