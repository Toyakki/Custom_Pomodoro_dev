import pygame
import pygame_gui
from button import Button
import csv
import pandas as pd
import csv

def display_questionnaire(manager):
    from main import pomodoro_timer
    width, height = 2000, 1000
    screen = pygame.display.set_mode((width, height))
    ui_manager = pygame_gui.UIManager((width, height))
    backdrop = pygame.image.load("Pomodoros/Backdrop2.png")

    # Create labels for the questions
    question1_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 20), (300, 30)),
                                                  manager=ui_manager,
                                                  text="What is the date today?")
    
    question2_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 70), (300, 30)),
                                                  manager=ui_manager,
                                                  text="Which subject did you focus on?")
    
    question3_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 180), (300, 30)),
                                                  manager=ui_manager,
                                                  text="Which p's/thms did you work on?")
    
    SUBMIT_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 300), (120, 30)),
                                                 text="Submit",
                                                 manager=ui_manager)
    
    BACK_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 300), (120, 30)),
                                                text="Back",
                                                manager=ui_manager)

    
    # Create input boxes for the questions
    date_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((60, 50), (200, 30)),
                                                              manager=ui_manager)
    math_topics_input = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((60, 100), (200, 50)),
                                                           item_list=["MAT157", "MAT247"],
                                                           manager=ui_manager,
                                                           allow_multi_select=True)  # Enable multi-selection
    problems_solved_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((60, 210), (200, 30)),
                                                              manager=ui_manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            ui_manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == SUBMIT_BUTTON:    
                    solved_dates = date_input.get_text()
                    selected_topics = math_topics_input.get_multi_selection()  # Get the selected subjects as a list
                    solved_problems = problems_solved_input.get_text()
                    responses = [solved_dates, selected_topics, solved_problems]
                    for topic in selected_topics:
                        with open (f"Pomodoros/{topic}.csv", "a", newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(responses)
                    pygame_gui.windows.UIMessageWindow(rect=pygame.Rect((width/2 - 150, height/2 - 75), (300, 150)),
                                                       html_message="<font face=arial size=4><center><b>Submitted successfully!</b></center></font>",
                                                       manager=ui_manager,
                                                       window_title="Success",
                                                       visible=True)                             
                    
                if event.ui_element == BACK_BUTTON:
                    pomodoro_timer()
                
        ui_manager.update(time_delta)
        screen.fill((255, 255, 255))
        screen.blit(backdrop, (width / 2, 0))  # Updated position for the backdrop
        ui_manager.draw_ui(screen)
        pygame.display.update()
    

    pygame.quit()