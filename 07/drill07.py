from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    # fill here
    global running
    global character
    global x,y
    global frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x, KPU_HEIGHT - 1 - event.y
            while SDL_MOUSEMOTION == True:
                delay(0.5)
                character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
                frame = (frame + 1) % 8
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

'''def character_move():
    global x,y
    global dir
    global character
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            x,y = event.x, KPU_HEIGHT - 1 - event.y

    pass

'''
open_canvas(KPU_WIDTH,KPU_HEIGHT)
# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
dir = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    mouse.draw(x,y)
    #character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    update_canvas()

    handle_events()


    #frame = (frame + 1) % 8

close_canvas()




