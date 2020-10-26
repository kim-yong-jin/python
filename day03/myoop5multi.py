class Animal:
    def __init__(self):
        self.age = 1
    
    def getOld(self):
        self.age += 1
        
class God :
    def __init__(self):
        self.sprit_power = 1;
    def goToGeryong(self):
        self.sprit_power += 10;
    def goToMisokchon(self):
        self.sprit_power += 2;

class Human(Animal,God):
    def __init__(self):
        super().__init__()
        self.money_power = 1000000000000
    def earnMoney(self, i = "none"):
        
        if i == "none":
            self.money_power += 1
        else:
            self.money_power += i
    
    def getOld(self):
        self.age += 2
    
        
        
if __name__ == '__main__':
   
    
    
    a = Human();
    
    print(a.sprit_power);
    
    
