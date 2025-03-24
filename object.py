class Player:
    def __init__(self,health,gender,name, defaultWeapon, credits):
        self.gender=gender
        self.health=health
        self.name=name
        self.defaultWeapon=defaultWeapon
        self.credits=credits
        print("player object created ;)")

    def playerHurt(self,damage):
        self.health=self.health-damage
        print("damage=", damage, "new health=",self.health)
    def isDead(self):
        if self.health<=0:
            return True
        else:
            return False 
        

p1=Player(100, "F")
p2=Player(90, "M")
print(p1.isDead())
print(p2.isDead())


print(p1.health,p1.gender)
print(p2.health, p2.gender)

