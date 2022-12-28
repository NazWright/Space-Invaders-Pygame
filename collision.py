import math 

class Collision:
    def __init__(self, object1X, object1Y, object2X, object2Y) -> None:
        self.object1X = object1X
        self.object1Y = object1Y
        self.object2X = object2X
        self.object2Y = object2Y
        
        
        
    def trigger():
        distance = math.sqrt(math.pow(ob - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:
            return True
        else:
            return False