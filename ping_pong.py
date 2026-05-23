from pygame import *
from random import randint

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
font.init()
font = font.SysFont('Arial', 36)
lose1 = font.render("Player 1 lose", True, (255,0,0))
lose2 = font.render("Player 2 lose", True, (255,0,0))
win = font.render("WINNER", True, (0,255,0))






player1 = Player("raketka.png", 50, 100, 10,  100, 130)
player2 = Player("raketka.png", win_width-150, 100, 10, 100, 130)
machik = GameSprite("machik.png", 350,250,7,40,40)

player1_photo = transform.scale(image.load('player1.png'),(80,80))
player2_photo = transform.scale(image.load('player2.png'),(80,80))





speed_x = 3
speed_y = 3
phot1 = True
phot2 = True
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
        machik.reset()
        machik.rect.x += speed_x
        machik.rect.y += speed_y
        if phot1 == True:
            window.blit(player1_photo, (10,10))
        if phot2 == True:
            window.blit(player2_photo, (620,10))




    
        if sprite.collide_rect(player1, machik) or sprite.collide_rect(player2, machik):
            speed_x *= -1

        if machik.rect.y >= 480 or machik.rect.y <= 0:
            speed_y *= -1


        if machik.rect.x >= 695:
            window.blit(lose2,(200,200))
            phot1 = False
            window.blit(player1_photo, (150,250))
            window.blit(win,(250,270))




        if machik.rect.x <= 5:
            window.blit(lose1,(200,200))
            phot2 = False
            window.blit(player2_photo, (150,250))
            window.blit(win,(250,270))




    display.update()
    clock.tick(FPS)




    



    



    



    









    












