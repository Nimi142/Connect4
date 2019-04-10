import pygame
from pygame import Rect
from PIL import Image
import requests
from io import BytesIO
BLACK = (0,0,0)
class Piece(pygame.sprite.Sprite):
    def __init__(self, color,x, y, x0=128, y0=128):
        self.x0 = x0
        self.y0 = y0
        self.x = x
        self.y = y
        self.color = color
        self.shape = Rect(self.x, self.y, self.x0, self.y0)
    def updateShape(self):
        self.shape = Rect(self.x,self.y,self.x0,self.y0)
    def draw(self,screen):
        self.shape = Rect(self.x, self.y, self.x0, self.y0)
        pygame.draw.rect(screen,self.color,self.shape)
class ImageBlock():
    def __init__(self, image, x, y, location):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        # self.resize()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    def resize(self):
        self.image = pygame.transform.scale(self.image,(self.x,self.y))
class Background(ImageBlock):
    def __init__(self, image, location = [0,0], x=896, y=768):
        self.image = image
        super().__init__(self.image, x, y, location)
        self.resize()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 0,0