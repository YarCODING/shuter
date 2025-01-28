
from module.behaviors import*

class PLAYER(BEHAVIORS):
    def __init__(self):
        self.size = (64, 64)
        self.color = RED 
        self.rect = p.Rect(
                        SCREENSIZE[0]/2 - self.size[0]/2,
                        SCREENSIZE[1] - self.size[1]*2,
                        self.size[0],
                        self.size[1]
                        )
        self.image = image_load(os.path.dirname(__file__))
        self.image = p.transform.scale(self.image[0], (self.size[0], self.size[1]))
        self.speed = 3

    def move(self):
        keys = p.key.get_pressed()

        if keys[p.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[p.K_d] and self.rect.x < SCREENSIZE[0] - self.size[0]:
            self.rect.x += self.speed

        if keys[p.K_w] and self.rect.y > SCREENSIZE[1]/2:
            self.rect.y -= self.speed
        if keys[p.K_s] and self.rect.y < SCREENSIZE[1] - self.size[1]:
           self.rect.y += self.speed

player = PLAYER()
