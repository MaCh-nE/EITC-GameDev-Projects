import pygame as pg
import numpy as np
import random


pg.init() 

size = ((1920,1080))
screen = pg.display.set_mode(size)
pg.display.set_caption("Testing PYGAME") 


Run = True
clock = pg.time.Clock()

# Basic colors
colors = {"BLACK" : (0,0,0) ,
"WHITE" : (255,255,255) ,
"RED" : (255,0,0) ,
"GREEN" : (0,255,0) ,
"BLUE" : (0,0,255) }

X = [(x,y) for x in np.linspace(0,size[0],20) for y in np.linspace(0,size[1],20)]

# Coordinates / radius dial lmain circle
center = [size[0]/2 , size[1]/2]
radius = size[0]/8



while Run :
    # 1 iteration dial while == 1 frame
    # Execution Block
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            Run = False 
    # Main (g) :
    screen.fill(colors["BLACK"])

    # 1- Looping circles
    C0 = [(radius*np.cos(x) + center[0] , radius*np.sin(x) + center[1]) for x in np.linspace(0,2*np.pi,75)] # main circle
    for xR in C0 :
        rdm_c = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        pg.draw.circle(screen,rdm_c,xR,100,2)

    ## 2- Curved grid
    gridage = np.linspace(0,1,40)
    for ratio in range(len(gridage)-1) :
        rdm_c = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        pg.draw.line(screen,rdm_c,[0,size[1]*gridage[ratio]],[size[0]*gridage[ratio+1],size[1]],1)
        pg.draw.line(screen,rdm_c,[size[0],size[1]*(1-gridage[ratio])],[size[0]*(1-gridage[ratio+1]),0],1)


    pg.display.flip()
    ## Horloge --> FPS 
    clock.tick(15)

pg.quit()
    
