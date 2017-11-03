#!/usr/bin/python
# coding=utf-8

#-----------------------------------------------------------------------------------------#
# Il gioco è stato scritto da uno che non ne sa nulla di programmazione, che sarei io :)  #
# Il gioco funziona con python27                                                          #
# Buon divertimento, se vi diverte, lo spero, aaaaa                                       #
#-----------------------------------------------------------------------------------------#

import random
import pygame

# ------------------------------------------------------------------------------------
# colori (rosso, verde, blu, ecc..)
# ------------------------------------------------------------------------------------
nero = (0, 0, 0)
rosso = (255, 0, 0)
bianco = (255, 255, 255)
verde = (0, 225, 0)
blu = (18, 10, 153)
giallo = (255, 216, 0)
# ------------------------------------------------------------------------------------
# si inizializza il gioco
# ------------------------------------------------------------------------------------
pygame.init()
infoObject = pygame.display.Info()
schermo = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
# ------------------------------------------------------------------------------------
# musica gioco
# ------------------------------------------------------------------------------------
m_gioco = pygame.mixer.Sound('inizio.wav')
# ------------------------------------------------------------------------------------
# aggiunta suono cattura nemico
# ------------------------------------------------------------------------------------
cattura = pygame.mixer.Sound('cattura1.wav')
# ------------------------------------------------------------------------------------
# avviso
# ------------------------------------------------------------------------------------
avviso = pygame.mixer.Sound('allarme.wav')
# ------------------------------------------------------------------------------------
# suono collisione muro
# ------------------------------------------------------------------------------------
preso = pygame.mixer.Sound('preso3.wav')
# ------------------------------------------------------------------------------------
# uscita gioco
# ------------------------------------------------------------------------------------
schianto = pygame.mixer.Sound('uscita1.wav')
# ------------------------------------------------------------------------------------
# suono collisione cratere
# ------------------------------------------------------------------------------------
lapide = pygame.mixer.Sound('morte6.wav')
# ------------------------------------------------------------------------------------
# aggiungo lo sfondo
# ------------------------------------------------------------------------------------
sfondo = pygame.image.load('sfondo4.jpg')
# ------------------------------------------------------------------------------------
# sfondo intro gioco
# ------------------------------------------------------------------------------------
sfondo1 = pygame.image.load('intro.jpg')
# ------------------------------------------------------------------------------------
# sfondo seleziona
# ------------------------------------------------------------------------------------
sfondo2 = pygame.image.load('seleziona.jpg')
# ------------------------------------------------------------------------------------
# qui si inserisce il titolo nello schermo gioco
# ------------------------------------------------------------------------------------
pygame.display.set_caption('CIOA, HO FAME, FAMMI MANGIARE ......MA STAI ATTENTO...........')
# ------------------------------------------------------------------------------------
# immagine tranello
# ------------------------------------------------------------------------------------
immagine25 = pygame.image.load('attenzione.png')
# ------------------------------------------------------------------------------------
# immagine giocatore
# ------------------------------------------------------------------------------------
immagine = pygame.image.load('giocatore.png')
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
immagine17 = pygame.image.load('prendimi19.png')
immagine18 = pygame.image.load('prendimi20.png')
immagine19 = pygame.image.load('prendimi21.png')
immagine20 = pygame.image.load('prendimi22.png')
immagine21 = pygame.image.load('prendimi23.png')
immagine22 = pygame.image.load('prendimi24.png')
immagine23 = pygame.image.load('prendimi25.png')
immagine24 = pygame.image.load('prendimi26.png')
# ------------------------------------------------------------------------------------
# immagine tranello 1
# ------------------------------------------------------------------------------------
cratere1 = pygame.image.load('morte2.png')
# ------------------------------------------------------------------------------------
# immagine tranello 2
# ------------------------------------------------------------------------------------
cratere2 = pygame.image.load('morte2.png')
# ------------------------------------------------------------------------------------
# immagine tranello 3
# ------------------------------------------------------------------------------------
cratere3 = pygame.image.load('morte2.png')
# ------------------------------------------------------------------------------------
# palla
# ------------------------------------------------------------------------------------
simpatica = pygame.image.load('simpatica.png')
simpatica1 = pygame.image.load('teschio2.png')
simpatica2 = pygame.image.load('teschio2.png')
simpatica3 = pygame.image.load('simpatica3.png')
simpatica5 = pygame.image.load('simpatica2.png')
# ------------------------------------------------------------------------------------
# palla che ti corre dietro
# ------------------------------------------------------------------------------------
nerone = pygame.image.load('teschio2.png')
nerone1 = pygame.image.load('nero1.png')
# ------------------------------------------------------------------------------------
# serve per ottimizzare il gioco
# ------------------------------------------------------------------------------------
clock = pygame.time.Clock()
# ------------------------------------------------------------------------------------
# velocita gioco
# ------------------------------------------------------------------------------------
velocita = 60
direzione = 'right'
piccoloFont = pygame.font.SysFont('comicsansms', 30)
medioFont = pygame.font.SysFont('comicsansms', 50)
grandeFont = pygame.font.SysFont('comicsansms', 80)
oggetto = 11
oggetto_n = 35
gran_c = 23
palla = 25
# ------------------------------------------------------------------------------------
# muro orrizzontale 0
# ------------------------------------------------------------------------------------
def ostacolo_o(x11, y11, x12, y12):
    pygame.draw.rect(schermo, blu, [x11, y11, x12, y12])
x11 = infoObject.current_h
y11 = random.randint(0, infoObject.current_w)
x12 = 50
y12 = 50
xl_velocita11 = 4
# ------------------------------------------------------------------------------------
# muro orrizzontale 1
# ------------------------------------------------------------------------------------
def ostacolo_a(x14, y14, x13, y13):
    pygame.draw.rect(schermo, rosso, [x14, y14, x13, y13])
x14 = infoObject.current_h
y14 = random.randint(0, infoObject.current_w)
x13 = 50
y13 = 50
xl_velocita12 = 4
# ------------------------------------------------------------------------------------
# contorno  destro
# ------------------------------------------------------------------------------------
def ostacolo0(xl0, yl0, xs0, ys0):
    pygame.draw.rect(schermo, rosso, [xl0, yl0, xs0, ys0])
xl0 = infoObject.current_w-100
yl0 = 0
xs0 = 30
ys0 = infoObject.current_h
# ------------------------------------------------------------------------------------
# contorno sinistro
# ------------------------------------------------------------------------------------
def ostacolo1(xl1, yl1, xs1, ys1):
    pygame.draw.rect(schermo, rosso, [xl1, yl1, xs1, ys1])
xl1 = infoObject.current_w > infoObject.current_w
yl1 = 0
xs1 = 30
ys1 = infoObject.current_h
# ------------------------------------------------------------------------------------
# contorno superiore
# ------------------------------------------------------------------------------------
def ostacolo2(xl2, yl2, xs2, ys2):
    pygame.draw.rect(schermo, rosso, [xl2, yl2, xs2, ys2])
xl2 = 0
yl2 = 0
xs2 = infoObject.current_w
ys2 = infoObject.current_h - infoObject.current_h+30
# ------------------------------------------------------------------------------------
# contorno inferiore
# ------------------------------------------------------------------------------------
def ostacolo3(xl3, yl3, xs3, ys3):
    pygame.draw.rect(schermo, rosso, [xl3, yl3, xs3, ys3])
xl3 = 0
yl3 = infoObject.current_h-90
xs3 = infoObject.current_w
ys3 = infoObject.current_h
# ------------------------------------------------------------------------------------
# schermata d'inizio
# ------------------------------------------------------------------------------------
def inizioGioco():
    ini = True
    while ini:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    m_gioco.play(-1)
                    ini = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        schermo.blit(sfondo1, [0, 0])
        messagioSchermo('VERMICELLO', verde, - 100, 'grande')
        messagioSchermo('Ciao....dopo 2 smile....si attivano i tranelli...', nero, - 30, 'medio')
        messagioSchermo('..dopo 20 smile puoi passare da parte a parte dello schermo...... ', nero, 10, 'medio')
        messagioSchermo('...pero aumentano anche gli imprevisti....!!!', nero, 50, 'medio')
        messagioSchermo('Premi I per giocare, premi Q per uscire', nero, 180, 'medio')
        messagioSchermo('Premi spazio per mettere in pausa', nero, 210)
        messagioSchermo('Premi spazio per uscire dalla pausa', nero, 230)
        pygame.display.update()
        clock.tick(velocita)
# ------------------------------------------------------------------------------------
# palla
# ------------------------------------------------------------------------------------
def rompi():
    schermo.blit(simpatica, [x, y])
    schermo.blit(simpatica1, [x1, y1])
    schermo.blit(simpatica2, [y2, x2])
    schermo.blit(simpatica3, [y3, x3])
    schermo.blit(simpatica5, [x7, y7])
    schermo.blit(nerone, [x5, y5])
    schermo.blit(nerone1, [x6, y6])
# ------------------------------------------------------------------------------------
# palla
# ------------------------------------------------------------------------------------
x = infoObject.current_w
y = 0
vx = palla
vy = palla
# ------------------------------------------------------------------------------------
# palla 1
# ------------------------------------------------------------------------------------
x1 = 0
y1 = infoObject.current_w/2
vx1 = palla
vy1 = palla
# ------------------------------------------------------------------------------------
# palla 2
# ------------------------------------------------------------------------------------
x2 = infoObject.current_h
y2 = 0
vx2 = palla
vy2 = palla
# ------------------------------------------------------------------------------------
# palla 3
# ------------------------------------------------------------------------------------
x3 = infoObject.current_w
y3 = 0
vx3 = palla
vy3 = palla
# ------------------------------------------------------------------------------------
# palla 4
# ------------------------------------------------------------------------------------
x4 = 0
y4 = infoObject.current_w
vx4 = palla
vy4 = palla
# ------------------------------------------------------------------------------------
# palla 7
# ------------------------------------------------------------------------------------
x7 = 0
y7 = infoObject.current_h
vx7 = palla
vy7 = palla
# ------------------------------------------------------------------------------------
# palla che ti corre dietro
# ------------------------------------------------------------------------------------
x5 = infoObject.current_w
y5 = 0
x_posizione = 'right'
palla1 = 25
# ------------------------------------------------------------------------------------
# palla che ti corre dietro
# ------------------------------------------------------------------------------------
x6 = 50
y6 = infoObject.current_h
x_posizione1 = 'right'
palla2 = 25
# ------------------------------------------------------------------------------------
# muro
# ------------------------------------------------------------------------------------
def ostacolo(xl, yl, xs, ys):
    pygame.draw.rect(schermo, rosso, [xl, yl, xs, ys])
    pygame.draw.rect(schermo, rosso, [xl, int(ys + spazio), xs, ys + infoObject.current_h])
# ------------------------------------------------------------------------------------
# salvataggio punteggio
# ------------------------------------------------------------------------------------
def Punteggio(listainizio):
    global record, vita
    testo = grandeFont.render('Punteggio: %d' % (listainizio - 1), True, giallo)
    schermo.blit(testo, [infoObject.current_w / 2 - 150, 0])
    record_file = open("FileGioco.txt", "r")
    record = int(record_file.read())
    record_file.close()
    testo1 = medioFont.render('Record: %d' % record, True, blu)
    schermo.blit(testo1, [infoObject.current_w / 2 - 150, 55])
    testo2 = medioFont.render('Vita: %s' % vita, True, verde)
    if vita <= 2:
        testo2 = medioFont.render('Vita: %s' % vita, True, giallo)
    if vita <= 1:
        testo2 = medioFont.render('Vita: %s' % vita, True, rosso)
    schermo.blit(testo2, [infoObject.current_w / 1.3 - 150, 50])
    if listainizio-1 > record:
        record_file = open("FileGioco.txt", "w")
        record_file.write('\n' + str(listainizio - 1))
        record_file.close()
# ------------------------------------------------------------------------------------
# pausa
# ------------------------------------------------------------------------------------
def pausa():
    testo = piccoloFont.render('Premi spazio per pausa, ripremi per continuare', True, rosso)
    schermo.blit(testo, [40, 40])
# ------------------------------------------------------------------------------------
# parametri muro (ostacolo)
# ------------------------------------------------------------------------------------
xl = infoObject.current_h
yl = 0
xs = 25
spazio = random.randrange(30, 150)
ys = 500
xl_velocita = 4.4
def giocatore(lista):
    global trasforma
    if direzione == 'right':
        trasforma = pygame.transform.rotate(immagine, 270)
    if direzione == 'left':
        trasforma = pygame.transform.rotate(immagine, 90)
    if direzione == 'up':
        trasforma = immagine
    if direzione == 'down':
        trasforma = pygame.transform.rotate(immagine, 180)
    schermo.blit(trasforma, (lista[-1][0], lista[-1][1]))
    for XnY in lista[:-1]:
        schermo.blit(immagine3, [XnY[0], XnY[1], oggetto_n, oggetto_n])
def textObbiettivo(text, color, size):
    global textSurface
    if size == 'piccolo':
        textSurface = piccoloFont.render(text, True, color)
    elif size == 'medio':
        textSurface = medioFont.render(text, True, color)
    if size == 'grande':
        textSurface = grandeFont.render(text, True, color)
    return textSurface, textSurface.get_rect()
def messagioSchermo(msg, color, margine_y=0, size='piccolo'):
    textSurface, textRectangle = textObbiettivo(msg, color, size)
    textRectangle.center = (infoObject.current_w / 2), (infoObject.current_h / 2) + margine_y
    schermo.blit(textSurface, textRectangle)
def inizio():
    global pausa, x, y, vx, vy, x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3, x4, y4, vx4, vy4, x5, y5, \
        x_posizione, x_posizione1, x6, y6, x7, y7, vx7, vy7, testa, xl0, yl0, xs0, ys0, xl1, yl1, xs1, ys1, \
        xl2, yl2, xs2, ys2, xl3, yl3, xs3, ys3, record, vita
    global direzione, xl, ys, xl11, yl11, xs11, ys11, x14, y14, x13, y13, x11, y11, x12, y12
    gioco = False
    gameOver = False
    main_x = infoObject.current_w / 2
    main_y = infoObject.current_h / 2
    # ------------------------------------------------------------------------------------
    # nemici
    # ------------------------------------------------------------------------------------
    nemicox = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox2 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy2 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox3 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy3 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox4 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy4 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox5 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy5 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox7 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy7 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox8 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy8 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox6 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy6 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox9 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy9 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox10 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy10 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox11 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy11 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox12 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy12 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox13 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy13 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox14 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy14 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox15 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy15 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox16 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy16 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox17 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy17 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox18 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy18 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox19 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy19 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox20 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy20 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox21 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy21 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox22 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy22 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox23 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy23 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox24 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy24 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    nemicox25 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy25 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
    # ------------------------------------------------------------------------------------
    # crateri
    # ------------------------------------------------------------------------------------
    craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
    craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
    craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
    craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
    craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
    craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
    # ------------------------------------------------------------------------------------
    # direzione, inizio gioco movimento destra sinistra
    # ------------------------------------------------------------------------------------
    main_x_change = 0
    main_y_change = 0
    lista = []
    listainizio = 1
    vita = 3
    # ------------------------------------------------------------------------------------
    # il ciclo while cattura gli eventi tramite event
    # ------------------------------------------------------------------------------------
    while not gioco:
        while gameOver:
            schermo.blit(sfondo2, [0, 0])
            messagioSchermo('NOOO.....!!!!!', rosso, - 80, 'grande')
            messagioSchermo('Per continuare clicca la lettera C', verde, 30, 'medio')
            messagioSchermo('Per uscire clicca la lettera U', verde, 80, 'medio')
            messagioSchermo('Hai recuperato: ' + str(listainizio - 1) + '  Smile', giallo, -20, 'medio')
            messagioSchermo('Record: %d ' % record, verde, -160, 'grande')
            messagioSchermo('Vite: %d' % vita, giallo, 140, 'grande')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        gioco = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        schianto.stop()
                        m_gioco.play()
                        inizio()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gioco = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direzione = 'left'
                    main_x_change = -oggetto
                    main_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direzione = 'right'
                    main_x_change = oggetto
                    main_y_change = 0
                elif event.key == pygame.K_UP:
                    direzione = 'up'
                    main_y_change = -oggetto
                    main_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direzione = 'down'
                    main_y_change = oggetto
                    main_x_change = 0
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                while 1:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                        break
        # ------------------------------------------------------------------------------------
        # parametri schermo
        # ------------------------------------------------------------------------------------
        if len(lista) <= 19:
            if main_x >= infoObject.current_w-120 or main_x < 30 or main_y < 30 or main_y >= infoObject.current_h-110:
                m_gioco.stop()
                lapide.play()
                gameOver = True
        if len(lista) >= 19:
            if main_x >= infoObject.current_w:
                main_x = +0
            elif main_x <= 0:
                main_x = +infoObject.current_w
            if main_y >= infoObject.current_h:
                main_y = +0
            elif main_y <= 0:
                main_y = +infoObject.current_h
        # ------------------------------------------------------------------------------------
        # schermo
        # ------------------------------------------------------------------------------------
        main_x += main_x_change
        main_y += main_y_change
        schermo.blit(sfondo, [0, 0])
        # ------------------------------------------------------------------------------------
        # nemico
        # ------------------------------------------------------------------------------------
        schermo.blit(immagine1, [nemicox, nemicoy, oggetto_n, oggetto_n])
        schermo.blit(immagine2, [nemicox2, nemicoy2, oggetto_n, oggetto_n])
        schermo.blit(immagine3, [nemicox3, nemicoy3, oggetto_n, oggetto_n])
        schermo.blit(immagine4, [nemicox4, nemicoy4, oggetto_n, oggetto_n])
        schermo.blit(immagine5, [nemicox5, nemicoy5, oggetto_n, oggetto_n])
        schermo.blit(immagine6, [nemicox6, nemicoy6, oggetto_n, oggetto_n])
        schermo.blit(immagine7, [nemicox9, nemicoy9, oggetto_n, oggetto_n])
        schermo.blit(immagine8, [nemicox10, nemicoy10, oggetto_n, oggetto_n])
        schermo.blit(immagine9, [nemicox7, nemicoy7, oggetto_n, oggetto_n])
        schermo.blit(immagine10, [nemicox8, nemicoy8, oggetto_n, oggetto_n])
        schermo.blit(immagine11, [nemicox11, nemicoy11, oggetto_n, oggetto_n])
        schermo.blit(immagine12, [nemicox12, nemicoy12, oggetto_n, oggetto_n])
        schermo.blit(immagine13, [nemicox13, nemicoy13, oggetto_n, oggetto_n])
        schermo.blit(immagine14, [nemicox14, nemicoy14, oggetto_n, oggetto_n])
        schermo.blit(immagine15, [nemicox15, nemicoy15, oggetto_n, oggetto_n])
        schermo.blit(immagine16, [nemicox16, nemicoy16, oggetto_n, oggetto_n])
        schermo.blit(immagine17, [nemicox17, nemicoy17, oggetto_n, oggetto_n])
        schermo.blit(immagine18, [nemicox18, nemicoy18, oggetto_n, oggetto_n])
        schermo.blit(immagine19, [nemicox19, nemicoy19, oggetto_n, oggetto_n])
        schermo.blit(immagine20, [nemicox20, nemicoy20, oggetto_n, oggetto_n])
        schermo.blit(immagine21, [nemicox21, nemicoy21, oggetto_n, oggetto_n])
        schermo.blit(immagine22, [nemicox22, nemicoy22, oggetto_n, oggetto_n])
        schermo.blit(immagine23, [nemicox23, nemicoy23, oggetto_n, oggetto_n])
        schermo.blit(immagine24, [nemicox24, nemicoy24, oggetto_n, oggetto_n])
        schermo.blit(immagine25, [nemicox25, nemicoy25, oggetto_n, oggetto_n])
        # ------------------------------------------------------------------------------------
        # nemico strano 7
        # ------------------------------------------------------------------------------------
        schermo.blit(immagine9, [nemicox7, nemicoy7, oggetto_n, oggetto_n])
        # ------------------------------------------------------------------------------------
        # nemico strano 8
        # ------------------------------------------------------------------------------------
        if len(lista) >= 2:
            schermo.blit(immagine10, [nemicox8, nemicoy8, oggetto_n, oggetto_n])
        # ------------------------------------------------------------------------------------
        # cratere 1
        # ------------------------------------------------------------------------------------
        schermo.blit(cratere1, [craterex1, craterey1, gran_c, gran_c])
        # ------------------------------------------------------------------------------------
        # collisione cratere 1
        # ------------------------------------------------------------------------------------
        if len(lista) >= 2:
            if (main_x >= craterex1) and (main_x <= craterex1 + gran_c) or (main_x + oggetto >= craterex1) \
                    and (main_x + oggetto <= craterex1 + gran_c):
                if (main_y >= craterey1) and (main_y <= craterey1 + gran_c) or (main_y + oggetto >= craterey1) \
                        and (main_y + oggetto <= craterey1 + gran_c):
                    if (main_x + oggetto >= craterex1) and (main_x + oggetto <= craterex1 + gran_c):
                        if (main_y + oggetto >= craterey1) and (main_y + oggetto <= craterey1 + gran_c):
                            lapide.play()
                            listainizio -= 1
                            lista.remove(testa)
                            if vita <= 0:
                                m_gioco.stop()
                                gameOver = True
                            elif listainizio - 1 <= 0:
                                avviso.play()
                                vita -= 1
        # ------------------------------------------------------------------------------------
        # cratere 2
        # ------------------------------------------------------------------------------------
        schermo.blit(cratere2, [craterex2, craterey2, gran_c, gran_c])
        #-------------------------------------------------------------------------------------
        # collisione cratere 2
        #-------------------------------------------------------------------------------------
        if len(lista) >= 2:
            if (main_x >= craterex2) and (main_x <= craterex2 + gran_c) or (main_x + oggetto >= craterex2) \
                    and (main_x + oggetto <= craterex2 + gran_c):
                if (main_y >= craterey2) and (main_y <= craterey2 + gran_c) or (main_y + oggetto >= craterey2) \
                        and (main_y + oggetto <= craterey2 + gran_c):
                    if (main_x + oggetto >= craterex2) and (main_x + oggetto <= craterex2 + gran_c):
                        if (main_y + oggetto >= craterey2) and (main_y + oggetto <= craterey2 + gran_c):
                            lapide.play()
                            listainizio -= 1
                            lista.remove(testa)
                            if vita <= 0:
                                m_gioco.stop()
                                gameOver = True
                            elif listainizio - 1 <= 0:
                                avviso.play()
                                vita -= 1
        # ------------------------------------------------------------------------------------
        # cratere 3
        # ------------------------------------------------------------------------------------
        schermo.blit(cratere3, [craterex3, craterey3, gran_c, gran_c])
        # ------------------------------------------------------------------------------------
        # collisione cratere 3
        # ------------------------------------------------------------------------------------
        if len(lista) >= 2:
            if (main_x >= craterex3) and (main_x <= craterex3 + gran_c) or (main_x + oggetto >= craterex3) \
                    and (main_x + oggetto <= craterex3 + gran_c):
                if (main_y >= craterey3) and (main_y <= craterey3 + gran_c) or (main_y + oggetto >= craterey3) \
                        and (main_y + oggetto <= craterey3 + gran_c):
                    if (main_x + oggetto >= craterex3) and (main_x + oggetto <= craterex3 + gran_c):
                        if (main_y + oggetto >= craterey3) and (main_y + oggetto <= craterey3 + gran_c):
                            lapide.play()
                            listainizio -= 1
                            lista.remove(testa)
                            if vita <= 0:
                                m_gioco.stop()
                                gameOver = True
                            elif listainizio - 1 <= 0:
                                avviso.play()
                                vita -= 1
        # ------------------------------------------------------------------------------------
        # giocatore
        # ------------------------------------------------------------------------------------
        testa = []
        testa.append(main_x)
        testa.append(main_y)
        lista.append(testa)
        if len(lista) > listainizio:
            del lista[0]
        # ------------------------------------------------------------------------------------
        # il vermicello non puo toccarsi
        # ------------------------------------------------------------------------------------
        # for iniziolista in lista[:-2]:
        #     if iniziolista == testa:
        #         lapide.play()
        #         gameOver = True
        giocatore(lista)
        rompi()
        if len(lista) <= 20:
            ostacolo0(xl0, yl0, xs0, ys0)
            ostacolo1(xl1, yl1, xs1, ys1)
            ostacolo2(xl2, yl2, xs2, ys2)
            ostacolo3(xl3, yl3, xs3, ys3)
        ostacolo(xl, yl, xs, ys)
        xl -= xl_velocita
        ostacolo_o(x11, y11, x12, y12)
        y11 -= xl_velocita11
        ostacolo_a(x14, y14, x13, y13)
        y14 -= xl_velocita12
        Punteggio(listainizio)
        pausa()
        # ------------------------------------------------------------------------------------
        # movimento palla
        # ------------------------------------------------------------------------------------
        x += vx
        y += vy
        if x >= infoObject.current_w - 70:
            vx = -2
            if len(lista) >= 10:
                vx = -4
                if len(lista) >= 14:
                    vx = -6
                    if len(lista) >= 16:
                        vx = -8
                        if len(lista) >= 18:
                            vx = -10
                            if len(lista) >= 21:
                                vx = -12
        if x < 5:
            vx = 3
            if len(lista) >= 13:
                vx = 4
                if len(lista) >= 15:
                    vx = 6
                    if len(lista) >= 17:
                        vx = 8
                        if len(lista) >= 19:
                            vx = 10
                            if len(lista) >= 20:
                                vx = 12
        if y > infoObject.current_h:
            vy = -4
            if len(lista) >= 15:
                vy = -8
                if len(lista) >= 16:
                    vy = -10
                    if len(lista) >= 6:
                        vy = -12
                        if len(lista) >= 18:
                            vy = -14
                            if len(lista) >= 26:
                                vy = -16
        if y < 3:
            vy = 2
            if len(lista) >= 12:
                vy = 4
                if len(lista) >= 15:
                    vy = 6
                    if len(lista) >= 27:
                        vy = 8
                        if len(lista) >= 30:
                            vy = 10
                            if len(lista) >= 36:
                                vy = 12
        # ------------------------------------------------------------------------------------
        # collisione palla
        # ------------------------------------------------------------------------------------
        if len(lista) >= 2:
            if (main_x >= x) and (main_x <= x + palla) or (main_x + oggetto >= x) and (main_x + oggetto <= x + palla):
                if (main_y >= y) and (main_y <= y + palla) or (main_y + oggetto >= y) and (
                        main_y + oggetto <= y + palla):
                    if (main_x + oggetto >= x) and (main_x + oggetto <= x + palla):
                        if (main_y + oggetto >= y) and (main_y + oggetto <= y + palla):
                            lapide.play()
                            listainizio -= 1
                            lista.remove(testa)
                            if vita <= 0:
                                m_gioco.stop()
                                gameOver = True
                            elif listainizio - 1 <= 0:
                                avviso.play()
                                vita -= 1
        # ------------------------------------------------------------------------------------
        # movimento palla 7
        # ------------------------------------------------------------------------------------
        if len(lista) >= 25:
            x7 += vx7
            y7 += vy7
            if x7 > infoObject.current_w - 70:
                vx7 = -10
                if len(lista) >= 30:
                    vx7 = -10
            if x7 <= 5:
                vx7 = 3
                if len(lista) >= 28:
                    vx7 = 9
            if y7 > infoObject.current_h:
                vy7 = -14
                if len(lista) >= 34:
                    vy7 = -16
            if y7 < 3:
                vy7 = 2
                if len(lista) >= 36:
                    vy = 5
            # ------------------------------------------------------------------------------------
            # collisione palla 7
            # ------------------------------------------------------------------------------------
            if len(lista) >= 2:
                if (main_x >= x7) and (main_x <= x7 + palla) or (main_x + oggetto >= x7) and (
                                main_x + oggetto <= x7 + palla):
                    if (main_y >= y7) and (main_y <= y7 + palla) or (main_y + oggetto >= y7) and (
                                    main_y + oggetto <= y7 + palla):
                        if (main_x + oggetto >= x7) and (main_x + oggetto <= x7 + palla):
                            if (main_y + oggetto >= y7) and (main_y + oggetto <= y7 + palla):
                                lapide.play()
                                listainizio -= 1
                                lista.remove(testa)
                                if vita <= 0:
                                    m_gioco.stop()
                                    gameOver = True
                                elif listainizio - 1 <= 0:
                                    avviso.play()
                                    vita -= 1
        # ------------------------------------------------------------------------------------
        # movimento palla 1
        # ------------------------------------------------------------------------------------
        if len(lista) >= 50:
            x1 += vx1
            y1 += vy1
            if x1 >= infoObject.current_w - 70:
                vx1 = -4
                if len(lista) >= 52:
                    vx1 = -5
                    if len(lista) >= 54:
                        vx1 = -7
                        if len(lista) >= 56:
                            vx1 = -9
                            if len(lista) >= 58:
                                vx1 = -13
                                if len(lista) >= 60:
                                    vx1 = -15
                                    if len(lista) >= 62:
                                        vx1 = -19
            if x1 <= 10:
                vx1 = 1
                if len(lista) >= 53:
                    vx1 = 8
            if y1 > infoObject.current_h:
                vy1 = -2
                if len(lista) >= 57:
                    vy1 = -12
            if y1 <= 4:
                vy1 = 2
                if len(lista) >= 59:
                    vy1 = 6
            # ------------------------------------------------------------------------------------
            # collisione palla 1
            # ------------------------------------------------------------------------------------
            if len(lista) >= 51:
                if (main_x >= x1) and (main_x <= x1 + palla) or (main_x + oggetto >= x1) and (
                                main_x + oggetto <= x1 + palla):
                    if (main_y >= y1) and (main_y <= y1 + palla) or (main_y + oggetto >= y1) and (
                                    main_y + oggetto <= y1 + palla):
                        if (main_x + oggetto >= x1) and (main_x + oggetto <= x1 + palla):
                            if (main_y + oggetto >= y1) and (main_y + oggetto <= y1 + palla):
                                lapide.play()
                                if vita <= 0:
                                    m_gioco.stop()
                                    gameOver = True
                                elif listainizio - 1 <= 0:
                                    avviso.play()
                                    vita -= 1
        # ------------------------------------------------------------------------------------
        # movimento palla 2
        # ------------------------------------------------------------------------------------
        if len(lista) >= 40:
            x2 += vx2
            y2 += vy2
            if x2 >= infoObject.current_w - 70:
                vx2 = -4
                if len(lista) >= 42:
                    vx2 = -10
                    if len(lista) >= 44:
                        vx2 = -6
                        if len(lista) >= 46:
                            vx2 = -8
                            if len(lista) >= 48:
                                vx2 = -10
                                if len(lista) >= 60:
                                    vx2 = -18
            if x2 <= 11:
                vx2 = 1
                if len(lista) >= 41:
                    vx2 = 3
                    if len(lista) >= 43:
                        vx2 = 6
                        if len(lista) >= 45:
                            vx2 = 8
                            if len(lista) >= 47:
                                vx2 = 10
                                if len(lista) >= 69:
                                    vx2 = 12
            if y2 > infoObject.current_h:
                vy2 = -3
                if len(lista) >= 50:
                    vy2 = -9
            if y2 <= 5:
                vy2 = 5
                if len(lista) >= 52:
                    vy2 = 3
            # ------------------------------------------------------------------------------------
            # collisione palla 2
            # ------------------------------------------------------------------------------------
            if len(lista) >= 2:
                if (main_x >= y2) and (main_x <= y2 + palla) or (main_x + oggetto >= y2) and (
                                main_x + oggetto <= y2 + palla):
                    if (main_y >= x2) and (main_y <= x2 + palla) or (main_y + oggetto >= x2) and (
                                        main_y + oggetto <= x2 + palla):
                        if (main_x + oggetto >= y2) and (main_x + oggetto <= y2 + palla):
                            if (main_y + oggetto >= x2) and (main_y + oggetto <= x2 + palla):
                                lapide.play()
                                if vita <= 0:
                                    m_gioco.stop()
                                    gameOver = True
                                elif listainizio - 1 <= 0:
                                    avviso.play()
                                    vita -= 1
        # ------------------------------------------------------------------------------------
        # movimento palla 3
        # ------------------------------------------------------------------------------------
        if len(lista) >= 3:
            x3 += vx3
            y3 += vy3
            if x3 >= infoObject.current_w - 90:
                vx3 = -4
                if len(lista) >= 4:
                    vx3 = -12
                    if len(lista) >= 5:
                        vx3 = -6
                        if len(lista) >= 6:
                            vx3 = -8
                            if len(lista) >= 8:
                                vx3 = -10
                                if len(lista) >= 16:
                                    vx3 = -12
            if x3 <= 6:
                vx3 = 1
                if len(lista) >= 5:
                    vx3 = 14
            if y3 >= infoObject.current_h:
                vy3 = -1
                if len(lista) >= 5:
                    vy3 = -10
            if y3 <= 12:
                vy3 = 5
                if len(lista) >= 5:
                    vy3 = 12
            # ------------------------------------------------------------------------------------
            # collisione palla 3
            # ------------------------------------------------------------------------------------
            if len(lista) >= 2:
                if (main_x >= y3) and (main_x <= y3 + palla) or (main_x + oggetto >= y3) and (
                                main_x + oggetto <= y3 + palla):
                    if (main_y >= x3) and (main_y <= x3 + palla) or (main_y + oggetto >= x3) and (
                                        main_y + oggetto <= x3 + palla):
                        if (main_x + oggetto >= y3) and (main_x + oggetto <= y3 + palla):
                            if (main_y + oggetto >= x3) and (main_y + oggetto <= x3 + palla):
                                lapide.play()
                                listainizio -= 1
                                lista.remove(testa)
                                if listainizio == 0:
                                    lapide.play()
                                    if vita <= 0:
                                        m_gioco.stop()
                                        gameOver = True
                                    elif listainizio - 1 <= 0:
                                        avviso.play()
                                        vita -= 1
        # ------------------------------------------------------------------------------------
        # movimento palla 4
        # ------------------------------------------------------------------------------------
        if len(lista) >= 4:
            x4 += vx4
            y4 += vy4
            if x4 > infoObject.current_w - 70:
                vx4 = -1
                if len(lista) >= 6:
                    vx4 = -13
                    if len(lista) >= 8:
                        vx4 = -12
                        if len(lista) >= 10:
                            vx4 = -6
                            if len(lista) >= 12:
                                vx4 = -8
                                if len(lista) >= 14:
                                    vx4 = -14
                                    if len(lista) >= 16:
                                        vx4 = -20
            if x4 <= 14:
                vx4 = 4
            if y4 > infoObject.current_h:
                vy4 = -4
                if len(lista) >= 6:
                    vy4 = -11
            if y4 <= 3:
                vy4 = 1
                if len(lista) >= 7:
                    vy4 = 6
            # ------------------------------------------------------------------------------------
            # collisione palla 4
            # ------------------------------------------------------------------------------------
            if len(lista) >= 2:
                if (main_x >= y4) and (main_x <= y4 + palla) or (main_x + oggetto >= y4) and (
                                    main_x + oggetto <= y4 + palla):
                    if (main_y >= x4) and (main_y <= x4 + palla) or (main_y + oggetto >= x4) and (
                                    main_y + oggetto <= x4 + palla):
                        if (main_x + oggetto >= y4) and (main_x + oggetto <= y4 + palla):
                            if (main_y + oggetto >= x4) and (main_y + oggetto <= x4 + palla):
                                lapide.play()
                                listainizio -= 1
                                lista.remove(testa)
                                if vita <= 0:
                                    m_gioco.stop()
                                    gameOver = True
                                elif listainizio - 1 <= 0:
                                    avviso.play()
                                    vita -= 1
        # ------------------------------------------------------------------------------------
        # movimento palla che ti corre dietro con variabili di velocita
        # ------------------------------------------------------------------------------------
        if len(lista) >= 1:
            if main_x <= x6:
                x6 -= 1.8
                x_posizione1 = 'left'
                if len(lista) >= 16:
                    x6 -= 1.9
                    if len(lista) >= 40:
                        x6 -= 2
                        if len(lista) >= 70:
                            x6 -= 2.1
            elif main_x >= x6:
                x6 += 1.8
                x_posizione1 = 'right'
                if len(lista) >= 16:
                    x6 += 1.9
                    if len(lista) >= 40:
                        x6 += 2
                        if len(lista) >= 70:
                            x6 += 2.1
            if main_y <= y6:
                y6 -= 1.8
                x_posizione1 = 'up'
                if len(lista) >= 16:
                    y6 -= 1.9
                    if len(lista) >= 40:
                        y6 -= 2
                        if len(lista) >= 70:
                            y6 -= 2.1
            elif main_y >= y6:
                y6 += 1.8
                x_posizione1 = 'down'
                if len(lista) >= 16:
                    y6 += 1.9
                    if len(lista) >= 40:
                        y6 += 2
                        if len(lista) >= 70:
                            y6 += 2.1
            # ------------------------------------------------------------------------------------
            # parametri collisione palla che ti corre dietro
            # ------------------------------------------------------------------------------------
            if len(lista) >= 2:
                if (main_x >= x6) and (main_x <= x6 + palla2) or (main_x + oggetto >= x6) and (
                                main_x + oggetto <= x6 + palla2):
                    if (main_y >= y6) and (main_y <= y6 + palla2) or (main_y + oggetto >= y6) and (
                                    main_y + oggetto <= y6 + palla2):
                        if (main_x + oggetto >= x6) and (main_x + oggetto <= x6 + palla2):
                            if (main_y + oggetto >= y6) and (main_y + oggetto <= y6 + palla2):
                                lapide.play()
                                listainizio -= 1
                                lista.remove(testa)
                                if vita <= 0:
                                    m_gioco.stop()
                                    gameOver = True
                                elif listainizio - 1 <= 0:
                                    avviso.play()
                                    vita -= 1
        # ------------------------------------------------------------------------------------
        # movimento palla che ti corre dietro con variabili di velocita
        # ------------------------------------------------------------------------------------
        if len(lista) >= 2:
            if main_x < x5:
                x5 -= 0.5
                x_posizione = 'left'
                if len(lista) >= 15:
                    x5 -= 0.6
                    if len(lista) >= 30:
                        x5 -= 0.7
                        if len(lista) >= 40:
                            x5 -= 0.8
                            if len(lista) >= 50:
                                x5 -= 0.9
                                if len(lista) >= 85:
                                    x5 -= 1
            elif main_x >= x5:
                x5 += 0.5
                x_posizione = 'right'
                if len(lista) >= 15:
                    x5 += 0.6
                    if len(lista) >= 30:
                        x5 += 0.7
                        if len(lista) >= 40:
                            x5 += 0.8
                            if len(lista) >= 50:
                                x5 += 0.9
                                if len(lista) >= 85:
                                    x5 += 1
            if main_y <= y5:
                y5 -= 0.5
                x_posizione = 'up'
                if len(lista) >= 15:
                    y5 -= 0.6
                    if len(lista) >= 30:
                        y5 -= 0.7
                        if len(lista) >= 40:
                            y5 -= 0.8
                            if len(lista) >= 50:
                                y5 -= 0.9
                                if len(lista) >= 85:
                                    y5 -= 1
            elif main_y >= y5:
                y5 += 0.5
                x_posizione = 'down'
                if len(lista) >= 15:
                    y5 += 0.6
                    if len(lista) >= 30:
                        y5 += 0.7
                        if len(lista) >= 40:
                            y5 += 0.8
                            if len(lista) >= 50:
                                y5 += 0.9
                                if len(lista) >= 85:
                                    y5 += 1
            # ------------------------------------------------------------------------------------
            # parametri collisione palla che ti corre dietro
            # ------------------------------------------------------------------------------------
            if len(lista) >= 2:
                if (main_x >= x5) and (main_x <= x5 + palla1) or (main_x + oggetto >= x5) and (
                                main_x + oggetto <= x5 + palla1):
                    if (main_y >= y5) and (main_y <= y5 + palla1) or (main_y + oggetto >= y5) and (
                                main_y + oggetto <= y5 + palla1):
                        if (main_x + oggetto >= x5) and (main_x + oggetto <= x5 + palla1):
                            if (main_y + oggetto >= y5) and (main_y + oggetto <= y5 + palla1):
                                lapide.play()
                                listainizio -= 1
                                lista.remove(testa)
                                if vita <= 0:
                                    m_gioco.stop()
                                    gameOver = True
                                elif listainizio - 1 <= 0:
                                    avviso.play()
                                    vita -= 1
        # ------------------------------------------------------------------------------------
        # movimento muro (ostacolo)
        # ------------------------------------------------------------------------------------
        if len(lista) >= 22:
            if xl < 0:
                xl = infoObject.current_w
                ys = random.randint(0, infoObject.current_h)
        if len(lista) >= 22:
            if main_x + 15 >= xl and main_y + 15 <= ys and main_x - 15 <= xs + xl:
                preso.play()
                m_gioco.stop()
                gameOver = True
            if main_x + 15 >= xl and main_y + 15 >= ys + spazio and main_x - 15 <= xs + xl:
                preso.play()
                m_gioco.stop()
                gameOver = True
        # ------------------------------------------------------------------------------------
        # muri strani
        # ------------------------------------------------------------------------------------
        if y11 < -x12:
            y11 = infoObject.current_w
            x11 = random.randint(0, infoObject.current_w)
            x12 = random.randint(0, infoObject.current_h)
        if y14 < -y13:
            y14 = infoObject.current_h
            x14 = random.randint(0, infoObject.current_w)
            y13 = random.randint(0, infoObject.current_h)
        pygame.display.update()
        # ------------------------------------------------------------------------------------
        # collisione nemico 1
        # ------------------------------------------------------------------------------------
        if (main_x >= nemicox) and (main_x <= nemicox + oggetto_n) or (main_x + oggetto >= nemicox) \
                and (main_x + oggetto < nemicox + oggetto_n):
            if (main_y >= nemicoy) and (main_y <= nemicoy + oggetto_n) or (main_y + oggetto >= nemicoy) \
                    and (main_y + oggetto <= nemicoy + oggetto_n):
                if (main_x + oggetto >= nemicox) and (main_x + oggetto <= nemicox + oggetto_n):
                    if (main_y + oggetto >= nemicoy) and (main_y + oggetto <= nemicoy + oggetto_n):
                        cattura.play()
                        nemicox = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        listainizio += 1
                        if listainizio - 1 == 100:
                            avviso.play()
                            vita += 1
                        craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico 2
        # ------------------------------------------------------------------------------------
        if (main_x >= nemicox2) and (main_x <= nemicox2 + oggetto_n) or (main_x + oggetto >= nemicox2) \
                and (main_x + oggetto <= nemicox2 + oggetto_n):
            if (main_y >= nemicoy2) and (main_y <= nemicoy2 + oggetto_n) or (main_y + oggetto >= nemicoy2) \
                        and (main_y + oggetto <= nemicoy2 + oggetto_n):
                if (main_x + oggetto >= nemicox2) and (main_x + oggetto <= nemicox2 + oggetto_n):
                    if (main_y + oggetto >= nemicoy2) and (main_y + oggetto <= nemicoy2 + oggetto_n):
                        cattura.play()
                        nemicox2 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy2 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        listainizio += 1
                        if listainizio - 1 == 100:
                            avviso.play()
                            vita += 1
                        craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico 3
        # ------------------------------------------------------------------------------------
        if (main_x >= nemicox3) and (main_x <= nemicox3 + oggetto_n) or (main_x + oggetto >= nemicox3) \
                and (main_x + oggetto <= nemicox3 + oggetto_n):
            if (main_y >= nemicoy3) and (main_y <= nemicoy3 + oggetto_n) or (main_y + oggetto >= nemicoy3) \
                            and (main_y + oggetto <= nemicoy3 + oggetto_n):
                if (main_x + oggetto >= nemicox3) and (main_x + oggetto <= nemicox3 + oggetto_n):
                    if (main_y + oggetto >= nemicoy3) and (main_y + oggetto <= nemicoy3 + oggetto_n):
                        cattura.play()
                        nemicox3 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy3 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        listainizio += 1
                        if listainizio - 1 == 100:
                            avviso.play()
                            vita += 1
                        craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico 4
        # ------------------------------------------------------------------------------------
        if (main_x >= nemicox4) and (main_x <= nemicox4 + oggetto_n) or (main_x + oggetto >= nemicox4) \
                and (main_x + oggetto < nemicox4 + oggetto_n):
            if (main_y >= nemicoy4) and (main_y <= nemicoy4 + oggetto_n) or (main_y + oggetto >= nemicoy4) \
                            and (main_y + oggetto <= nemicoy4 + oggetto_n):
                if (main_x + oggetto >= nemicox4) and (main_x + oggetto <= nemicox4 + oggetto_n):
                    if (main_y + oggetto >= nemicoy4) and (main_y + oggetto <= nemicoy4 + oggetto_n):
                        cattura.play()
                        nemicox4 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy4 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        listainizio += 1
                        if listainizio - 1 == 100:
                            avviso.play()
                            vita += 1
                        craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico 5
        # ------------------------------------------------------------------------------------
        if (main_x >= nemicox5) and (main_x <= nemicox5 + oggetto_n) or (main_x + oggetto >= nemicox5) \
                and (main_x + oggetto < nemicox5 + oggetto_n):
            if (main_y >= nemicoy5) and (main_y <= nemicoy5 + oggetto_n) or (main_y + oggetto >= nemicoy5) \
                        and (main_y + oggetto <= nemicoy5 + oggetto_n):
                if (main_x + oggetto >= nemicox5) and (main_x + oggetto <= nemicox5 + oggetto_n):
                    if (main_y + oggetto >= nemicoy5) and (main_y + oggetto <= nemicoy5 + oggetto_n):
                        cattura.play()
                        nemicox5 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy5 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        listainizio += 1
                        if listainizio - 1 == 100:
                            avviso.play()
                            vita += 1
                        craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico 6
        # ------------------------------------------------------------------------------------
        if (main_x >= nemicox6) and (main_x <= nemicox6 + oggetto_n) or (main_x + oggetto >= nemicox6) \
                and (main_x + oggetto <= nemicox6 + oggetto_n):
            if (main_y >= nemicoy6) and (main_y <= nemicoy6 + oggetto_n) or (main_y + oggetto >= nemicoy6) \
                    and (main_y + oggetto <= nemicoy6 + oggetto_n):
                if (main_x + oggetto >= nemicox6) and (main_x + oggetto <= nemicox6 + oggetto_n):
                    if (main_y + oggetto >= nemicoy6) and (main_y + oggetto <= nemicoy6 + oggetto_n):
                        cattura.play()
                        nemicox6 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy6 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        listainizio += 1
                        if listainizio - 1 == 100:
                            avviso.play()
                            vita += 1
                        craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico strano 7
        # ------------------------------------------------------------------------------------
        if (main_x >= nemicox7) and (main_x <= nemicox7 + oggetto_n) or (main_x + oggetto >= nemicox7) \
                and (main_x + oggetto <= nemicox7 + oggetto_n):
            if (main_y >= nemicoy7) and (main_y <= nemicoy7 + oggetto_n) or (main_y + oggetto >= nemicoy7) \
                    and (main_y + oggetto <= nemicoy7 + oggetto_n):
                if (main_x + oggetto >= nemicox7) and (main_x + oggetto <= nemicox7 + oggetto_n):
                    if (main_y + oggetto >= nemicoy7) and (main_y + oggetto <= nemicoy7 + oggetto_n):
                        cattura.play()
                        nemicox7 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy7 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        listainizio += 1
                        if listainizio - 1 == 100:
                            avviso.play()
                            vita += 1
                        nemicox8 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy8 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico strano 8
        # ------------------------------------------------------------------------------------
        if (main_x >= nemicox8) and (main_x <= nemicox8 + oggetto_n) or (main_x + oggetto >= nemicox8) \
                and (main_x + oggetto <= nemicox8 + oggetto_n):
            if (main_y >= nemicoy8) and (main_y <= nemicoy8 + oggetto_n) or (main_y + oggetto >= nemicoy8) \
                    and (main_y + oggetto <= nemicoy8 + oggetto_n):
                if (main_x + oggetto >= nemicox8) and (main_x + oggetto <= nemicox8 + oggetto_n):
                    if (main_y + oggetto >= nemicoy8) and (main_y + oggetto <= nemicoy8 + oggetto_n):
                        cattura.play()
                        nemicox8 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy8 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        listainizio += 1
                        if listainizio - 1 == 100:
                            avviso.play()
                            vita += 1
                        nemicox3 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy3 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox4 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy4 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox5 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy5 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox6 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy6 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox7 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy7 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico strano 9
        # ------------------------------------------------------------------------------------
        if (main_x >= nemicox9) and (main_x <= nemicox9 + oggetto_n) or (main_x + oggetto >= nemicox9) \
                and (main_x + oggetto < nemicox9 + oggetto_n):
            if (main_y >= nemicoy9) and (main_y <= nemicoy9 + oggetto_n) or (main_y + oggetto >= nemicoy9) \
                    and (main_y + oggetto <= nemicoy9 + oggetto_n):
                if (main_x + oggetto >= nemicox9) and (main_x + oggetto <= nemicox9 + oggetto_n):
                    if (main_y + oggetto >= nemicoy9) and (main_y + oggetto <= nemicoy9 + oggetto_n):
                        cattura.play()
                        nemicox9 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy9 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        listainizio += 1
                        if listainizio - 1 == 100:
                            avviso.play()
                            vita += 1
                        nemicox3 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy3 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox4 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy4 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox5 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy5 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox6 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy6 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox7 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy7 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox8 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy8 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico strano 10
        # ------------------------------------------------------------------------------------
        if (main_x >= nemicox10) and (main_x <= nemicox10 + oggetto_n) or (main_x + oggetto >= nemicox10) \
                and (main_x + oggetto <= nemicox10 + oggetto_n):
            if (main_y >= nemicoy10) and (main_y <= nemicoy10 + oggetto_n) or (main_y + oggetto >= nemicoy10) \
                    and (main_y + oggetto <= nemicoy10 + oggetto_n):
                if (main_x + oggetto >= nemicox10) and (main_x + oggetto <= nemicox10 + oggetto_n):
                    if (main_y + oggetto >= nemicoy10) and (main_y + oggetto <= nemicoy10 + oggetto_n):
                        cattura.play()
                        nemicox10 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy10 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        listainizio += 1
                        if listainizio - 1 == 100:
                            avviso.play()
                            vita += 1
                        nemicox3 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy3 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox4 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy4 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox5 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy5 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox6 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy6 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox7 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy7 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox8 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy8 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        nemicox9 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                        nemicoy9 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                        craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                        craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                        craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico strano 11
        # ------------------------------------------------------------------------------------
        if len(lista) > 0:
            if (main_x >= nemicox11) and (main_x <= nemicox11 + oggetto_n) or (main_x + oggetto >= nemicox11) \
                    and (main_x + oggetto <= nemicox11 + oggetto_n):
                if (main_y >= nemicoy11) and (main_y <= nemicoy11 + oggetto_n) or (main_y + oggetto >= nemicoy11) \
                        and (main_y + oggetto <= nemicoy11 + oggetto_n):
                    if (main_x + oggetto >= nemicox11) and (main_x + oggetto <= nemicox11 + oggetto_n):
                        if (main_y + oggetto >= nemicoy11) and (main_y + oggetto <= nemicoy11 + oggetto_n):
                            cattura.play()
                            nemicox11 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy11 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            listainizio += 1
                            if listainizio - 1 == 100:
                                avviso.play()
                                vita += 1
                            nemicox3 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy3 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox4 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy4 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox5 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy5 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox6 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy6 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox7 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy7 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox8 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy8 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox9 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy9 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox10 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy10 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico strano 12
        # ------------------------------------------------------------------------------------
        if len(lista) > 0:
            if (main_x >= nemicox12) and (main_x <= nemicox12 + oggetto_n) or (main_x + oggetto >= nemicox12) \
                    and (main_x + oggetto <= nemicox12 + oggetto_n):
                if (main_y >= nemicoy12) and (main_y <= nemicoy12 + oggetto_n) or (main_y + oggetto >= nemicoy12) \
                        and (main_y + oggetto <= nemicoy12 + oggetto_n):
                    if (main_x + oggetto >= nemicox12) and (main_x + oggetto <= nemicox12 + oggetto_n):
                        if (main_y + oggetto >= nemicoy12) and (main_y + oggetto <= nemicoy12 + oggetto_n):
                            cattura.play()
                            nemicox12 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy12 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            listainizio += 1
                            if listainizio - 1 == 100:
                                avviso.play()
                                vita += 1
                            elif len(lista) >= 60:
                                listainizio += 2
                            nemicox3 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy3 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox2 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy2 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox4 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy4 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox5 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy5 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox6 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy6 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox7 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy7 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox8 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy8 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox9 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy9 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox10 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy10 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            nemicox11 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy11 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico strano 13
        # ------------------------------------------------------------------------------------
        if len(lista) > 0:
            if (main_x >= nemicox13) and (main_x <= nemicox13 + oggetto_n) or (main_x + oggetto >= nemicox13) \
                    and (main_x + oggetto <= nemicox13 + oggetto_n):
                if (main_y >= nemicoy13) and (main_y <= nemicoy13 + oggetto_n) or (main_y + oggetto >= nemicoy13) \
                        and (main_y + oggetto <= nemicoy13 + oggetto_n):
                    if (main_x + oggetto >= nemicox13) and (main_x + oggetto <= nemicox13 + oggetto_n):
                        if (main_y + oggetto >= nemicoy13) and (main_y + oggetto <= nemicoy13 + oggetto_n):
                            cattura.play()
                            nemicox13 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy13 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            listainizio += 1
                            if listainizio - 1 == 100:
                                avviso.play()
                                vita += 1
                            elif len(lista) >= 60:
                                listainizio += 2
                            craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico strano 14
        # ------------------------------------------------------------------------------------
        if len(lista) > 0:
            if (main_x >= nemicox14) and (main_x <= nemicox14 + oggetto_n) or (main_x + oggetto >= nemicox14) \
                    and (main_x + oggetto <= nemicox14 + oggetto_n):
                if (main_y >= nemicoy14) and (main_y <= nemicoy14 + oggetto_n) or (main_y + oggetto >= nemicoy14) \
                        and (main_y + oggetto <= nemicoy14 + oggetto_n):
                    if (main_x + oggetto >= nemicox14) and (main_x + oggetto <= nemicox14 + oggetto_n):
                        if (main_y + oggetto >= nemicoy14) and (main_y + oggetto <= nemicoy14 + oggetto_n):
                            cattura.play()
                            nemicox14 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy14 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            listainizio += 1
                            if listainizio - 1 == 100:
                                vita += 1
                                avviso.play()
                            elif len(lista) >= 60:
                                listainizio += 2
                            craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico strano 15
        # ------------------------------------------------------------------------------------
        if len(lista) > 5:
            if (main_x >= nemicox15) and (main_x <= nemicox15 + oggetto_n) or (main_x + oggetto >= nemicox15) and (
                            main_x + oggetto <= nemicox15 + oggetto_n):
                if (main_y >= nemicoy15) and (main_y <= nemicoy15 + oggetto_n) or (main_y + oggetto >= nemicoy15) and (
                                main_y + oggetto <= nemicoy15 + oggetto_n):
                    if (main_x + oggetto >= nemicox15) and (main_x + oggetto <= nemicox15 + oggetto_n):
                        if (main_y + oggetto >= nemicoy15) and (main_y + oggetto <= nemicoy15 + oggetto_n):
                            cattura.play()
                            nemicox15 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy15 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            listainizio += 1
                            if listainizio - 1 == 100:
                                avviso.play()
                                vita += 1
                            craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
        # ------------------------------------------------------------------------------------
        # collisione nemico strano 16
        # ------------------------------------------------------------------------------------
        if len(lista) > 0:
            if (main_x >= nemicox16) and (main_x <= nemicox16 + oggetto_n) or (main_x + oggetto >= nemicox16) and (
                            main_x + oggetto <= nemicox16 + oggetto_n):
                if (main_y >= nemicoy16) and (main_y <= nemicoy16 + oggetto_n) or (main_y + oggetto >= nemicoy16) and (
                                main_y + oggetto <= nemicoy16 + oggetto_n):
                    if (main_x + oggetto >= nemicox16) and (main_x + oggetto <= nemicox16 + oggetto_n):
                        if (main_y + oggetto >= nemicoy16) and (main_y + oggetto <= nemicoy16 + oggetto_n):
                            cattura.play()
                            nemicox16 = round(
                                random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                            nemicoy16 = round(
                                random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                            listainizio += 2
                            if listainizio - 1 == 100:
                                avviso.play()
                                vita += 1
                            craterex1 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey1 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex2 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey2 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
                            craterex3 = round(random.randrange(0, infoObject.current_w - gran_c) / gran_c) * gran_c
                            craterey3 = round(random.randrange(0, infoObject.current_h - gran_c) / gran_c) * gran_c
            # ------------------------------------------------------------------------------------
            # collisione nemico 17
            # ------------------------------------------------------------------------------------
            if len(lista) > 1:
                if (main_x >= nemicox17) and (main_x <= nemicox17 + oggetto_n) or (main_x + oggetto >= nemicox17) and (
                                main_x + oggetto <= nemicox17 + oggetto_n):
                    if (main_y >= nemicoy17) and (main_y <= nemicoy17 + oggetto_n) or (
                            main_y + oggetto >= nemicoy17) and (
                                    main_y + oggetto <= nemicoy17 + oggetto_n):
                        if (main_x + oggetto >= nemicox17) and (main_x + oggetto <= nemicox17 + oggetto_n):
                            if (main_y + oggetto >= nemicoy17) and (main_y + oggetto <= nemicoy17 + oggetto_n):
                                cattura.play()
                                nemicox17 = round(
                                    random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                                nemicoy17 = round(
                                    random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                                listainizio += 1
                                if listainizio - 1 == 100:
                                    avviso.play()
                                    vita += 1
            # ------------------------------------------------------------------------------------
            # collisione nemico 18
            # ------------------------------------------------------------------------------------
            if len(lista) > 0:
                if (main_x >= nemicox18) and (main_x <= nemicox18 + oggetto_n) or (main_x + oggetto >= nemicox18) and (
                                main_x + oggetto <= nemicox18 + oggetto_n):
                    if (main_y >= nemicoy18) and (main_y <= nemicoy18 + oggetto_n) or (
                            main_y + oggetto >= nemicoy18) and (
                                    main_y + oggetto <= nemicoy18 + oggetto_n):
                        if (main_x + oggetto >= nemicox18) and (main_x + oggetto <= nemicox18 + oggetto_n):
                            if (main_y + oggetto >= nemicoy18) and (main_y + oggetto <= nemicoy18 + oggetto_n):
                                cattura.play()
                                nemicox18 = round(
                                    random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                                nemicoy18 = round(
                                    random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                                listainizio += 1
                                if listainizio - 1 == 100:
                                    avviso.play()
                                    vita += 1
            # ------------------------------------------------------------------------------------
            # collisione nemico 19
            # ------------------------------------------------------------------------------------
            if len(lista) > 0:
                if (main_x >= nemicox19) and (main_x <= nemicox19 + oggetto_n) or (main_x + oggetto >= nemicox19) and (
                                main_x + oggetto <= nemicox19 + oggetto_n):
                    if (main_y >= nemicoy19) and (main_y <= nemicoy19 + oggetto_n) or (
                            main_y + oggetto >= nemicoy19) and (
                                    main_y + oggetto <= nemicoy19 + oggetto_n):
                        if (main_x + oggetto >= nemicox19) and (main_x + oggetto <= nemicox19 + oggetto_n):
                            if (main_y + oggetto >= nemicoy19) and (main_y + oggetto <= nemicoy19 + oggetto_n):
                                cattura.play()
                                nemicox19 = round(
                                    random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                                nemicoy19 = round(
                                    random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                                listainizio += 1
                                if listainizio - 1 == 100:
                                    avviso.play()
                                    vita += 1
            # ------------------------------------------------------------------------------------
            # collisione nemico 20
            # ------------------------------------------------------------------------------------
            if len(lista) > 0:
                if (main_x >= nemicox20) and (main_x <= nemicox20 + oggetto_n) or (main_x + oggetto >= nemicox20) and (
                                main_x + oggetto <= nemicox20 + oggetto_n):
                    if (main_y >= nemicoy20) and (main_y <= nemicoy20 + oggetto_n) or (
                            main_y + oggetto >= nemicoy20) and (
                                    main_y + oggetto <= nemicoy20 + oggetto_n):
                        if (main_x + oggetto >= nemicox20) and (main_x + oggetto <= nemicox20 + oggetto_n):
                            if (main_y + oggetto >= nemicoy20) and (main_y + oggetto <= nemicoy20 + oggetto_n):
                                cattura.play()
                                nemicox20 = round(
                                    random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                                nemicoy20 = round(
                                    random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                                listainizio += 1
                                if listainizio - 1 == 100:
                                    avviso.play()
                                    vita += 1
            # ------------------------------------------------------------------------------------
            # collisione nemico 21
            # ------------------------------------------------------------------------------------
            if len(lista) > 0:
                if (main_x >= nemicox21) and (main_x <= nemicox21 + oggetto_n) or (main_x + oggetto >= nemicox21) and (
                                main_x + oggetto <= nemicox21 + oggetto_n):
                    if (main_y >= nemicoy21) and (main_y <= nemicoy21 + oggetto_n) or (
                            main_y + oggetto >= nemicoy21) and (
                                    main_y + oggetto <= nemicoy21 + oggetto_n):
                        if (main_x + oggetto >= nemicox21) and (main_x + oggetto <= nemicox21 + oggetto_n):
                            if (main_y + oggetto >= nemicoy21) and (main_y + oggetto <= nemicoy21 + oggetto_n):
                                cattura.play()
                                nemicox21 = round(
                                    random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                                nemicoy21 = round(
                                    random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                                listainizio += 1
                                if listainizio - 1 == 100:
                                    avviso.play()
                                    vita += 1
            # ------------------------------------------------------------------------------------
            # collisione nemico 22
            # ------------------------------------------------------------------------------------
            if len(lista) > 0:
                if (main_x >= nemicox22) and (main_x <= nemicox22 + oggetto_n) or (main_x + oggetto >= nemicox22) and (
                                main_x + oggetto <= nemicox22 + oggetto_n):
                    if (main_y >= nemicoy22) and (main_y <= nemicoy22 + oggetto_n) or (
                            main_y + oggetto >= nemicoy22) and (
                                    main_y + oggetto <= nemicoy22 + oggetto_n):
                        if (main_x + oggetto >= nemicox22) and (main_x + oggetto <= nemicox22 + oggetto_n):
                            if (main_y + oggetto >= nemicoy22) and (main_y + oggetto <= nemicoy22 + oggetto_n):
                                cattura.play()
                                nemicox22 = round(
                                    random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                                nemicoy22 = round(
                                    random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                                listainizio += 1
                                if listainizio - 1 == 100:
                                    avviso.stop()
                                    vita += 1
            # ------------------------------------------------------------------------------------
            # collisione nemico 23
            # ------------------------------------------------------------------------------------
            if len(lista) > 0:
                if (main_x >= nemicox23) and (main_x <= nemicox23 + oggetto_n) or (main_x + oggetto >= nemicox23) and (
                                main_x + oggetto <= nemicox23 + oggetto_n):
                    if (main_y >= nemicoy23) and (main_y <= nemicoy23 + oggetto_n) or (
                            main_y + oggetto >= nemicoy23) and (
                                    main_y + oggetto <= nemicoy23 + oggetto_n):
                        if (main_x + oggetto >= nemicox23) and (main_x + oggetto <= nemicox23 + oggetto_n):
                            if (main_y + oggetto >= nemicoy23) and (main_y + oggetto <= nemicoy23 + oggetto_n):
                                cattura.play()
                                nemicox23 = round(
                                    random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                                nemicoy23 = round(
                                    random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                                listainizio += 1
                                if listainizio - 1 == 100:
                                    avviso.play()
                                    vita += 1
            # ------------------------------------------------------------------------------------
            # collisione nemico 24
            # ------------------------------------------------------------------------------------
            if len(lista) > 0:
                if (main_x >= nemicox24) and (main_x <= nemicox24 + oggetto_n) or (main_x + oggetto >= nemicox24) and (
                                main_x + oggetto <= nemicox24 + oggetto_n):
                    if (main_y >= nemicoy24) and (main_y <= nemicoy24 + oggetto_n) or (
                            main_y + oggetto >= nemicoy24) and (
                                    main_y + oggetto <= nemicoy24 + oggetto_n):
                        if (main_x + oggetto >= nemicox24) and (main_x + oggetto <= nemicox24 + oggetto_n):
                            if (main_y + oggetto >= nemicoy24) and (main_y + oggetto <= nemicoy24 + oggetto_n):
                                cattura.play()
                                nemicox24 = round(
                                    random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                                nemicoy24 = round(
                                    random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                                listainizio += 1
                                if listainizio - 1 == 100:
                                    avviso.play()
                                    vita += 1
            # ------------------------------------------------------------------------------------
            # collisione nemico 25 (tranello)
            # ------------------------------------------------------------------------------------
            if len(lista) > 2:
                if (main_x >= nemicox25) and (main_x <= nemicox25 + oggetto_n) or (main_x + oggetto >= nemicox25) and (
                                main_x + oggetto <= nemicox25 + oggetto_n):
                    if (main_y >= nemicoy25) and (main_y <= nemicoy25 + oggetto_n) or (
                            main_y + oggetto >= nemicoy25) and (
                                    main_y + oggetto <= nemicoy25 + oggetto_n):
                        if (main_x + oggetto >= nemicox25) and (main_x + oggetto <= nemicox25 + oggetto_n):
                            if (main_y + oggetto >= nemicoy25) and (main_y + oggetto <= nemicoy25 + oggetto_n):
                                cattura.play()
                                nemicox25 = round(
                                    random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
                                nemicoy25 = round(
                                    random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n
                                lapide.play()
                                listainizio -= 3
                                lista.remove(testa)
                                if vita <= 0:
                                    m_gioco.stop()
                                    gameOver = True
                                elif listainizio - 1 <= 0:
                                    avviso.play()
                                    vita -= 1
        clock.tick(velocita)
    pygame.quit()
    quit()
inizioGioco()
inizio()
