import pygame
import os


WIDTH,HEIGHT=1000,700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Ping Pong Game-Axel Howard')

def main():


   run = True
   while run:


       for event in pygame.event.get():
           if event.type==pygame.QUIT:
               run = False
   pygame.quit()


if __name__ == "__main__":
   main()