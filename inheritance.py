class animal:# base clas
    def __init__(self,name):
        self.name=name
    def speak(self):
        return"some sound" 

class dog(animal):#child class
    def speak(self):
        return" barks"   

class cow(animal):
    # def speak(self):
    #     return"moos"
    pass


dog1 =dog("max")   
print(dog1.name)  
print(dog1.speak())

cow1=cow("jack")
print(cow1.name)
print(cow1.speak())