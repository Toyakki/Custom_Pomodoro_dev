#main.py
import pygame
import pygame_gui
import sys
from button import Button
import csv
import os
from questionnaire_window import display_questionnaire
from datetime import date

def pomodoro_timer():

    WIDTH, HEIGHT = 2000, 1000
    clock = pygame.time.Clock()
    time_delta = clock.tick(60) / 1000.0
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    pygame.display.set_caption("Pomodoro Timer")
    
    CLOCK = pygame.time.Clock()

    BACKDROP = pygame.image.load("Custom_Pomodoro_dev/Pomodoros-copy/Backdrop.png")
    WHITE_BUTTON = pygame.image.load("Custom_Pomodoro_dev/Pomodoros-copy/button.png")

    FONT = pygame.font.Font("Custom_Pomodoro_dev/Pomodoros-copy/ArialRoundedMTBold.ttf", 120)
    timer_text = FONT.render("25:00", True, "gray")
    timer_text_rect = timer_text.get_rect(center=(WIDTH/2, HEIGHT/2-25))

    START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "START", 
                        pygame.font.Font("Custom_Pomodoro_dev/Pomodoros-copy/ArialRoundedMtBold.ttf", 20), "#808080", "#808080")
    POMODORO_BUTTON = Button(None, (WIDTH/2-150, HEIGHT/2-140), 120, 30, "Pomodoro", 
                        pygame.font.Font("Custom_Pomodoro_dev/Pomodoros-copy/ArialRoundedMtBold.ttf", 20), "#808080", "#808080")
    SHORT_BREAK_BUTTON = Button(None, (WIDTH/2, HEIGHT/2-140), 120, 30, "Short Break", 
                        pygame.font.Font("Custom_Pomodoro_dev/Pomodoros-copy/ArialRoundedMtBold.ttf", 20), "#808080", "#808080")
    LONG_BREAK_BUTTON = Button(None, (WIDTH/2+150, HEIGHT/2-140), 120, 30, "Long Break", 
                        pygame.font.Font("Custom_Pomodoro_dev/Pomodoros-copy/ArialRoundedMtBold.ttf", 20), "#808080", "#808080")
    FINISH_BUTTON = Button(None, (WIDTH/2+300, HEIGHT/2-140), 120, 30, "FINISH",
                        pygame.font.Font("Custom_Pomodoro_dev/Pomodoros-copy/ArialRoundedMtBold.ttf", 20), "#808080", "#808080")

    
    POMODORO_LENGTH = 3600  # 5400 secs / 90 mins
    SHORT_BREAK_LENGTH = 600  # 600 secs / 10 mins
    LONG_BREAK_LENGTH = 1200  # 1200 secs / 20 mins

    current_seconds = POMODORO_LENGTH
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    started = False
    
    alarm_sound = pygame.mixer.Sound("Custom_Pomodoro_dev/Pomodoros-copy/337756-Japanese_ambience_-water_trickling_from_a_pond_and_crickets_during_night_time_-traffic_noise_in_the_distance_-seamles.wav")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                    if started:
                        started = False
                    else:
                        started = True
                if POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                    current_seconds = POMODORO_LENGTH
                    started = False
                if SHORT_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                    current_seconds = SHORT_BREAK_LENGTH
                    started = False
                if LONG_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                    current_seconds = LONG_BREAK_LENGTH
                    started = False
                
                if FINISH_BUTTON.check_for_input(pygame.mouse.get_pos()):
                    display_questionnaire(manager)
                    started = False
                if started:
                    START_STOP_BUTTON.text_input = "STOP"
                    START_STOP_BUTTON.text = pygame.font.Font("Custom_Pomodoro_dev/Pomodoros-copy/ArialRoundedMtBold.ttf", 20).render(
                                            START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
                else:
                    START_STOP_BUTTON.text_input = "START"
                    START_STOP_BUTTON.text = pygame.font.Font("Custom_Pomodoro_dev/Pomodoros-copy/ArialRoundedMtBold.ttf", 20).render(
                                            START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
            if event.type == pygame.USEREVENT and started:
                current_seconds -= 1
            
            if event.type == pygame.USEREVENT and started and current_seconds == 0:
                alarm_sound.play()
                display_questionnaire(manager)
        
        
        SCREEN.fill((128, 128, 128))
        SCREEN.blit(BACKDROP, BACKDROP.get_rect(center=(WIDTH/2, HEIGHT/2)))

        START_STOP_BUTTON.update(SCREEN)
        START_STOP_BUTTON.change_color(pygame.mouse.get_pos())
        POMODORO_BUTTON.update(SCREEN)
        POMODORO_BUTTON.change_color(pygame.mouse.get_pos())
        SHORT_BREAK_BUTTON.update(SCREEN)
        SHORT_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
        LONG_BREAK_BUTTON.update(SCREEN)
        LONG_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
        FINISH_BUTTON.update(SCREEN)
        FINISH_BUTTON.change_color(pygame.mouse.get_pos())

        if current_seconds >= 0:
            display_seconds = current_seconds % 60
            display_minutes = int(current_seconds / 60) % 60
        timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "gray")
        SCREEN.blit(timer_text, timer_text_rect)

        manager.update(time_delta)
        manager.draw_ui(SCREEN)
        pygame.display.update()

def main():
    pygame.init()
    pygame.mixer.init()

    # Call the pomodoro_timer function
    pomodoro_timer()


if __name__ == "__main__":
    main()