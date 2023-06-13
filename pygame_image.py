import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img2 = pg.transform.rotozoom(kk_img, 1, 1.0)
    kk_img3 = pg.transform.rotozoom(kk_img, 2, 1.0)
    kk_img4 = pg.transform.rotozoom(kk_img, 3, 1.0)
    kk_img5 = pg.transform.rotozoom(kk_img, 4, 1.0)
    kk_img6 = pg.transform.rotozoom(kk_img, 5, 1.0)
    kk_img7 = pg.transform.rotozoom(kk_img, 6, 1.0)
    kk_img8 = pg.transform.rotozoom(kk_img, 7, 1.0)
    kk_img9 = pg.transform.rotozoom(kk_img, 8, 1.0)
    kk_img10 = pg.transform.rotozoom(kk_img, 9, 1.0)
    kk_img11 = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_img12 = pg.transform.rotozoom(kk_img, 9, 1.0)
    kk_img13 = pg.transform.rotozoom(kk_img, 8, 1.0)
    kk_img14 = pg.transform.rotozoom(kk_img, 7, 1.0)
    kk_img15 = pg.transform.rotozoom(kk_img, 6, 1.0)
    kk_img16 = pg.transform.rotozoom(kk_img, 5, 1.0)
    kk_img17 = pg.transform.rotozoom(kk_img, 4, 1.0)
    kk_img18 = pg.transform.rotozoom(kk_img, 3, 1.0)
    kk_img19 = pg.transform.rotozoom(kk_img, 2, 1.0)
    kk_img20 = pg.transform.rotozoom(kk_img, 1, 1.0)
    kk_imgs = [kk_img, kk_img2, kk_img3, kk_img4, kk_img5, kk_img6, kk_img7, kk_img8, kk_img9, kk_img10, kk_img11, kk_img12, kk_img13, kk_img14, kk_img15, kk_img16, kk_img17, kk_img18, kk_img19, kk_img20]
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        
        screen.blit(bg_img2, [1600 -x, 0])
        screen.blit(bg_img, [3199 -x, 0])
        screen.blit(bg_img, [-x, 0])
        screen.blit(kk_imgs[tmr%20], [300,200])
        pg.display.update()
        x += 1
        tmr += 1        
        clock.tick(100)
        
        if x > 3199:
            x = 0


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()