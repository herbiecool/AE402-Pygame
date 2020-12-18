class Human:    
    def __init__(self, name, weight, height ,gender):
        self.name = name
        self.weight = weight
        self.height = height
        self.gender = gender 

    def bmi(self):
        return self.weight//((self.height/100)**2)
    def futureW(self):
        return self.weight+30
    def futureH(self):
        return self.height+20
             
name = input('name?')  
weight = int(input('weight?')) 
height = int(input('height?')) 
gender = input('gender?')
a = Human(name,height,weight,gender)
print('')
print("name",a.name)
print("weight",a.weight)
print("height",a.height)
print("bmi",a.bmi()) 
print("gender",a.gender)
print("futureW",a.futureW())
print("futureH",a.futureH())