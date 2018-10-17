# -*- coding:utf-8 -*-
"""
----------------------------------------------
  File Name:   plane_main
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
import time
from plane_sprites import *
from common_utils import *

# Game Over 的背景图
game_over = pygame.image.load('./images/gameover.png')


class PlaneGame(object):
    """
    飞机大战主游戏
    """
    def __init__(self):
        # 初始化分数
        self.score = 0
        print("游戏初始化")
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，创建精灵和精灵组
        self.__create_sprites()
        # 4、设置定时器事件--创建敌机   每隔1s一架
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 发射子弹的定时器
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        # 播放背景音乐
        play_background_music()

    def start_game(self):
            print("开始游戏...")
            while True:
                # 1.设置刷新帧率
                self.clock.tick(FRAME_PER_SEC)
                # 2. 事件监听
                self.__event_handler()
                # 3. 碰撞检测
                self.__check_collide()
                # 4. 更新/绘制精灵组(背景)
                self.__update_sprites()
                # 5. 更新显示
                pygame.display.update()
                pass

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场......")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组中
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # 只要用户手指不抬起，会一直输出向右移动，指定用户手指抬起为止
            keys_pressed = pygame.key.get_pressed()
            # 判断元组中对应的按键索引值
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.move = False
                self.hero.speed = 3
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.move = False
                self.hero.speed = -3
            elif keys_pressed[pygame.K_UP]:
                self.hero.move = True
                self.hero.speed = -3
            elif keys_pressed[pygame.K_DOWN]:
                self.hero.move = True
                self.hero.speed = 3
            else:
                self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁敌机
        coll_list = pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        if len(coll_list) > 0:
            # 播放敌机坠毁的音效文件
            play_audio("./sound/use_bomb.wav")
            self.score += 1
            for coll in coll_list:
                print("子弹[%s]销毁敌机[%s]了!" % (coll, coll_list[coll]))
        # 2. 敌机撞毁英雄 True:表示敌机被销毁  返回值表示和英雄发生碰撞的敌机列表
        enymies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 3.判断列表是否有内容
        if len(enymies) > 0:
            # 让英雄牺牲
            play_audio("./sound/me_down.wav")
            self.hero.kill()
            # 结束游戏
            self.__game_over()
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        # 更新精灵组中所有的精灵对象
        self.enemy_group.update()
        # 将精灵组中所有精灵绘制到屏幕上
        self.enemy_group.draw(self.screen)
        # 更新英雄精灵组中所有精灵对象
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 更新子弹精灵组中所有精灵对象
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    def __game_over(self):
        print("游戏结束")
        # 游戏 Game Over 后显示最终得分
        font = pygame.font.Font(None, 64)
        text = font.render('Final Score: ' + str(self.score), True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx
        text_rect.centery = self.screen.get_rect().centery + 24
        self.screen.blit(game_over, (
            SCREEN_RECT.centerx - game_over.get_rect().width / 2, SCREEN_RECT.centery - game_over.get_rect().width / 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()

        # 让当前线程睡眠两秒钟
        time.sleep(2)

        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()



