#OlympusPaint.py
#Nikola Zjalic

#TO DO
#show the current width of line
#MAKE IMAGES TRANSPARENT

from pygame import *
from random import *
font.init()
paintFont = font.SysFont("Times New Roman", 20) #main font
omx,omy = mx,my = (0,0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getName():
    ans = ""                     # final answer will be built one letter at a time.
    tnrFont = font.SysFont("Times New Roman", 16) #times new roman font
    back = screen.copy()         # copy screen so we can replace it when done
    textArea = Rect(5,85,200,25) # make changes here.
    
    typing = True
    while typing:
        for e in event.get():          
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""          
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    
        txtPic = tnrFont.render(ans, True, (240,120,40))
        draw.rect(screen,(81,52,22),textArea)        # draw the text window and the text.
        draw.rect(screen,(120,80,50),textArea,2)
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))        
        display.flip()
        
    screen.blit(back,(0,0))
    return ans


def ffill(x,y,fc,rc):
    if fc != rc:
        points = [(x,y)]
        while len(points) > 0:
            x,y = points.pop()  #takes last element in the list
            if 0 < x < 980 and 0 < y < 750 and screen.get_at((x,y))[:3] == rc:  #check if (x,y) is
                screen.set_at((x,y),fc)
                points += [(x + 1,y), (x - 1, y), (x, y + 1), (x, y - 1)]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LOAD IMAGES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#IMPORTANT STUFF
background = image.load("images/background.jpg")
toolbox = image.load("images/toolbox.png")
pallette = image.load("images/pallette.png")
tooloptions = image.load("images/tooloptions.png")
styleoptions = image.load("images/shapestyleoptions.png")
stampoptions = image.load("images/stampoptions.png")
saveloadrects = image.load("images/saveloadrects.png")
mxyrect = image.load("images/mxyrect.png")

#TOOLS(HOVER)
eyedropperhover = image.load("images/eyedropperhover.png")
eraserhover = image.load("images/eraserhover.png")
pencilhover = image.load("images/pencilhover.png")
linehover = image.load("images/linehover.png")
paintbrushhover = image.load("images/paintbrushhover.png")
paintcanhover = image.load("images/paintcanhover.png")
spraycanhover = image.load("images/spraycanhover.png")
stampshover = image.load("images/stampshover.png")
boxhover = image.load("images/boxhover.png")
ellipsehover = image.load("images/ellipsehover.png")
undohover = image.load("images/undohover.png")
redohover = image.load("images/redohover.png")
savehover = image.load("images/savehover.png")
loadhover = image.load("images/loadhover.png")

#TOOLS(SELECTED)
eyedropperselected = image.load("images/eyedropperselected.png")
eraserselected = image.load("images/eraserselected.png")
pencilselected = image.load("images/pencilselected.png")
lineselected = image.load("images/lineselected.png")
paintbrushselected = image.load("images/paintbrushselected.png")
paintcanselected = image.load("images/paintcanselected.png")
spraycanselected = image.load("images/spraycanselected.png")
stampsselected = image.load("images/stampsselected.png")
boxselected = image.load("images/boxselected.png")
ellipseselected = image.load("images/ellipseselected.png")

#BOX, ELLIPSE STYLE ICONS
style1hover = image.load("images/style1hover.png")
style2hover = image.load("images/style2hover.png")
style3hover = image.load("images/style3hover.png")
style1selected = image.load("images/style1selected.png")
style2selected = image.load("images/style2selected.png")
style3selected = image.load("images/style3selected.png")

#STAMPS(THE ONES BEING BLITTED TO THE CANVAS)
stamp1 = image.load("images/stamp1.png")
stamp2 = image.load("images/stamp2.png")
stamp3 = image.load("images/stamp3.png")
stamp4 = image.load("images/stamp4.png")
stamp5 = image.load("images/stamp5.png")
stamp6 = image.load("images/stamp6.png")
stamp7 = image.load("images/stamp7.png")
stamp8 = image.load("images/stamp8.png")

#STAMP ICONS(HOVER)
stamp1hover = image.load("images/stamp1hover.png")
stamp2hover = image.load("images/stamp2hover.png")
stamp3hover = image.load("images/stamp3hover.png")
stamp4hover = image.load("images/stamp4hover.png")
stamp5hover = image.load("images/stamp5hover.png")
stamp6hover = image.load("images/stamp6hover.png")
stamp7hover = image.load("images/stamp7hover.png")
stamp8hover = image.load("images/stamp8hover.png")

#STAMP ICONS(SELECTED)
stamp1selected = image.load("images/stamp1selected.png")
stamp2selected = image.load("images/stamp2selected.png")
stamp3selected = image.load("images/stamp3selected.png")
stamp4selected = image.load("images/stamp4selected.png")
stamp5selected = image.load("images/stamp5selected.png")
stamp6selected = image.load("images/stamp6selected.png")
stamp7selected = image.load("images/stamp7selected.png")
stamp8selected = image.load("images/stamp8selected.png")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RECTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#IMPORTANT
canvasRect = Rect(135,115,840,630)
tooloptionRect = Rect(5,545,125,200)

#BOX, ELLIPSE STYLE RECTS
shapestyleRect1 = Rect(10,550,115,60) 
shapestyleRect2 = Rect(10,615,115,60)
shapestyleRect3 = Rect(10,680,115,60)

#TOOLBOX RECTS
saveRect = Rect(5,115,60,35)
loadRect = Rect(70,115,60,35)
eyedropRect = Rect(5,155,60,60)
eraserRect = Rect(70,155,60,60)
pencilRect = Rect(5,220,60,60)
lineRect = Rect(70,220,60,60)
paintbrushRect = Rect(5,285,60,60)
paintcanRect = Rect(70,285,60,60)
spraycanRect = Rect(5,350,60,60)
stampsRect = Rect(70,350,60,60)
boxRect = Rect(5,415,60,60)
ellipseRect = Rect(70,415,60,60)
undoRect = Rect(5,480,60,60)
redoRect = Rect(70,480,60,60)

#STAMP ICON RECTS
stamp1Rect = Rect(10,550,55,40)
stamp2Rect = Rect(70,550,55,40)
stamp3Rect = Rect(10,595,55,45)
stamp4Rect = Rect(70,595,55,45)
stamp5Rect = Rect(10,645,55,45)
stamp6Rect = Rect(70,645,55,45)
stamp7Rect = Rect(10,695,55,45)
stamp8Rect = Rect(70,695,55,45)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BASIC PAINT SET-UP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

screen = display.set_mode((980, 750))
display.set_caption ("Olympus Paint")
screen.blit(background,(-35,-30))
draw.rect(screen,(255,255,255),canvasRect)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOOL VARIABLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

width = 10
#width of the selected tool

shapestyle = 1 #options for the box and ellipse tools
#1 = no fill
#2 = fill
#3 = fill w/ colour

sel_Stamp = 1
#1 = logo
#2 = icon
#3 = symbol
#4 = kratos 1
#5 = kratos 2
#6 = chaos blade
#7 = blade of exile
#8 = cestus

sel_Tool = 2
#0 = eye drop tool
#1 = eraser
#2 = pencil
#3 = line
#4 = paint brush
#5 = paint can
#6 = spray can
#7 = stamps 
#8 = box
#9 = ellipse

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LIST RELATED STUFF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

back = screen.subsurface(canvasRect).copy()   #copy of canvasRect
undo = []
redo = []
recentColours = []
recentColRects = []
undo.append(back) 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~COLOUR RELATED STUFF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sel_Colour1 = (0,0,0)       #Left click colour
sel_Colour2 = (255,255,255) #Right click colour

for i in range(14):
    recentColours.append((255,255,255))    

for i in range(7):
    recentColRects.append(Rect(655 + i * 45,15,40,40))
for i in range(7):
    recentColRects.append(Rect(655 + i * 45,60,40,40))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EVENT LOOP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
                
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1 or evt.button == 3:
                back = screen.subsurface(canvasRect).copy() #take a copy of canvasRect everytime user left or right clicks
                omx, omy = evt.pos       #old mx, old my - used for drawing and dragging lines

            #PAINTCAN
            if canvasRect.collidepoint(mx,my) and sel_Tool == 5:
                if evt.button == 1:
                    ffill(omx,omy,sel_Colour1,screen.get_at((omx,omy)))               
                if evt.button == 3:
                    ffill(omx,omy,sel_Colour2,screen.get_at((omx,omy)))

            if evt.button == 1:
                if undoRect.collidepoint(mx,my) and len(undo) > 1:
                    redo.append(undo[-1])
                    undo = undo[:-1]
                    screen.blit(undo[-1],(135,115))
                    
                if redoRect.collidepoint(mx,my) and len(redo) > 0:
                    undo.append(redo[-1])
                    redo = redo[:-1]
                    screen.blit(undo[-1],(135,115))
                    
                if canvasRect.collidepoint(omx,omy) and sel_Tool > 0:
                    redo = []
                
                if saveRect.collidepoint(mx,my):
                    name = getName()
                    if name != "":
                        image.save(back,name + ".png")
                    
                if loadRect.collidepoint(mx,my):
                    name = getName()
                    if name != "":
                        loadimage = image.load(name + ".png")
                        screen.blit(loadimage,(135,115))        

            if evt.button == 4:
                if width < 50:
                     width += 1
            if evt.button == 5:
                if width > 1:
                     width -= 1
                    
        if evt.type == MOUSEBUTTONUP:
            
            if canvasRect.collidepoint(omx,omy) and evt.button == 1 or canvasRect.collidepoint(omx,omy) and evt.button == 3: 
                undo.append(screen.subsurface(canvasRect).copy())
                
            if sel_Tool == 0 and tooloptionRect.collidepoint(mx,my) or sel_Tool == 0 and canvasRect.collidepoint(mx,my):
                if evt.button == 1:
                    recentColours = [sel_Colour1] + recentColours[0:14]
                if evt.button == 3:
                    recentColours = [sel_Colour2] + recentColours[0:14]

            if evt.button == 1 and evt.button == 3:
                omx,omy = (0,0)
                
#                                                                             MAIN LOOP
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MISC~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    
    #Draws the recent colour rects and the current colour rects at the top of the screen.
    for i in range(7):
        draw.rect(screen,recentColours[i],(655 + i * 45,15,40,40))
        draw.rect(screen,recentColours[i + 7],(655 + i * 45,60,40,40))        
    draw.rect(screen,sel_Colour2,(580,40,50,50))
    draw.rect(screen,sel_Colour1,(560,20,50,50))
    
    #Changes sel_Colour1 or sel_Colour2 according to the colour in the recentColRect
    for i in range(14):
        if recentColRects[i].collidepoint(mx,my) and canvasRect.collidepoint(omx,omy) == False:
            if mb[0] == 1:
                sel_Colour1 = recentColours[i]
            if mb[2] == 1:
                sel_Colour2 = recentColours[i]

    screen.blit(mxyrect,(400,80))  #blit (x,y) coordinates of the mouse on to the screen.
    if canvasRect.collidepoint(mx,my):
        mouse_Pos = paintFont.render(("(" + str(mx - 135) + " , " + str(my - 115) + ")"), True, (240,120,40))
        screen.blit(mouse_Pos,(417,82))
    
    screen.blit(toolbox,(5,155))  #blits toolbox and save & load images
    screen.blit(saveloadrects,(5,115))                       
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOOL SELECTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    if canvasRect.collidepoint(omx,omy) == False: #check if omx,omy is in the canvas. this is to prevent tool or colour selection if user accidently exits
                                                  #the canvas while drawing. this is where the selected tool is changed and tool hover icons are blitted. 
        if eyedropRect.collidepoint(mx,my) and sel_Tool != 0:
            screen.blit(eyedropperhover,(5,155))
            if mb[0] == 1:
                sel_Tool = 0
                
        if eraserRect.collidepoint(mx,my) and sel_Tool != 1:
            screen.blit(eraserhover,(70,155))
            if mb[0] == 1:
                sel_Tool = 1
                
        if pencilRect.collidepoint(mx,my) and sel_Tool != 2:
            screen.blit(pencilhover,(5,220))
            if mb[0] == 1:
                sel_Tool = 2
                
        if lineRect.collidepoint(mx,my) and sel_Tool != 3:
            screen.blit(linehover,(70,220))
            if mb[0] == 1:
                sel_Tool = 3
                
        if paintbrushRect.collidepoint(mx,my) and sel_Tool != 4:
            screen.blit(paintbrushhover,(5,285))
            if mb[0] == 1:
                sel_Tool = 4
                
        if paintcanRect.collidepoint(mx,my) and sel_Tool != 5:
            screen.blit(paintcanhover,(70,285))
            if mb[0] == 1:
                sel_Tool = 5
                
        if spraycanRect.collidepoint(mx,my) and sel_Tool != 6:
            screen.blit(spraycanhover,(5,350))
            if mb[0] == 1:
                sel_Tool = 6
                
        if stampsRect.collidepoint(mx,my) and sel_Tool != 7:
            screen.blit(stampshover,(70,350))
            if mb[0] == 1:
                sel_Tool = 7
                
        if boxRect.collidepoint(mx,my) and sel_Tool != 8:
            screen.blit(boxhover,(5,415))
            if mb[0] == 1:
                sel_Tool = 8
                
        if ellipseRect.collidepoint(mx,my) and sel_Tool != 9:
            screen.blit(ellipsehover,(70,415))
            if mb[0] == 1:
                sel_Tool = 9
                
        if undoRect.collidepoint(mx,my):
            screen.blit(undohover,(5,480))
            
        if redoRect.collidepoint(mx,my):
            screen.blit(redohover,(70,480))

        if saveRect.collidepoint(mx,my):
            screen.blit(savehover,(5,115))

        if loadRect.collidepoint(mx,my):
            screen.blit(loadhover,(70,115))
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOOL OPTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
    if sel_Tool == 0:   #blit tool selected images and the a tool options box according to the selected tool.
        screen.blit(eyedropperselected,(5,155))
        screen.blit(pallette,(5,545))
        if tooloptionRect.collidepoint(mx,my):
            if mb[0] == 1:
                sel_Colour1 = screen.get_at((mx,my))
            if mb[2] == 1:
                sel_Colour2 = screen.get_at((mx,my))
                
    if sel_Tool == 1:
        screen.blit(eraserselected,(70,155))
        screen.blit(tooloptions,(5,545))
        
    if sel_Tool == 2:
        screen.blit(pencilselected,(5,220))
        screen.blit(tooloptions,(5,545))
        
    if sel_Tool == 3:
        screen.blit(lineselected,(70,220))
        screen.blit(tooloptions,(5,545))
        
    if sel_Tool == 4:
        screen.blit(paintbrushselected,(5,285))
        screen.blit(tooloptions,(5,545))
        
    if sel_Tool == 5:
        screen.blit(paintcanselected,(70,285))
        screen.blit(tooloptions,(5,545))
        
    if sel_Tool == 6:
        screen.blit(spraycanselected,(5,350))
        screen.blit(tooloptions,(5,545))
        
    if sel_Tool == 7:
        screen.blit(stampsselected,(70,350))
        screen.blit(stampoptions,(5,545))
        if canvasRect.collidepoint(omx,omy) == False:
            
            if stamp1Rect.collidepoint(mx,my) and sel_Stamp != 1:
                screen.blit(stamp1hover,(10,550))
                if mb[0] == 1:
                    sel_Stamp = 1                   
            if stamp2Rect.collidepoint(mx,my) and sel_Stamp != 2:
                screen.blit(stamp2hover,(70,550))
                if mb[0] == 1:
                    sel_Stamp = 2                   
            if stamp3Rect.collidepoint(mx,my) and sel_Stamp != 3:
                screen.blit(stamp3hover,(10,595))
                if mb[0] == 1:
                    sel_Stamp = 3
            if stamp4Rect.collidepoint(mx,my) and sel_Stamp != 4:
                screen.blit(stamp4hover,(70,595))
                if mb[0] == 1:
                    sel_Stamp = 4
            if stamp5Rect.collidepoint(mx,my) and sel_Stamp != 5:
                screen.blit(stamp5hover,(10,645))
                if mb[0] == 1:
                    sel_Stamp = 5
            if stamp6Rect.collidepoint(mx,my) and sel_Stamp != 6:
                screen.blit(stamp6hover,(70,645))
                if mb[0] == 1:
                    sel_Stamp = 6
            if stamp7Rect.collidepoint(mx,my) and sel_Stamp != 7:
                screen.blit(stamp7hover,(10,695))
                if mb[0] == 1:
                    sel_Stamp = 7
            if stamp8Rect.collidepoint(mx,my) and sel_Stamp != 8:
                screen.blit(stamp8hover,(70,695))
                if mb[0] == 1:
                    sel_Stamp = 8
                
        if sel_Stamp == 1:
            screen.blit(stamp1selected,(10,550))
        if sel_Stamp == 2:
            screen.blit(stamp2selected,(70,550))
        if sel_Stamp == 3:
            screen.blit(stamp3selected,(10,595))
        if sel_Stamp == 4:
            screen.blit(stamp4selected,(70,595))
        if sel_Stamp == 5:
            screen.blit(stamp5selected,(10,645))
        if sel_Stamp == 6:
            screen.blit(stamp6selected,(70,645))
        if sel_Stamp == 7:
            screen.blit(stamp7selected,(10,695)) 
        if sel_Stamp == 8:
            screen.blit(stamp8selected,(70,695))
            
    if sel_Tool == 8:
        screen.blit(boxselected,(5,415))
        screen.blit(styleoptions,(5,545))
        if canvasRect.collidepoint(omx,omy) == False:
            
            if shapestyleRect1.collidepoint(mx,my) and shapestyle != 1:
                screen.blit(style1hover,(10,550))
                if mb[0] == 1:
                    shapestyle = 1                  
            if shapestyleRect2.collidepoint(mx,my) and shapestyle != 2:
                screen.blit(style2hover,(10,615))
                if mb[0] == 1:
                    shapestyle = 2
            if shapestyleRect3.collidepoint(mx,my) and shapestyle != 3:
                screen.blit(style3hover,(10,680))
                if mb[0] == 1:
                    shapestyle = 3

        if shapestyle == 1:
            screen.blit(style1selected,(10,550))
        if shapestyle == 2:
            screen.blit(style2selected,(10,615))
        if shapestyle == 3:
            screen.blit(style3selected,(10,680))
        
    if sel_Tool == 9:
        screen.blit(ellipseselected,(70,415))
        screen.blit(styleoptions,(5,545))
        if canvasRect.collidepoint(omx,omy) == False:
            
            if shapestyleRect1.collidepoint(mx,my) and shapestyle != 1:
                screen.blit(style1hover,(10,550))
                if mb[0] == 1:
                    shapestyle = 1
            if shapestyleRect2.collidepoint(mx,my) and shapestyle != 2:
                screen.blit(style2hover,(10,615))
                if mb[0] == 1:
                    shapestyle = 2
            if shapestyleRect3.collidepoint(mx,my) and shapestyle != 3:
                screen.blit(style3hover,(10,680))
                if mb[0] == 1:
                    shapestyle = 3

        if shapestyle == 1:
            screen.blit(style1selected,(10,550))
        if shapestyle == 2:
            screen.blit(style2selected,(10,615))
        if shapestyle == 3:
            screen.blit(style3selected,(10,680))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CANVAS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
         
        #EYEDROPPER
        if sel_Tool == 0:
            if mb[0] == 1:
                sel_Colour1 = screen.get_at((mx,my))
                
            if mb[2] == 1:
                sel_Colour2 = screen.get_at((mx,my))
                
        #ERASER
        if sel_Tool == 1:
            if mb[0] == 1 or mb[2] == 1:
                draw.rect(screen,(255,255,255),(omx - width / 2, omy - width/2,width,width))
                dist = (((omx - mx) ** 2 + (omy - my) ** 2)) ** 0.5
                for i in range(int(dist)):          # circle is drawn on every point on the line between omx,omy and mx,my.
                    sx = i * (omx - mx) / dist      # (sx,sy) is a coordinate that lies on the line between omx,omy and mx,my. this is where we draw the circle
                    sx = i * (omx - mx) / dist
                    sy = i * (omy - my) / dist
                    draw.rect(screen,(255,255,255),(omx - int(sx) - width / 2, omy - int(sy) - width/2,width,width))
                omx,omy = mx,my
                
        #PENCIL
        if sel_Tool == 2:           
            if mb[0] == 1:
                draw.line(screen,sel_Colour1,(omx,omy),(mx,my))
                omx,omy = mx,my
                
            if mb[2] == 1:
                draw.line(screen,sel_Colour2,(omx,omy),(mx,my))
                omx,omy = mx,my
                
        #LINE
        if sel_Tool == 3:           
            if mb[0] == 1:
                screen.blit(back,(135,115))
                draw.line(screen,sel_Colour1, (omx,omy),(mx,my),width)
                
            if mb[2] == 1:
                screen.blit(back,(135,115))
                draw.line(screen,sel_Colour2, (omx,omy),(mx,my),width)
                
        #PAINTBRUSH
        if sel_Tool == 4:
            if mb[0] == 1:
                draw.circle(screen,sel_Colour1,(omx,omy),width)
                dist = (((omx - mx) ** 2 + (omy - my) ** 2)) ** 0.5
                for i in range(int(dist)):          # circle is drawn on every point on the line between omx,omy and mx,my.
                    sx = i * (omx - mx) / dist      # (sx,sy) is a coordinate that lies on the line between omx,omy and mx,my. this is where we draw the circle
                    sy = i * (omy - my) / dist
                    draw.circle(screen,sel_Colour1,(omx - int(sx), omy - int(sy)),width)
                omx,omy = mx,my
                
            if mb[2] == 1:
                dist = (((omx - mx) ** 2 + (omy - my) ** 2)) ** 0.5
                for i in range(int(dist)):        
                    sx = i * (omx - mx) / dist
                    sy = i * (omy - my) / dist
                    draw.circle(screen,sel_Colour2,(omx - int(sx), omy - int(sy)),width)
                omx,omy = mx,my
                    
        
        #SPRAY CAN
        if sel_Tool == 6:           
            if mb[0] == 1:
                for i in range(width):
                    xpos = randint(width * -1, width)  #xpos and ypos are offset points from mx,my
                    ypos = randint(width * -1, width)
                    if xpos ** 2 + ypos ** 2 <= width ** 2:  #use equation of a circle to check if the point lies within the circle
                        screen.set_at((mx + xpos, my + ypos),sel_Colour1)
                    
            if mb[2] == 1:
                for i in range(width):
                    xpos = randint(width * -1, width)
                    ypos = randint(width * -1, width)
                    if xpos ** 2 + ypos ** 2 <= width ** 2:
                        screen.set_at((mx + xpos, my + ypos),sel_Colour2)
                    
        #STAMPS
        if sel_Tool == 7:
            if mb[0] == 1 or mb[2] == 1:
                screen.blit(back,(135,115))
                if sel_Stamp == 1:
                    screen.blit(stamp1,(mx - 187, my - 50))
                if sel_Stamp == 2:
                    screen.blit(stamp2,(mx - 61, my - 60))
                if sel_Stamp == 3:
                    screen.blit(stamp3,(mx - 38, my - 38))
                if sel_Stamp == 4:
                    screen.blit(stamp4,(mx - 115, my - 100))
                if sel_Stamp == 5:
                    screen.blit(stamp5,(mx - 100, my - 126))
                if sel_Stamp == 6:
                    screen.blit(stamp6,(mx - 105, my - 50))
                if sel_Stamp == 7:
                    screen.blit(stamp7,(mx - 86, my - 50)) 
                if sel_Stamp == 8:
                    screen.blit(stamp8,(mx - 67, my - 50))
                    
        #BOX
        if sel_Tool == 8:
            if width % 2 == 0:
                corner = 1    #'corner' is added to fix the corners of the rectangles when width is an odd integer.
            else:
                corner = 0
                
            if mb[0] == 1:
                screen.blit(back,(135,115))
                if mx > omx:
                    
                    if shapestyle == 1:  #empty
                        draw.line(screen,sel_Colour1,(omx,omy),(omx,my),width)
                        draw.line(screen,sel_Colour1,(omx - width / 2 + corner,omy),(mx + width / 2,omy),width)
                        draw.line(screen,sel_Colour1,(omx - width / 2 + corner,my),(mx + width / 2,my),width)
                        draw.line(screen,sel_Colour1,(mx,omy),(mx,my),width)
                    if shapestyle == 2:  #filled
                        draw.rect(screen,sel_Colour1,(omx,omy,mx - omx,my - omy))
                    if shapestyle == 3:  #coloured
                        draw.rect(screen,sel_Colour2,(omx,omy,mx - omx,my - omy))
                        draw.line(screen,sel_Colour1,(omx,omy),(omx,my),width)
                        draw.line(screen,sel_Colour1,(omx - width / 2 + corner,omy),(mx + width / 2,omy),width)
                        draw.line(screen,sel_Colour1,(omx - width / 2 + corner,my),(mx + width / 2,my),width)
                        draw.line(screen,sel_Colour1,(mx,omy),(mx,my),width)
                        
                if mx < omx:
                    if shapestyle == 1:  #empty
                        draw.line(screen,sel_Colour1,(omx,omy),(omx,my),width)
                        draw.line(screen,sel_Colour1,(omx + width / 2,omy),(mx - width / 2 + corner,omy),width)
                        draw.line(screen,sel_Colour1,(omx + width / 2,my),(mx - width / 2 + corner,my),width)
                        draw.line(screen,sel_Colour1,(mx,omy),(mx,my),width)
                    if shapestyle == 2:  #filled
                        draw.rect(screen,sel_Colour1,(omx,omy,mx - omx,my - omy))
                    if shapestyle == 3:  #coloured
                        draw.rect(screen,sel_Colour2,(omx,omy,mx - omx,my - omy))
                        draw.line(screen,sel_Colour1,(omx,omy),(omx,my),width)
                        draw.line(screen,sel_Colour1,(omx + width / 2,omy),(mx - width / 2 + corner,omy),width)
                        draw.line(screen,sel_Colour1,(omx + width / 2,my),(mx - width / 2 + corner,my),width)
                        draw.line(screen,sel_Colour1,(mx,omy),(mx,my),width)
                    
            if mb[2] == 1:
                screen.blit(back,(135,115))
                
                if mx > omx:
                    if shapestyle == 1:   #empty
                        draw.line(screen,sel_Colour2,(omx,omy),(omx,my),width)
                        draw.line(screen,sel_Colour2,(omx - width / 2 + corner,omy),(mx + width / 2,omy),width)
                        draw.line(screen,sel_Colour2,(omx - width / 2 + corner,my),(mx + width / 2,my),width)
                        draw.line(screen,sel_Colour2,(mx,omy),(mx,my),width)
                    if shapestyle == 2:   #filled
                        draw.rect(screen,sel_Colour2,(omx,omy,mx - omx,my - omy))
                    if shapestyle == 3:   #coloured
                        draw.rect(screen,sel_Colour1,(omx,omy,mx - omx,my - omy))
                        draw.line(screen,sel_Colour2,(omx,omy),(omx,my),width)
                        draw.line(screen,sel_Colour2,(omx - width / 2 + corner,omy),(mx + width / 2,omy),width)
                        draw.line(screen,sel_Colour2,(omx - width / 2 + corner,my),(mx + width / 2,my),width)
                        draw.line(screen,sel_Colour2,(mx,omy),(mx,my),width)
                        
                if mx < omx:
                    if shapestyle == 1:   #empty
                        draw.line(screen,sel_Colour2,(omx,omy),(omx,my),width)
                        draw.line(screen,sel_Colour2,(omx + width / 2,omy),(mx - width / 2 + corner,omy),width)
                        draw.line(screen,sel_Colour2,(omx + width / 2,my),(mx - width / 2 + corner,my),width)
                        draw.line(screen,sel_Colour2,(mx,omy),(mx,my),width)
                    if shapestyle == 2:   #filled
                        draw.rect(screen,sel_Colour2,(omx,omy,mx - omx,my - omy))
                    if shapestyle == 3:   #coloured
                        draw.rect(screen,sel_Colour1,(omx,omy,mx - omx,my - omy))
                        draw.line(screen,sel_Colour2,(omx,omy),(omx,my),width)
                        draw.line(screen,sel_Colour2,(omx + width / 2,omy),(mx - width / 2 + corner,omy),width)
                        draw.line(screen,sel_Colour2,(omx + width / 2,my),(mx - width / 2 + corner,my),width)
                        draw.line(screen,sel_Colour2,(mx,omy),(mx,my),width)
                    
        #ELLIPSE
        if sel_Tool == 9:              
            if mb[0] == 1:
                screen.blit(back,(135,115))
                
                if shapestyle == 1:   #empty
                    x_small = min(omx,mx)       #For the ellipse tool, we must draw from the smaller point to the bigger point otherwise the program will crash.
                    x_big = max(omx,mx)         #We use min and max to find out the larger of omx,mx and omy,my. An if statement is used to make sure the width is not
                    y_small = min(omy,my)       #greater than the ellipse radius or else the program will crash.
                    y_big = max(omy,my)
                    if (x_big - x_small) / 2 > width and (y_big - y_small) / 2 > width:
                        draw.ellipse(screen,sel_Colour1,(x_small, y_small, x_big - x_small, y_big - y_small),width)
                    else:
                        draw.ellipse(screen,sel_Colour1,(x_small, y_small, x_big - x_small, y_big - y_small))
                        
                if shapestyle == 2:   #fill
                    x_small = min(omx,mx)
                    x_big = max(omx,mx)
                    y_small = min(omy,my)
                    y_big = max(omy,my)
                    draw.ellipse(screen,sel_Colour1,(x_small, y_small, x_big - x_small, y_big - y_small))
                    
                if shapestyle == 3:   #coloured
                    x_small = min(omx,mx)
                    x_big = max(omx,mx)
                    y_small = min(omy,my)
                    y_big = max(omy,my)
                    if (x_big - x_small) / 2 > width and (y_big - y_small) / 2 > width:
                        draw.ellipse(screen,sel_Colour2,(x_small,y_small, x_big - x_small, y_big - y_small))
                        draw.ellipse(screen,sel_Colour1,(x_small,y_small, x_big - x_small, y_big - y_small),width)
                    else:
                        draw.ellipse(screen,sel_Colour1,(x_small, y_small, x_big - x_small, y_big - y_small))
                        
            if mb[2] == 1:
                screen.blit(back,(135,115))
                
                if shapestyle == 1:   #empty
                    x_small = min(omx,mx)
                    x_big = max(omx,mx)
                    y_small = min(omy,my)
                    y_big = max(omy,my)
                    if (x_big - x_small) / 2 > width and (y_big - y_small) / 2 > width:
                        draw.ellipse(screen,sel_Colour2,(x_small,y_small, x_big - x_small , y_big - y_small),width)
                    else:
                        draw.ellipse(screen,sel_Colour2,(x_small, y_small, x_big - x_small, y_big - y_small))
                        
                if shapestyle == 2:   #filled
                    x_small = min(omx,mx)
                    x_big = max(omx,mx)
                    y_small = min(omy,my)
                    y_big = max(omy,my)
                    draw.ellipse(screen,sel_Colour2,(x_small,y_small, x_big - x_small, y_big - y_small))
                    
                if shapestyle == 3:   #coloured
                    x_small = min(omx,mx)
                    x_big = max(omx,mx)
                    y_small = min(omy,my)
                    y_big = max(omy,my)
                    if (x_big - x_small) / 2 > width and (y_big - y_small) / 2 > width:
                        draw.ellipse(screen,sel_Colour1,(x_small,y_small, x_big - x_small, y_big - y_small))
                        draw.ellipse(screen,sel_Colour2,(x_small,y_small, x_big - x_small, y_big - y_small),width)
                    else:
                        draw.ellipse(screen,sel_Colour2,(x_small, y_small, x_big - x_small, y_big - y_small))

    screen.set_clip(None)       
    display.flip()
font.quit()
del paintFont
quit()
