from settings import*

class BEHAVIORS:
    def draw_img(self):
        SCREEN.blit(self.image, self.rect)
    def draw_rect(self):
        p.draw.rect(SCREEN, self.color, self.rect)