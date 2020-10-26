class Animal:
    def __init__(self):
        self.age = 1
    
    def getOld(self):
        self.age += 1
        
        
a = Animal()

print(a.age)
a.getOld()
print(a.age)