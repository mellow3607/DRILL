from pico2d import *
from math import *



open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
degree = 1
radian = 0
while(True):
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x += 2
        #delay(0.01)

   
    while y < 600 :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y)
        y += 2
        #delay(0.01)

    
    while 0 < x:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x -= 2
        #delay(0.01)

    
    while 0 < y:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y -= 2
        #delay(0.01)

    while degree < 360+1:
        clear_canvas_now()
        grass.draw_now(400,30)
        radian = degree * pi / 180
        character.draw_now(360 + cos(radian) * 270 ,360 + sin(radian) * 270)
        degree += 1

    if degree == 361 :
        degree = 0

#delay(5)

close_canvas()
