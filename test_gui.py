import pygame
from pygame.locals import KEYDOWN
import os
import sys

def imageLoad(name, card):    
    if card == 1:
        fullname = os.path.join("images/cards/", name)
    else: fullname = os.path.join('images', name)
    
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    
    return image, image.get_rect()	
	
width  = 1250
height = 800
size   = [width, height]
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Blackjack")
background, backgroundRect = imageLoad("background.png", 0)

b = pygame.sprite.Sprite() # create sprite
b.image = pygame.image.load("images/cards/c2.png").convert() # load ball image
b.rect = b.image.get_rect() # use image extent values
b.rect.topleft = [(width / 2), 0] # put the ball in the top left corner
screen.blit(background, backgroundRect)
screen.blit(b.image, b.rect)
b.size = b.image.get_size()
b.bigger_img = pygame.transform.scale(b.image, (int(b.size[0]*2), int(b.size[1]*2)))
screen.blit(b.bigger_img, [100,100])

while True:
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()