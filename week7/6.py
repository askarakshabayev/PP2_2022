'''
pygame.mixer.music.load('1.wav')
pygame.mixer.music.play(0) # playing a song once

pygame.mixer.music.load('1.wav')
pygame.mixer.music.play(-1) # playing a song infinitely

pygame.mixer.music.queue("2.wav")
pygame.mixer.music.stop()
'''

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

pygame.mixer.music.load('test.mp3')
pygame.mixer.music.play()

SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            print('the song ended!')

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
