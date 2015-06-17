from pygame import *

screen = display.set_mode((800,600))

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            omx,omy = evt.pos
            back = screen.copy()
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

    if mb[0] == 1:
        dist = (((omx - mx) ** 2 + (omy - my) ** 2)) ** 0.5
        for i in range(int(dist)):        
            sx = i * (omx - mx) / dist
            sy = i * (omy - my) / dist
            draw.circle(screen,(255,0,0),(omx - int(sx), omy - int(sy)),3)
        omx,omy = mx,my
    display.flip() 
quit()
