from pygame import *

screen = display.set_mode((980, 750))
display.set_caption ("Paint")
red = (255,0,0)
width = 5
click = False
running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1 or evt.button == 3:
                back = screen.copy()
                omx, omy = evt.pos       #old mx, old my - used for drawing and dragging lines
                click = True
                
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    if click:
        screen.fill((0,0,0))
        dist = ((omx - mx)**2 + (omy - my)**2)**0.5
        for i in range(int(dist)):
            sx = i * mx / dist
            sy = i * my / dist
            draw.circle(screen,red,(int(mx - omx + sx),int(my - omy + sy)),5)
        

    display.flip()
quit()

