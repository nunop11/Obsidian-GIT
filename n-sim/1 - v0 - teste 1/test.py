import pygame as pg
import pygame.draw as dw
import numpy as np
from PIL import Image
pg.init()

def animate():
    L = 1080
    disp = pg.display.set_mode((L,L), pg.RESIZABLE)
    pg.display.set_caption("Teste #1")
    clk = pg.time.Clock()
    FPS = 60

    yL = 0.75*L
    R = L/100
    r = np.array([R,yL-R])
    v = np.array([50,-50])
    dw.line(disp, (255,255,255), (0,yL), (L,yL), 5)
    dw.circle(disp, (255,255,255), (r[0], r[1]), R, 0)
    a = np.array([0,-10]) 

    points = [(r[0],r[1])]

    m = 1 # massa (kg)
    
    N = 300
    dt = 50/N
    
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

        dw.line(disp, (255,255,255), (0,yL), (L,yL), 5)
        # na formula normal é +0.5at^2, mas no pygame o (0,0) é em cima!
        v = v - a*dt
        r = r + v*dt - 0.5*a*dt*dt
        if r[1]+R >= yL:
            # v[1] *= -1
            r[1] = 2*yL - r[1] - 2*R
            # th = np.arctan2(v[0],v[1]) # angulo entre xx e trajetoria
            # v[0] *= np.sqrt(e)*abs(np.cos(th))
            # v[1] *= np.sqrt(e)*abs(np.sin(th))

            th = np.arctan2(v[1],v[0]) # angulo entre xx e trajetoria
            v[0] = np.linalg.norm(v)*np.cos(th)*np.sqrt(e)
            v[1] = -np.linalg.norm(v)*np.sin(th)*np.sqrt(e)
            print(0.5*m*(np.linalg.norm(v)**2))
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

