from module.behaviors import*

class ENEMYBOSS(BEHAVIORS):
    ofset_x = 0
    ofset_y = 0
    limit = 0

    def __init__(self):
        self.size = (64, 64)
        self.color = RED 
        self.reverse = False
        self.rect = p.Rect(
                        ENEMYBOSS.ofset_x,
                        ENEMYBOSS.ofset_y,
                        self.size[0],
                        self.size[1]
                        )
        self.image = image_load(os.path.dirname(__file__))
        self.image = p.transform.scale(self.image[0], (self.size[0], self.size[1]))
        self.speed = 2.5
        self.health = 5
        self.bull_spawn = 0
        ENEMYBOSS.limit +=1
        if ENEMYBOSS.limit != SCREENSIZE[0]/ self.size[0]:
            ENEMYBOSS.ofset_x += self.size[0]
        else:
            ENEMYBOSS.ofset_y += self.size[1]
            ENEMYBOSS.ofset_x = 0
            ENEMYBOSS.limit = 0


    def move(self):
        if self.reverse == False:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

        if self.rect.x > SCREENSIZE[0] - self.size[0] or self.rect.x < 0:
            self.reverse = not(self.reverse)
            self.rect.y +=self.size[1]

    def shooting(self, enemy_bullets, ENEMY_BULLET, enemy):
        self.bull = randint(0, 50)
        if self.bull == 1:
            enemy_bullets.append(ENEMY_BULLET(enemy))
        


map_list = [
        0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
]

enemyboss = ENEMYBOSS()