#!/usr/bin/python
# coding=utf-8

import random
import pygame

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
# avviso = pygame.mixer.Sound('avviso.wav')

# suono collisione muro
preso = pygame.mixer.Sound('preso3.wav')

# uscita gioco
schianto = pygame.mixer.Sound('uscita1.wav')

# suono collisione cratere
lapide = pygame.mixer.Sound('morte6.wav')

# suono record
# applauso = pygame.mixer.Sound('allarme1.wav')

# aggiungo lo sfondo
sfondo = pygame.image.load('sfondo4.jpg')

# sfondo intro gioco
sfondo1 = pygame.image.load('intro.jpg')

# sfondo seleziona
sfondo2 = pygame.image.load('seleziona.jpg')

# icona gioco
# pygame.display.set_icon(pygame.image.load('supermen1.png'))

# qui si inserisce il titolo nello schermo gioco
pygame.display.set_caption('SE MI FAI MANGIARE ......ATTENTO...........')



# immagine giocatore
immagine = pygame.image.load('giocatore.png')
immagine1 = pygame.image.load('prendimi3.png')
immagine2 = pygame.image.load('prendimi4.png')
immagine3 = pygame.image.load('prendimi5.png')
# immagine4 = pygame.image.load('prendimi6.png')
# immagine5 = pygame.image.load('prendimi7.png')

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
oggetto = 10
oggetto_n = 35
gran_c = 23
palla = 25



# schermata d'inizio

def inizioGioco():
    ini = True
    while ini:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
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
        messagioSchermo('Premi G per giocare, premi U per uscire', nero, 180, 'medio')
        messagioSchermo('Premi spazio per mettere in pausa', nero, 210)
        messagioSchermo('Premi spazio per uscire dalla pausa', nero, 230)
        pygame.display.update()
        clock.tick(velocita)


# palla
def rompi():
    schermo.blit(simpatica, [x, y])



# palla
x = infoObject.current_w
y = 0
vx = palla
vy = palla



# salvataggio punteggio
def Punteggio(listainizio):
    global record, vita
    testo = grandeFont.render('Punteggio: %d' % (listainizio - 1), True, giallo)
    schermo.blit(testo, [infoObject.current_w / 2 - 150, 0])
    record_file = open("FileGioco.txt", "r")
    record = int(record_file.read())
    record_file.close()
    testo1 = grandeFont.render('Record: %d' % (record), True, blu)
    schermo.blit(testo1, [infoObject.current_w / 2 - 150, 50])
    testo2 = grandeFont.render('Vita: %d' % (vita), True, giallo)
    schermo.blit(testo2, [infoObject.current_w / 1.3 - 150, 50])

    if listainizio - 1 > record:
        record_file = open("FileGioco.txt", "w")
        record_file.write('\n' + str(listainizio - 1))
        record_file.close()


# pausa
def pausa():
    testo = piccoloFont.render('Premi spazio per pausa, ripremi per continuare', True, rosso)
    schermo.blit(testo, [40, 40])


# parametri muro (ostacolo)
xl = infoObject.current_h
yl = 0
xs = 25
spazio = random.randrange(30, 150)
ys = 500
xl_velocita = 4.4


def giocatore(lista):
    global trasforma
    global vita
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


def messagioSchermo(msg, color, margine_y = 0, size = 'piccolo'):
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

    # nemico 1
    nemicox = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n

    # nemico 2
    nemicox2 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy2 = round(random.randrange(10, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n

    # nemico 3
    nemicox3 = round(random.randrange(0, infoObject.current_w - oggetto_n) / oggetto_n) * oggetto_n
    nemicoy3 = round(random.randrange(0, infoObject.current_h - oggetto_n) / oggetto_n) * oggetto_n


    # direzione, inizio gioco movimento destra sinistra
    main_x_change = 0
    main_y_change = 0
    lista = []
    listainizio = 1
    vita = 3


    # il ciclo while cattura gli eventi tramite event
    while not gioco:
        while gameOver:
            schermo.blit(sfondo2, [0, 0])
            messagioSchermo('NOOO.....!!!!!', verde, - 80, 'grande')
            messagioSchermo('Premi R per ripetere', verde, 30, 'medio')
            messagioSchermo('Premi U per uscire', verde, 80, 'medio')
            messagioSchermo('Smile recuperati: ' + str(listainizio -1), rosso, -20, 'medio')
            messagioSchermo('Record: %d ' % (record), rosso, -160, 'grande')
            messagioSchermo('Vita: %d' % (vita), giallo, 140, 'grande')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        gioco = True
                        gameOver = False
                    if event.key == pygame.K_r:
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

        # parametri schermo
        if len(lista) <= 19:
            if main_x >= infoObject.current_w - 120 or main_x < 30 or main_y < 30 or main_y >= infoObject.current_h - 110:
                m_gioco.stop()
                schianto.play()
                # gameOver = True

        # schermo
        main_x += main_x_change
        main_y += main_y_change
        schermo.blit(sfondo, [0, 0])

        # nemico
        schermo.blit(immagine1, [nemicox, nemicoy, oggetto_n, oggetto_n])
        schermo.blit(immagine2, [nemicox2, nemicoy2, oggetto_n, oggetto_n])
        schermo.blit(immagine3, [nemicox3, nemicoy3, oggetto_n, oggetto_n])
        #

        # giocatore
        testa = []
        testa.append(main_x)
        testa.append(main_y)
        lista.append(testa)

        if len(lista) > listainizio:
            del lista[0]

        # il vermicello non puo toccarsi
        for iniziolista in lista[:-50]:
            if iniziolista == testa:
                m_gioco.stop()
                lapide.play()
                gameOver = True

        giocatore(lista)
        rompi()

        Punteggio(listainizio)

        pausa()

        # movimento palla
        x += vx
        y += vy
        if x >= infoObject.current_w - 60:
            vx = -2
        if x < 5:
            vx = 3
        if y >= infoObject.current_h:
            vy = -4
        if y < 3:
            vy = 2

        # collisione palla

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
                                gameOver = True
                            elif listainizio - 1 <= 0:
                                vita -= 1








        pygame.display.update()

        # collisione nemico 1
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

        # collisione nemico 2
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

        # collisione nemico 3
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


        clock.tick(velocita)
    pygame.quit()
    quit()


inizioGioco()
inizio()
