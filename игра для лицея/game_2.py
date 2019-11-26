# coding=utf-8
import pygame
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber, QLineEdit
from game_2 import *
from PyQt5.QtGui import QPixmap


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500) # создаем окно
        self.setWindowTitle('Главное меню')


        self.btn = QPushButton('Начать игру', self)  # создаем кнопку начать игру
        self.btn.resize(150, 150)
        self.btn.move(170, 30)
        self.btn.setStyleSheet("background-color: #98FF98")
        self.btn.clicked.connect(self.start_game)

        self.btn = QPushButton('Выйти из игры', self)  # создаем кнопку выйти из игры
        self.btn.resize(150, 150)
        self.btn.move(330, 30)
        self.btn.setStyleSheet("background-color: #008000")
        self.btn.clicked.connect(self.finish_game)

        self.btn = QPushButton('Информация:', self)  # создаем кнопку информация
        self.btn.resize(150, 150)
        self.btn.move(10, 30)
        self.btn.setStyleSheet("background-color: #008000")
        self.btn.clicked.connect(self.info_game)

        self.label = QLabel(self)  # поле, в которм появится текст
        self.label.resize(700, 150)
        self.label.move(30, 150)

        pixmap = QPixmap('L1.png')  # фото справа
        self.image = QLabel(self)
        self.image.setPixmap(pixmap)
        self.image.resize(300, 300)
        self.image.move(380, 200)

        pixmap1 = QPixmap('tower.png')  # фото слева
        self.image = QLabel(self)
        self.image.setPixmap(pixmap1)
        self.image.resize(200, 200)
        self.image.move(140, 220)

        pixmap2 = QPixmap('R1.png')  # фото слева
        self.image = QLabel(self)
        self.image.setPixmap(pixmap2)
        self.image.resize(300, 300)
        self.image.move(40, 200)

    def finish_game(self):
        self.close()  # закрытие окна
        quit()
    def start_game(self):
        main()  # запускает игру

    def info_game(self):
        self.label.setText("Игра довольно простая, в ней считается количество сделанных персонажем шагов и\n "
                           "пройденное расстояние в пикселях.Если хотите начать игру, нажмите 'Начать игру'")
        # выводит текст

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = Menu()
    m.show()
    sys.exit(app.exec())


def main():
    pygame.init()
    window = pygame.display.set_mode((1920, 1080))  # создаем окно
    pygame.display.set_caption('Game for YL')  # добавляем имя игры
    font = pygame.font.SysFont("comicsans", 30, True)
    steps = 0

    class Player(object):  # создаем класс игрока с параметрами
        def __init__(self, x, y, width, height, step):  # координаты по x и y ширина и высота
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5  # скорость игрока
            self.left = False
            self.right = False
            self.walkCount = 0
            self.standing = True
            self.steps = step

        def draw(self, window):  # рисуем героя в зависимости от положения
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if self.left and self.steps > 500:
                window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right and self.steps > 500:
                window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right is False and self.right is False and self.steps > 500:
                window.blit(playerStand, (self.x, self.y))
            elif self.left and self.steps < 500:
                window.blit(walkLeft_B[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right and self.steps < 500:
                window.blit(walkRight_B[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right is False and self.right is False and self.steps < 500:
                window.blit(playerStand_B, (self.x, self.y))

    PLATFORM_WIDTH = 64  # высота блока
    PLATFORM_HEIGHT = 64  # ширина блока
    ROAD = pygame.image.load('platformPack_tile016.png')  # дорга
    KUST = pygame.image.load('foliagePack_019.png')  # куст
    TREE = pygame.image.load('foliagePack_009.png')  # дерево
    TOWER = pygame.image.load('tower.png')  # башня
    GAME_OVER = pygame.image.load('game_over.png')

    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'),
                 pygame.image.load('R3.png'), pygame.image.load('R4.png'),
                 pygame.image.load('R5.png'), pygame.image.load('R6.png'),
                 pygame.image.load('R7.png'), pygame.image.load('R8.png'),
                 pygame.image.load('R9.png')]

    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'),
                pygame.image.load('L3.png'), pygame.image.load('L4.png'),
                pygame.image.load('L5.png'), pygame.image.load('L6.png'),
                pygame.image.load('L7.png'), pygame.image.load('L8.png'),
                pygame.image.load('L9.png')]
    # моделька игрока в движении
    playerStand = pygame.image.load('standing.png')  # игрок стоит
    walkRight_B = [pygame.image.load('R1_B.png'), pygame.image.load('R2_B.png'),
                   pygame.image.load('R3_B.png'), pygame.image.load('R4_B.png'),
                   pygame.image.load('R5_B.png'), pygame.image.load('R6_B.png'),
                   pygame.image.load('R7_B.png'), pygame.image.load('R8_B.png'),
                   pygame.image.load('R9_B.png')]

    walkLeft_B = [pygame.image.load('L1_B.png'), pygame.image.load('L2_B.png'),
                  pygame.image.load('L3_B.png'), pygame.image.load('L4_B.png'),
                  pygame.image.load('L5_B.png'), pygame.image.load('L6_B.png'),
                  pygame.image.load('L7_B.png'), pygame.image.load('L8_B.png'),
                  pygame.image.load('L9_B.png')]
    # моделька игрока в движении
    playerStand_B = pygame.image.load('standing_B.png')  # игрок стоит
    clock = pygame.time.Clock()

    # карта уровня
    level = [
        "  !!                          ",
        "  !!      ^           ^       ",
        "  !!!!!!!!!!!!!!  ^      @    ",
        "  !!!!!!!!!!!!!!         ^    ",
        "   @    ^    !!!  @    ^      ",
        "       @     !!!    ^ @       ",
        "             !!! ^       @    ",
        "    @   @    !!!        ^     ",
        "  ^   @      !!!    @    @    ",
        "   @     &   !!! &            ",
        "       ^     !!!      ^  ^    ",
        "     ^       !!!    ^         ",
        "             !!!         @    ",
        "  ^    @     !!!         ^    ",
        "      ^      !!!    ^   ^     ",
        "             !!!              "]

    def draw_game_window():  # рисуем карту
        window.fill((62, 117, 59))
        x_block = y_block = 0  # координаты
        for row in level:  # вся строка в level
            for col in row:  # каждый символ в level
                if col == '^' and hero.x != x_block and hero.y != y_block:  # рисуем кусты
                    window.blit(KUST, (x_block, y_block))
                elif col == '&':  # рисуем башню
                    window.blit(TOWER, (x_block, y_block))
                elif col == '!':  # рисуем дорогу
                    window.blit(ROAD, (x_block, y_block))
                elif col == '@':  # рисуем деревья
                    window.blit(TREE, (x_block, y_block))

                x_block += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y_block += PLATFORM_HEIGHT  # то же самое и с высотой
            x_block = 0
        hero.draw(window)

        text = font.render("STEPS: " + str(hero.steps // 5), 1,
                           (255, 255, 255))  # Arguments are: text, anti-aliasing, color
        window.blit(text, (1700, 10))
        distance = font.render("DISTANCE: " + str(hero.steps * 5) + "px", 1,
                               (255, 255, 255))  # Arguments are: text, anti-aliasing, color
        window.blit(distance, (1700, 30))

    hero = Player(120, 90, 64, 64, steps)  # создаем игрока, используя консьруктор класса Player
    run = True
    while run:  # основной цикл игры
        clock.tick(27)  # 27 кадров в секунду

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # если нажать крестик игра завершается без ошибки
                run = False

        keys = pygame.key.get_pressed()  # все клавиши

        if keys[pygame.K_a] and hero.x > hero.vel + 5:  # двжение влево
            hero.x -= hero.vel
            hero.left = True  # направление игрока
            hero.right = False  # направление игрока
            hero.standing = False
            hero.steps += 1


        elif keys[pygame.K_d] and hero.x < 1920 - hero.width - 10 :  # двжение вправо
            hero.x += hero.vel
            hero.left = False  # направление игрока
            hero.right = True  # направление игрока
            hero.standing = False
            hero.steps += 1

        elif keys[pygame.K_w] and hero.y > hero.vel + 5:  # двжение вверх
            hero.y -= hero.vel
            hero.left = False  # направление игрока
            hero.right = True  # направление игрока
            hero.standing = False
            hero.steps += 1

        elif keys[pygame.K_s] and hero.y < 1080 - hero.height - 10:  # движение вниз
            hero.y += hero.vel
            hero.left = True  # направление игрока
            hero.right = False  # направление игрока
            hero.standing = False
            hero.steps += 1

        else:
            hero.left = False  # направление игрока
            hero.right = False  # направление игрока
            hero.walkCount = 0

        draw_game_window()  # рисуем элементы
        pygame.display.update()  # обновляем окно

    pygame.quit()  # обязательная строчка
