# -*- coding:utf-8 -*-
"""
----------------------------------------------
  File Name:   AI_02_Rect
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

# 定义对象
hero_rect = pygame.Rect(0, 0, 100, 200)


# 输出原点
print("原点坐标（%d, %d）" % (hero_rect.x, hero_rect.y))
# 输出大小
print("大小:%d, %d" % (hero_rect.width, hero_rect.height))
# print("%d, %d" % hero_rect.size)  # size 封装了宽高属性


