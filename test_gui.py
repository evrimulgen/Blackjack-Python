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
bgColor = 200,0,255
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Blackjack")
screen.fill(bgColor)

b = pygame.sprite.Sprite() # create sprite
b.image = pygame.image.load("images/cards/c2.png").convert() # load ball image
b.rect = b.image.get_rect() # use image extent values
b.rect.topleft = [(width / 2), 0] # put the ball in the top left corner
#screen.blit(b.image, b.rect)
b.size = b.image.get_size()
b.bigger_img = pygame.transform.scale(b.image, (int(b.size[0]*2), int(b.size[1]*2)))
screen.blit(b.bigger_img, [(width / 2 + 25), 50])

a = pygame.sprite.Sprite() # create sprite
a.image = pygame.image.load("images/cards/back.png").convert() # load ball image
a.rect = a.image.get_rect() # use image extent values
a.rect.topleft = [(width / 2), 0] # put the ball in the top left corner
#screen.blit(b.image, b.rect)
a.size = b.image.get_size()
a.bigger_img = pygame.transform.scale(a.image, (int(a.size[0]*2), int(a.size[1]*2)))
screen.blit(a.bigger_img, [(width / 2 - 175), 50])

tux = pygame.image.load("images/cards/back.png")
x = 0
y = 0
screen.blit(tux, (200,200))


pygame.display.flip()


while True:
	x += 1
	y += 1
	if (x >= width):
		x = 0
	if (y >= height):
		y = 0
	screen.fill(bgColor)
	screen.blit(tux, (x,y))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()