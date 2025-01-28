from module.behaviors import*

class BULLET(BEHAVIORS):
    def __init__(self, player):
        self.size = (8, 8)
        self.color = RED 
        self.rect = p.Rect(
                        player.rect.x + player.size[0]/2 - self.size[0]/2,
                        player.rect.y - self.size[1],
                        self.size[0],
                        self.size[1]
                        )
        self.image = image_load(os.path.dirname(__file__))
        self.image = p.transform.scale(self.image[0], (self.size[0], self.size[1]))
        self.speed = 8

    def move(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            bullets.remove(self)
bullets = []
