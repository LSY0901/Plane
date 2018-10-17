# -*- coding:utf-8 -*-
"""
----------------------------------------------
  File Name:   plane_sprites
  Description: 
  Author:       Mr.Liu
  date:         2018/8/27
-----------------------------------------------
   Change Activity:
                2018/8/27:
-----------------------------------------------
"""
_author_ = 'Mr.Liu'
import random
import pygame
from common_utils import *
# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT +1


class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战游戏精灵
    """
    def __init__(self, image_name, speed=1):
        """
        :param image_name: 图像的文件名
        :param speed: 精灵的移动速度
        """
        super().__init__()   # 当前类的父类不是object类   要父类初始化
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()   # 通过调用对象.get_rect()方法获得位置
        self.speed = speed

    def update(self):
        """
        精灵移动
         :return:
        """
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed
        # self.rect.x += self.speed


class Background(GameSprite):
    """
    游戏背景精灵
    """
    def __init__(self, is_alt=False):
        # 调用父类的方法实现精灵的创建
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1、调用父类方法实现
        super().update()
        # 2、判断是否移出屏幕，将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
        pass


class Enemy(GameSprite):
    """
    敌机精灵
    """
    def __init__(self):
    # 调用父类方法，创建敌机精灵，同时制定敌机图片
        super().__init__("./images/enemy1.png")
    # 指定敌机的初始化随机速度
        self.speed = random.randint(2, 3)
    # 指定敌机的初始随机位置
        self.rect.bottom = 0 # 设置垂直方向的位置
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        # 播放敌机飞行的音效文件
        play_audio("./sound/enemy3_flying.wav")

    def update(self):
        # 调用父类方法 保持垂直方向上飞行
        super().update()
        # 判断是否飞出屏幕， 如果是，需要从精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            print("敌机飞出屏幕，需要从精灵组中删除.......")
            # kill（）销毁对象  将精灵从精灵组中删除
            self.kill()
        pass


class Hero(GameSprite):
    """
    英雄精灵
    """
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.move = False
        # 3、创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄在水平方向移动
        if not self.move:
            self.rect.x += self.speed
        else:
            self.rect.y += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.bottom > SCREEN_RECT.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height
        elif self.rect.y < 0:
            self.rect.y = 0

    def fire(self):
        play_audio("./sound/bullet.wav")
        # print("发射子弹.....")
        for i in (0, 1, 2):
            # 1. 创建子弹精灵
            bullet = Bullet()
            bullet1 = Bullet()
            bullet2 = Bullet()
            # 2. 设置精灵位置，让子弹的底部等于英雄y坐标在向上一段的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet1.rect.bottom = self.rect.y - i * 20
            bullet2.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            bullet1.rect.centerx = self.rect.centerx - 40
            bullet2.rect.centerx = self.rect.centerx + 40
            # 3. 将精灵添加到精灵组
            self.bullets.add(bullet, bullet1, bullet2)



class Bullet(GameSprite):
    """
    子弹精灵
    """
    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./images/bullet2.png", -2)
        pass
    def update(self):
        # 调用父类方法，让子弹沿着垂直方向飞行
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __def__(self):
        print("子弹被销毁.......")