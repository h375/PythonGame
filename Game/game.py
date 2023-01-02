class Player:

    def __init__(self,x,y):
        self.x = x 
        self.y = y
        # self.bananaX =20 
        self.bananas = []
        self.level = 1
        self.usedBananas = 0
        self.enemies = []


    # def getX(self):
    #     return self.x

    # def getY(self):
    #     return self.y

    def moveDown(self):
        if self.y < 500:
            self.y +=20

    def moveUp(self):
        if self.y > 1:
            self.y-=20

    def reset(self):
        self.usedBananas = 0


    
    # def shoot(self):
    #     if self.bananaX  < 810:
    #         self.bananaX +=5

        # else:
        #     self.bananaX = 20
        #     self.shoost()


class Banana:
    def __init__(self):
        self.x = 20

    def shoot(self):
        if self.x < 810:
            self.x+=7


class Enemy:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def moveLeft(self):
        if self.x > 0:
            self.x-=50

        
class Fireball:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def shoot(self):
        if self.x > 0:
            self.x-=100
