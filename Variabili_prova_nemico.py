#!/usr/bin/python
# coding=utf-8

import pygame
import random


# colori (rosso, verde, blu, ecc..)

nero = (0, 0, 0)
rosso = (255, 0, 0)
bianco = (255, 255, 255)
verde = (0, 225, 0)
blu = (18, 10, 153)
giallo = (255, 216, 0)

# si inizializza il gioco
pygame.init()

infoObject = pygame.display.Info()
schermo = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

# musica gioco
m_gioco = pygame.mixer.Sound('inizio.wav')

# aggiunta suono cattura nemico
cattura = pygame.mixer.Sound('cattura1.wav')

# avviso
avviso = pygame.mixer.Sound('avviso.wav')

# suono collisione muro
preso = pygame.mixer.Sound('preso3.wav')

# uscita gioco
schianto = pygame.mixer.Sound('uscita1.wav')

# suono collisione cratere
lapide = pygame.mixer.Sound('morte6.wav')

# suono record
applauso = pygame.mixer.Sound('allarme1.wav')

# aggiungo lo sfondo
sfondo = pygame.image.load('sfondo4.jpg')

# sfondo intro gioco
sfondo1 = pygame.image.load('intro.jpg')

# sfondo seleziona
sfondo2 = pygame.image.load('seleziona.jpg')

# icona gioco
pygame.display.set_icon(pygame.image.load('supermen1.png'))

# qui si inserisce il titolo nello schermo gioco
pygame.display.set_caption('SE MI FAI MANGIARE ......ATTENTO...........')

# immagine giocatore
immagine = pygame.image.load('giocatore.png')

# immagini (smile da mangiare)
immagine1 = pygame.image.load('prendimi3.png')
immagine2 = pygame.image.load('prendimi4.png')
immagine3 = pygame.image.load('prendimi5.png')
immagine4 = pygame.image.load('prendimi6.png')
immagine5 = pygame.image.load('prendimi7.png')
immagine6 = pygame.image.load('prendimi8.png')
immagine7 = pygame.image.load('prendimi9.png')
immagine8 = pygame.image.load('prendimi10.png')
immagine9 = pygame.image.load('prendimi11.png')
immagine10 = pygame.image.load('prendimi12.png')
immagine11 = pygame.image.load('prendimi13.png')
immagine12 = pygame.image.load('prendimi14.png')
immagine13 = pygame.image.load('prendimi15.png')
immagine14 = pygame.image.load('prendimi16.png')
immagine15 = pygame.image.load('prendimi17.png')
immagine16 = pygame.image.load('prendimi18.png')

# immagine tranello 1
cratere1 = pygame.image.load('morte2.png')

# immagine tranello 2
cratere2 = pygame.image.load('morte2.png')

# immagine tranello 3
cratere3 = pygame.image.load('morte2.png')

# palla
simpatica = pygame.image.load('simpatica.png')
simpatica1 = pygame.image.load('teschio2.png')
simpatica2 = pygame.image.load('teschio2.png')
simpatica3 = pygame.image.load('simpatica3.png')
simpatica4 = pygame.image.load('simpatica5.png')
simpatica5 = pygame.image.load('simpatica2.png')

# palla che ti corre dietro
nerone = pygame.image.load('teschio2.png')
nerone1 = pygame.image.load('nero1.png')

# serve per ottimizzare il gioco
clock = pygame.time.Clock()

# velocita gioco
velocita = 60

direzione = 'right'
piccoloFont = pygame.font.SysFont('comicsansms', 30)
medioFont = pygame.font.SysFont('comicsansms', 50)
grandeFont = pygame.font.SysFont('comicsansms', 80)
oggetto = 10 # velocita giocatore
oggetto_n = 32 # grandezza smile da recuperare
gran_c = 23 # grandezza lapide
palla = 25 # grandezza palla

# muro orrizzontale 0
x11 = infoObject.current_h
y11 = random.randint(0, infoObject.current_w)
x12 = 50
y12 = 50
xl_velocita11 = 4

# muro orrizzontale 1
x14 = infoObject.current_h
y14 = random.randint(0, infoObject.current_w)
x13 = 50
y13 = 50
xl_velocita12 = 4

# contorno destro
xl0 = infoObject.current_w-100
yl0 = 0
xs0 = 30
ys0 = infoObject.current_h

# contorno sinistro
xl1 = infoObject.current_w > infoObject.current_w
yl1 = 0
xs1 = 30
ys1 = infoObject.current_h

# contorno superiore
xl2 = 0
yl2 = 0
xs2 = infoObject.current_w
ys2 = infoObject.current_h - infoObject.current_h+30

# contorno inferiore
xl3 = 0
yl3 = infoObject.current_h-90
xs3 = infoObject.current_w
ys3 = infoObject.current_h


# palla
x = infoObject.current_w
y = 0
vx = palla
vy = palla

# palla 1
x1 = 0
y1 = infoObject.current_w/2
vx1 = palla
vy1 = palla

# palla 2
x2 = infoObject.current_h
y2 = 0
vx2 = palla
vy2 = palla

# palla 3
x3 = infoObject.current_w
y3 = 0
vx3 = palla
vy3 = palla

# palla 4
x4 = 0
y4 = infoObject.current_w
vx4 = palla
vy4 = palla

# palla 7
x7 = 0
y7 = infoObject.current_h
vx7 = palla
vy7 = palla

# palla che ti corre dietro
x5 = infoObject.current_w
y5 = 0
x_posizione = 'right'
palla1 = 25

# palla che ti corre dietro
x6 = 50
y6 = infoObject.current_h
x_posizione1 = 'right'
palla2 = 25

# parametri muro (ostacolo)
xl = infoObject.current_h
yl = 0
xs = 25
spazio = random.randrange(30, 150)
ys = 500
xl_velocita = 4.4
