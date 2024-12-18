#Exercício 021 - Tocando um MP3
import pygame
pygame.init()
pygame.mixer.music.load('afraid021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()