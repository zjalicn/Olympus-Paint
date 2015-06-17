#Paint.py
#Nikola Zjalic

#TO DO
##move pallette over to make tool bar bigger
##make a theme
##background
##find a place for the pallette icon
##save image
##undo, redo
##stamp menu
##allow user to import stamp?
##show the current width of line


from pygame import *

screen = display.set_mode((1200,800))
display.set_caption ("Paint")
screen.fill((111,111,111))

#Rectangle dimensions for tools, canvas, pallette, etc.
canvas = Rect(100,120,800,600)
palletteRect = Rect(920,200,185,187)
pencilRect = Rect(20,100,60,60)
eraserRect = Rect(20,180,60,60)
undoRect = Rect(20,260,60,60)
redoRect = Rect(20,340,60,60)
saveRect = Rect(20,420,60,60)

sel_Tool = 0
#0 = line
#1 = eraser

menu = 0
#0 = pallette menu
#1 = stamp menu

width = 10      #Line width

sel_Colour1 = (0,0,0)       #Selected colour for left click
sel_Colour2 = (255,255,255) #Selected colour for right click
recentColours = []          #Recently used colours at the top of the screen
for i in range(14):
    recentColours.append((255,255,255))

def rects():        #draws the tool rectangles back to the screen
    draw.rect(screen,(0,255,0),pencilRect,2)
    draw.rect(screen,(0,255,0),eraserRect,2)
    draw.rect(screen,(0,0,255),undoRect,2)
    draw.rect(screen,(0,0,255),redoRect,2)
    draw.rect(screen,(255,255,0),saveRect,2)

pallette = image.load("images/pallette.png")
palletteicon = image.load("images/palletteicon.png")
blackwhite = image.load("images/blackwhite.png")

draw.rect(screen,(255,255,255),canvas)
rects()


running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1 or evt.button == 3:
                omx, omy = evt.pos       #old mx, old my - used for drawing and dragging lines
            if evt.button == 4:
                width += 1
            if evt.button == 5:
                width -= 1
        if evt.type == MOUSEBUTTONUP:
            if palletteRect.collidepoint(mx,my):
                if evt.button == 1:
                    recentColours = [sel_Colour1] + recentColours[0:14]
                if evt.button == 3:
                    recentColours = [sel_Colour2] + recentColours[0:14]
            
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    print mx, my

    draw.rect(screen,sel_Colour1,(1125,240,40,40))
    draw.rect(screen,sel_Colour2,(1125,290,40,40))

    if menu == 0:
        screen.blit(pallette,(920,200))
        screen.blit(blackwhite,(1095,200))
##    if menu == 1:
##        blit stamp menu stuff

    screen.blit(palletteicon,(100,10))
    for i in range(7):
        draw.rect(screen,recentColours[i],(200 + 50 * i,10,40,40))
        draw.rect(screen,recentColours[i + 7],(200 + 50 * i,60,40,40))
    
    if pencilRect.collidepoint(mx,my) and mb[0] == 1:
        rects()
        draw.rect(screen,(255,0,0),pencilRect,2)
        sel_Tool = 0
            
    if eraserRect.collidepoint(mx,my) and mb[0] == 1:
        rects()
        draw.rect(screen,(255,0,0),eraserRect,2)
        sel_Tool = 1

    if undoRect.collidepoint(mx,my) and mb[0] == 1:
        rects()
        draw.rect(screen,(255,0,0),undoRect,2)

    if redoRect.collidepoint(mx,my) and mb[0] == 1:
        rects()
        draw.rect(screen,(255,0,0),redoRect,2)

    if saveRect.collidepoint(mx,my) and mb[0] == 1:
        rects()
        draw.rect(screen,(255,0,0),saveRect,2)

    if palletteRect.collidepoint(mx,my):
        if mb[0] == 1:
            sel_Colour1 = screen.get_at((mx,my))
        if mb[2] == 1:
            sel_Colour2 = screen.get_at((mx,my))
            
    if canvas.collidepoint(mx,my):
        screen.set_clip(canvas)
        if sel_Tool == 0:
            if mb[0] == 1:
                screen.blit(back,(0,0))
                draw.line(screen,sel_Colour1,(mx,my),(omx,omy),width)
            if mb[2] == 1:
                screen.blit(back,(0,0))
                draw.line(screen,sel_Colour2,(mx,my),(omx,omy),width)
        if sel_Tool == 1:
            if mb[0] == 1:
                draw.rect(screen,(255,255,255),(mx - width / 2, my - width / 2, width , width))
            if mb[2] == 1:
                draw.rect(screen,sel_Colour2,(mx - width / 2, my - width / 2, width , width))
        screen.set_clip(None)

    display.flip()
quit()
