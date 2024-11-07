import pygame as pg
import sys
from entities import PhysicsEntity
from utils import load_image,load_images
from tilemap import Tilemap

class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((800,800))
        self.display = pg.Surface((400,400))

        self.clock = pg.time.Clock()
        
        # self.img = pg.image.load('C:/Users/huy.vu-quang/Documents/pygame_project/Sprite Pack 1/Sprite Pack 1/2 - Bumpy the Robot/Idle (16 x 16).png')
        # self.image.set_colorkey((0,0,0))
        # self.img_pos = [160,260]
        self.movement = [False, False]
        
        self.collision_area = pg.Rect(50,50,300,50)
        
        self.player = PhysicsEntity(self, 'player', (50,50), (8,12))
        
        
        self.assets = {
                        'grass': load_images('tiles/grass'),
                        'dirt': load_images('tiles/dirt'),
                        'player': load_image('player.png')
                       }
        self.tilemap = Tilemap(self, tile_size =16)

    def run(self):
        while True:
            self.display.fill("skyblue")
            self.tilemap.render(self.display)
            self.player.update(self.tilemap,(self.movement[1] - self.movement[0],0))
            
            self.player.render(self.display)
            # print(self.tilemap.physics_rects_around(self.player.pos))
                        
#             img_r = pg.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
#             if img_r.colliderect(self.collision_area):
#                 pg.draw.rect(self.screen, (0,100,255), self.collision_area)
#             else:
#                 pg.draw.rect(self.screen, (0,100,155), self.collision_area)
#     
#     
#             self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
#             
#             self.screen.blit(self.img, self.img_pos)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = True
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = True                    
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = False
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = False
            
            
            self.screen.blit(pg.transform.scale(self.display,self.screen.get_size()), (0,0))

            
            pg.display.update()
            self.clock.tick(30)

Game().run()