import pygame as pg
import os

BASE_IMG_PATH = 'C:/Users/huy/PycharmProjects/platformer_dafluffypotato/data/images/'

def load_image(path):
    img = pg.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images


    
