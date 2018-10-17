# -*- coding:utf-8 -*-
"""
----------------------------------------------
  File Name:   AI_03_窗口
  Description: 
  Author:       Mr.Liu
  date:         2018/8/27
-----------------------------------------------
   Change Activity:
                2018/8/27:
-----------------------------------------------
"""
_author_ = 'Mr.Liu'
import pygame

from plane_sprites import *

pygame.init()

# 创建游戏主窗口   默认大小和屏幕匹配
screen = pygame.display.set_mode((480, 700))  # 参数为元组

# 背景
# 1、加载图像
bg = pygame.image.load("./images/background.png")
# 2、调用屏幕对象  blit（对象，位置）
screen.blit(bg, (0, 0))
# 3、屏幕更新
pygame.display.update()


# 英雄
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 300))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义rect记录飞机的初始位置，150,300表示英雄飞机的初始位置，102,126表示英雄飞机的宽高
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵，指定敌机精灵图片
enemy = GameSprite("./images/enemy1.png")
# 指定敌机图片和速度，第二个参数2表示敌机精灵的速度
enemy1 = GameSprite("./images/enemy1.png", 2)
# enemy2 = GameSprite("./images/enemy1.png", 3)
# enemy3 = GameSprite("./images/enemy1.png", 4)
# enemy4 = GameSprite("./images/enemy1.png", 5)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环 ===>意味着游戏正式开始
while True:
    # 可以指定循环体内部代码执行的频率
    clock.tick(60)

    # # 捕获事件
    # event_list = pygame.event.get()
    # # 判断有无元素
    # if len(event_list) > 0:
    #     print(event_list)
    # 监听事件
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            print("游戏退出..........")
            pygame.quit()
            exit()
    #  修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    # if hero_rect.y <= 0:
    if hero_rect.y <= 0 - hero_rect.height:
        hero_rect.y  = 700
    # 调用blit方法绘制图像
    # 重绘背景(覆盖之前图像)，解决飞机残影问题
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)


    # 让精灵组调用两个方法
    # update - 让组中所有精灵更新位置
    enemy_group.update()
    # draw - 将精灵组中所有精灵绘制到屏幕上
    enemy_group.draw(screen)


    # 调用upate方法更新显示
    pygame.display.update()
    pass

pygame.quit()


