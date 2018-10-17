import pygame
pygame.init()


def play_background_music():
    """播放背景音乐"""

    # 1.初始化音效对象
    pygame.mixer.init()
    # 2.载入音效文件
    pygame.mixer.music.load("./sound/game_music.ogg")
    pygame.mixer.music.set_volume(0.5)  # 设置播放的音量大小，值为0-1之间的值
    pygame.mixer.music.play(-1)  # -1:表示循环播放


def play_audio(file_name):
    """播放指定音效文件"""
    sound_audio = pygame.mixer.Sound(file_name)
    sound_audio.set_volume(0.5)
    sound_audio.play()