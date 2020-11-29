    
#!/usr/bin/python

# Импортируем библиотеки
import pygame 
from pygame.locals import *
import random
import copy

# Загрузка изображений
icon =  pygame.image.load('resources/icon.png')
cBack = pygame.image.load('resources/cards/cardback.png')
diamondA = pygame.image.load('resources/cards/ad.png')
clubA =  pygame.image.load('resources/cards/ac.png')
heartA = pygame.image.load('resources/cards/ah.png')
spadeA = pygame.image.load('resources/cards/as.png')
diamond2 = pygame.image.load('resources/cards/2d.png')
club2 = pygame.image.load('resources/cards/2c.png')
heart2 = pygame.image.load('resources/cards/2h.png')
spade2 = pygame.image.load('resources/cards/2s.png')
diamond3 = pygame.image.load('resources/cards/3d.png')
club3 = pygame.image.load('resources/cards/3c.png')
heart3 = pygame.image.load('resources/cards/3h.png')
spade3 = pygame.image.load('resources/cards/3s.png')
diamond4 = pygame.image.load('resources/cards/4d.png')
club4 = pygame.image.load('resources/cards/4c.png')
heart4 = pygame.image.load('resources/cards/4h.png')
spade4 = pygame.image.load('resources/cards/4s.png')
diamond5 = pygame.image.load('resources/cards/5d.png')
club5 = pygame.image.load('resources/cards/5c.png')
heart5 = pygame.image.load('resources/cards/5h.png')
spade5 = pygame.image.load('resources/cards/5s.png')
diamond6 = pygame.image.load('resources/cards/6d.png')
club6 = pygame.image.load('resources/cards/6c.png')
heart6 = pygame.image.load('resources/cards/6h.png')
spade6 = pygame.image.load('resources/cards/6s.png')
diamond7 = pygame.image.load('resources/cards/7d.png')
club7 = pygame.image.load('resources/cards/7c.png')
heart7 = pygame.image.load('resources/cards/7h.png')
spade7 = pygame.image.load('resources/cards/7s.png')
diamond8 = pygame.image.load('resources/cards/8d.png')
club8 = pygame.image.load('resources/cards/8c.png')
heart8 = pygame.image.load('resources/cards/8h.png')
spade8 = pygame.image.load('resources/cards/8s.png')
diamond9 = pygame.image.load('resources/cards/9d.png')
club9 = pygame.image.load('resources/cards/9c.png')
heart9 = pygame.image.load('resources/cards/9h.png')
spade9 = pygame.image.load('resources/cards/9s.png')
diamond10 = pygame.image.load('resources/cards/10d.png')
club10 = pygame.image.load('resources/cards/10c.png')
heart10 = pygame.image.load('resources/cards/10h.png')
spade10 = pygame.image.load('resources/cards/10s.png')
diamondJ = pygame.image.load('resources/cards/jd.png')
clubJ = pygame.image.load('resources/cards/jc.png')
heartJ = pygame.image.load('resources/cards/jh.png')
spadeJ = pygame.image.load('resources/cards/js.png')
diamondQ = pygame.image.load('resources/cards/qd.png')
clubQ = pygame.image.load('resources/cards/qc.png')
heartQ = pygame.image.load('resources/cards/qh.png')
spadeQ = pygame.image.load('resources/cards/qs.png')
diamondK = pygame.image.load('resources/cards/kd.png')
clubK = pygame.image.load('resources/cards/kc.png')
heartK = pygame.image.load('resources/cards/kh.png')
spadeK = pygame.image.load('resources/cards/ks.png')

#Установка иконки на окно игры
pygame.display.set_icon(icon)

#Глобальные константы
black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)

cards = [ diamondA, clubA, heartA, spadeA, \
          diamond2, club2, heart2, spade2, \
          diamond3, club3, heart3, spade3, \
          diamond4, club4, heart4, spade4, \
          diamond5, club5, heart5, spade5, \
          diamond6, club6, heart6, spade6, \
          diamond7, club7, heart7, spade7, \
          diamond8, club8, heart8, spade8, \
          diamond9, club9, heart9, spade9, \
          diamond10, club10, heart10, spade10, \
          diamondJ, clubJ, heartJ, spadeJ, \
          diamondQ, clubQ, heartQ, spadeQ, \
          diamondK, clubK, heartK, spadeK ]
cardA = [ diamondA, clubA, heartA, spadeA ]
card2 = [ diamond2, club2, heart2, spade2 ]
card3 = [ diamond3, club3, heart3, spade3 ]
card4 = [ diamond4, club4, heart4, spade4 ]
card5 = [ diamond5, club5, heart5, spade5 ]
card6 = [ diamond6, club6, heart6, spade6 ]
card7 = [ diamond7, club7, heart7, spade7 ]
card8 = [ diamond8, club8, heart8, spade8 ]
card9 = [ diamond9, club9, heart9, spade9 ]
card10 = [ diamond10, club10, heart10, spade10, \
            diamondJ, clubJ, heartJ, spadeJ, \
            diamondQ, clubQ, heartQ, spadeQ, \
            diamondK, clubK, heartK, spadeK ]

def getAmt(card):
    ''' Возвращает сумму, которую стоит карта.
Например, Ace по умолчанию 11. 10/Валет/Дама/Король 10.'''
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        print ("Генерация провалена...")
        exit()

def genCard(cList, xList):
    '''Создает карту из cList, удаляет ее из cList и добавляет ее в xList.
Возвращает, если карта-Туз и просто 2 3 4 карта.'''
    cA = 0
    card = random.choice(cList)
    cList.remove(card)
    xList.append(card)
    if card in cardA:
        cA = 1
    return card, cA

def initGame(cList, uList, dList):
    '''Генерирует две карты для дилера и пользователя, по одной за раз для каждого.
Возвращает, если карта является тузом и общее количество карт на человека.'''
    userA = 0
    dealA = 0
    card1, cA = genCard(cList, uList)
    userA += cA
    card2, cA = genCard(cList, dList)
    dealA += cA
    card3, cA = genCard(cList, uList)
    userA += cA
    card4, cA = genCard(cList, dList)
    dealA += cA
    return getAmt(card1) + getAmt(card3), userA, getAmt(card2) + getAmt(card4), dealA

def main():
    ccards = copy.copy(cards)
    stand = False
    userCard = []
    dealCard = []
    winNum = 0
    loseNum = 0
    moneyNum = random.randint(1,5)
    stavka = 1
    #Инициализация игры
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Игра BlackJack')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Взять ещё', 0, black)
    standTxt = font.render('Достаточно', 0, black)
    doubleTxt = font.render('Удвоить ставку',0,black)
    restartTxt = font.render('Перезапустить', 0, black)
    gameoverTxt = font.render('Вы проиграли!', 0, white)
    moneyNoTxt = font.render('У вас закончились деньги! Пора домой за новой партией!',0,white)
    userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)

    #Fill Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((40, 150, 15))
    hitB = pygame.draw.rect(background, gray, (28, 445, 75, 25))
    standB = pygame.draw.rect(background, gray, (110, 445, 75, 25))
    ratioB = pygame.draw.rect(background, gray, (535, 395, 95, 70))
    doubleB = pygame.draw.rect(background,gray, (198, 445, 85, 25))

    #Бесконечный цикл
    while True:
        #Проверяем если игрок проиграл,то
        gameover = True if (userSum >= 21 and userA == 0) or len(userCard) == 5 else False
        if len(userCard) == 2 and userSum == 21:
            gameover = True
        elif len(dealCard) == 2 and dealSum == 21:
            gameover = True
        elif moneyNum <= 0:
            gameover = True

        #Обновление фона под тексты денег игрока количества выйграшей и проиграшей.
        scoreDillerTxt = font.render('Текущее количество очков у Диллера: %i' % dealSum,1,black)
        scorePlayerTxt = font.render('Текущее количество очков у Игрока: %i' % userSum,1,black)
        stavkaTxt = font.render('Текущая ставка игрока: %i' % stavka,1,black)
        moneyTxt = font.render('Денег у игрока: %i' % moneyNum,1, black)
        winTxt = font.render('Побед: %i' % winNum, 1, black)
        loseTxt = font.render('Поражений: %i' % loseNum, 1, black)

        #Проверки нажатий по кнопкам Взять ещё или достаточно
        for event in pygame.event.get():
            if event.type == quit:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(pygame.mouse.get_pos()):
                #Диллер дает игроку карту, если он не нарушает правила блэкджека.
                card, cA = genCard(ccards, userCard)
                userA += cA
                userSum += getAmt(card)
                print ("Игрок: %i" % userSum)
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and doubleB.collidepoint(pygame.mouse.get_pos()):
                if(stavka < moneyNum):
                    stavka *=2
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
                #when player stands, the dealer plays
                stand = True
                while dealSum <= userSum and dealSum < 17:
                    card, cA = genCard(ccards, dealCard)
                    dealA += cA
                    dealSum += getAmt(card)
                    print ("Диллер: %i" % dealSum)
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()):
                #restarts the game, updating scores
                if userSum == dealSum:
                    pass
                elif userSum <= 21 and len(userCard) == 5:
                    winNum += 1
                    moneyNum += stavka * 1.5
                elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                    winNum += 1
                else:
                    if(moneyNum > 0):
                        moneyNum -=stavka
                        loseNum += 1
                        stavka = 1
                    else:
                        moneyNum = random.randint(1,5)
                        loseNum = 0
                        winNum = 0
                        stavka = 1
                gameover = False
                stand = False
                userCard = []
                dealCard = []
                ccards = copy.copy(cards)
                userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)
                restartB = pygame.draw.rect(background, (40, 150, 15), (260, 225, 105, 25))

        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (39, 448))
        screen.blit(standTxt, (116, 448))
        screen.blit(doubleTxt,(198,448))
        screen.blit(scoreDillerTxt,(5,158))
        screen.blit(stavkaTxt,(5,238))
        screen.blit(scorePlayerTxt,(5,258))
        screen.blit(moneyTxt, (535,398))
        screen.blit(winTxt, (535, 423))
        screen.blit(loseTxt, (535, 448))

        #Отображение карт Диллера.
        for card in dealCard:
            x = 10 + dealCard.index(card) * 110
            screen.blit(card, (x, 10))
        screen.blit(cBack, (120, 10))

        #Отображение карт Игрока.
        for card in userCard:
            x = 10 + userCard.index(card) * 110
            screen.blit(card, (x, 295))

        #когда игра закончена, рисует кнопку перезапуска и текст, и показывает вторую карту дилера.
        if gameover or stand:
            if(moneyNum > 0):
                screen.blit(gameoverTxt, (270, 200))
            else:
                screen.blit(moneyNoTxt, (150, 200))
            restartB = pygame.draw.rect(background, gray, (260, 225, 105, 25))
            screen.blit(restartTxt, (270, 228))
            screen.blit(dealCard[1], (120, 10))
            
        pygame.display.update()
            

if __name__ == '__main__':
    main()