from behaviors import*

class ENEMY_BULLET(BEHAVIORS):
    def __init__(self, enemy):
        self.size = (8, 8)
        self.color = RED 
        self.rect = p.Rect(
                        enemy.rect.x + enemy.size[0]/2 - self.size[0]/2,
                        enemy.rect.y - self.size[1],
                        self.size[0],
                        self.size[1]
                        )
        self.image = p.image.load('bullet.png')
        self.image = p.transform.scale(self.image, (self.size[0], self.size[1]))
        self.speed = 5
        

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            enemy_bullets.remove(self)


enemy_bullets = []