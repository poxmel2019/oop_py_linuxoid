import random
def f():
    """Classes and objects"""
    class Warrior:

        health = 0        
        name = None

        def setName(self,n):
            self.name = n

        def setHealth(self,h):
            self.health = h

        def beat(self,a):
            print("{0} is beating".format(self.name))
            a.health -= 20
            print("{0} has {1} health".format(a.name,a.health))

        def getHealth(self):
            print("The unit {1} has {0} health".format(self.health,self.name))

    
    unit_1 = Warrior()
    unit_2 = Warrior()

    unit_1.setName('Bob')
    unit_2.setName('Tom')

    unit_1.setHealth(100)
    unit_2.setHealth(100)

    li = [unit_1,unit_2]
    
    unit_1.getHealth()
    unit_2.getHealth()


    que1 = 0
    que2 = 0

    condition = True
    while condition:
        que1 = random.randrange(2)
        if que1 == 0: que2 = 1
        elif que2 == 1: que2 = 0
        li[que1].beat(li[que2])
        if li[que1].health == 0 or li[que2].health == 0:
            condition = False
            print('Game over')
            
        
        
    

