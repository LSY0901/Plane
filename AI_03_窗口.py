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

pygame.init()

# 创建游戏主窗口   默认大小和屏幕匹配
screen = pygame.display.set_mode((480, 700))  # 参数为元组

# 1、加载图像
bg = pygame.image.load("./images/background.png")
# 2、调用屏幕对象  blit（对象，位置）
screen.blit(bg, (0, 0))

# 3、屏幕更新
pygame.display.update()




while True:
    pass

pygame.quit()


