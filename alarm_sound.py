import pygame

def init_sound():
    pygame.mixer.init()

def start_alarm_sound():
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play(-1)  

def stop_alarm_sound():
    pygame.mixer.music.stop()
