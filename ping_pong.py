from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self,player_image, x, y, speed,x_size,y_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size,y_size))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(GameSprite):

    def update_l(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed

        
        if keys[K_s] and self.rect.y < win_height - 125:
            self.rect.y += self.speed


    def update_r(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_height - 125:
            self.rect.y += self.speed





win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
back = (200,255,255)
window.fill(back)



player1 = Player("raketka.png", 50, 100, 10,  100, 130)
player2 = Player("raketka.png", win_width-150, 100, 10, 100, 130)











finish = False
game = True
FPS = 60
clock = time.Clock()
while game:

    for e in event.get():
            if e.type == QUIT:
                game = False


    if finish != True:
        window.fill(back)
        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
        






    display.update()
    clock.tick(FPS)




    



    









    












