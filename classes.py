class person:
    def __init__(self,name,age,height,address,is_married):
        self.name = name
        self.age = age
        self.height=height
        self.address=address
        self.is_married=is_married
    def greet(self): 
        return f"HI, my name is {self.name}"  

person1=person("Alice",25,"170cm","kimath street",False)
person2=person("Alba",20,"172cm","embakasi",False)
print(person1)        
print(person2)
print(person1.greet())
print(person2.greet())

