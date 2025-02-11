from behaviors import*

class ENEMY(BEHAVIORS):
    ofset_x = 0
    ofset_y = 0
    limit = 0

    def __init__(self):
        self.size = (32, 32)
        self.color = RED 
        self.reverse = False
        self.rect = p.Rect(
                        ENEMY.ofset_x,
                        ENEMY.ofset_y,
                        self.size[0],
                        self.size[1]
                        )
        self.image = p.image.load('enemy.png')
        self.image = p.transform.scale(self.image, (self.size[0], self.size[1]))
        self.speed = 2
        self.bull_spawn = 0
        ENEMY.limit +=1
        if ENEMY.limit != SCREENSIZE[0]/ self.size[0]:
            ENEMY.ofset_x += self.size[0]
        else:
            ENEMY.ofset_y += self.size[1]
            ENEMY.ofset_x = 0
            ENEMY.limit = 0


    def move(self):
        if self.reverse == False:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

        if self.rect.x > SCREENSIZE[0] - self.size[0] or self.rect.x < 0:
            self.reverse = not(self.reverse)
            self.rect.y +=self.size[1]

        if self.rect.y < 0:
            enemy_list.remove(self)

    def shooting(self, enemy_bullets, ENEMY_BULLET, enemy):
        self.bull = randint(0, 750)
        if self.bull == 1:
            enemy_bullets.append(ENEMY_BULLET(enemy))
            piy = p.mixer.Sound('piu.mp3')
            piy.play(1)
        


map_list = [
        0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
]

enemy_list = []

def spawn_enemys():
    global enemy_list
    for i in map_list:
        if i == 1:
            enemy_list.append(ENEMY())
        else:
            ENEMY.limit +=1
            if ENEMY.limit != SCREENSIZE[0]/ 32:
                ENEMY.ofset_x += 32
            else:
                ENEMY.ofset_y += 32
                ENEMY.ofset_x = 0
                ENEMY.limit = 0
    
    ENEMY.ofset_x = 0
    ENEMY.ofset_y = 0
    ENEMY.limit = 0



class ENEMYBOSS(BEHAVIORS):
    def __init__(self):
        self.size = (64, 64)
        self.color = RED 
        self.reverse = False
        self.rect = p.Rect(
                        0,
                        0,
                        self.size[0],
                        self.size[1]
                        )
        self.image = p.image.load('enemyboss.png')
        self.image = p.transform.scale(self.image, (self.size[0], self.size[1]))
        self.speed = 2.5
        self.health = 5


    def move(self):
        if self.reverse == False:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

        if self.rect.x > SCREENSIZE[0] - self.size[0] or self.rect.x < 0:
            self.reverse = not(self.reverse)
            self.rect.y +=self.size[1]

            

    def shooting(self, enemy_bullets, ENEMY_BULLET, enemy):
        self.bull = randint(0, 200)
        if self.bull == 1:
            enemy_bullets.append(ENEMY_BULLET(enemy))

enemyboss = ENEMYBOSS()