import pygame as pg
import pygame.draw as dw
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
pg.init()

def maskLine(ini):
    mask = ini.copy()
    for i in range(mask.shape[0]):
        iOne = np.min(np.where(mask[i] != 0)[0])
        mask[i] = np.where(i<=iOne, 0, 1) # mask é 1 quando estamos num espaço proibido
    return mask

def animate():
    L = 1080
    disp = pg.display.set_mode((L,L), pg.RESIZABLE)
    pg.display.set_caption("Teste #1")
    clk = pg.time.Clock()
    FPS = 60

    yL = 0.75*L
    R = L/100
    r = np.array([R,yL-R])
    v = np.array([40,-40])
    dw.line(disp, (255,255,255), (0,yL), (L,yL+50), 5)

    x3 = pg.surfarray.pixels3d(disp)
    ini = np.uint8(x3)[:,:,0]
    mask = maskLine(ini)
    dw.circle(disp, (255,255,255), (r[0], r[1]), R, 0)
    a = np.array([0,-10]) 

    points = [(r[0],r[1])]

    m = 1 # massa (kg)
    
    N = 200
    dt = 20/N
    
    e = 0.5

    for i in range(N):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return None
            if event.type == pg.VIDEORESIZE:
                disp = pg.display.set_mode((event.w, event.h),pg.RESIZABLE)
                L = np.min([event.h, event.w])
                yL = 0.75*L
        disp.fill((0,0,0)) # refresh fundo da pagina

        dw.line(disp, (255,255,255), (0,yL), (L,yL+50), 5)
        # na formula normal é +0.5at^2, mas no pygame o (0,0) é em cima!
        v = v - a*dt
        r = r + v*dt - 0.5*a*dt*dt
        if mask[int(r[1]), int(r[0])]==1: # em r[] estou a usar [x,y], mas o array numpy mask usa [y,x] !
            # print(np.where(mask[:,int(r[0])]==0)[0])
            r[1] = np.max(np.where(mask[:,int(r[0])]==0)[0])
            th = np.arctan2(v[1],v[0]) # angulo entre xx e trajetoria
            v[0] = np.linalg.norm(v)*np.cos(th)*np.sqrt(e)
            v[1] = -np.linalg.norm(v)*np.sin(th)*np.sqrt(e)
        points.append((r[0],r[1]))
        dw.lines(disp, (100,100,100), False, points, 2)
        dw.circle(disp, (255,255,255), (r[0], r[1]), R, 0)
        pg.display.update()
        clk.tick(FPS)
        x3 = pg.surfarray.pixels3d(disp)
        array = np.uint8(x3)
        im = Image.fromarray(array)
        im = im.save(f'C:/Users/nunop/Desktop/funCode/test1/photos/{i:04d}.png', 'PNG')


animate()
pg.quit()
