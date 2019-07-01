import math
import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))  # 定义屏幕大小
pygame.display.set_caption("The Pie Game - Press 1 ,2,3,4")  # 命名游戏的名字
myfont = pygame.font.Font(None, 60)  # 定义输入的字体和大小

color = 200, 80, 60
width = 4
x = 300
y = 250
radius = 200
position = x - radius, y - radius, radius * 2, radius * 2  # 定义变量

pieces1 = False
pieces2 = False
pieces3 = False
pieces4 = False  # 定义布尔类型变量

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()  # 关闭窗口；优先处理事件；退出改程序
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()  # 键盘操作；
            elif event.key == pygame.K_1:
                pieces1 = True
            elif event.key == pygame.K_2:
                pieces2 = True
            elif event.key == pygame.K_3:
                pieces3 = True
            elif event.key == pygame.K_4:
                pieces4 = True

    screen.fill((0, 0, 200))

    textImg1 = myfont.render("1", True, color)
    screen.blit(textImg1, (x + radius / 2 - 20, y - radius / 2))
    textImg2 = myfont.render("2", True, color)
    screen.blit(textImg2, (x - radius / 2, y - radius / 2))
    textImg3 = myfont.render("3", True, color)
    screen.blit(textImg3, (x - radius / 2, y + radius / 2 - 20))
    textImg4 = myfont.render("4", True, color)
    screen.blit(textImg4, (x + radius / 2 - 20, y + radius / 2 - 20))
    # 画出1.2.3.4四个数字和颜色以及位置
    if pieces1:
        start_angle = math.radians(0)
        end_angle = math.radians(90)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
    if pieces2:
        start_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
    if pieces3:
        start_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
    if pieces4:
        start_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)
    if pieces1 and pieces4 and pieces3 and pieces2:
        color = 0, 255, 0
    pygame.display.update()
