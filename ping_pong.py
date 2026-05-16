from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
back = (200,255,255)
window.fill(back)

finish = False
game = True
FPS = 60
clock = time.Clock()
while game:

    for e in event.get():
            if e.type == QUIT:
                game = False






    display.update()
    clock.tick(FPS)




    



    












