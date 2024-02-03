import pygame
import pygame_gui
from button import Button
import csv
import pandas as pd
import csv
import datetime

def display_questionnaire(manager):
    from main import pomodoro_timer
    width, height = 2000, 1000
    screen = pygame.display.set_mode((width, height))
    ui_manager = pygame_gui.UIManager((width, height))
    backdrop = pygame.image.load("Custom_Pomodoro_dev/Pomodoros-copy/Backdrop2.png")

    # Create labels for the questions
    question1_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 20), (300, 30)),
                                                  manager=ui_manager,
                                                  text="What is the date today?")
    
    question2_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 70), (300, 30)),
                                                  manager=ui_manager,
                                                  text="Which subject did you focus on?")
    
    question3_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 180), (300, 30)),
                                                  manager=ui_manager,
                                                  text="Which theorems did you work on? (From Lawrence/ Eckwart notes)")
    
    question4_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 230), (300, 30)),
                                                  manager=ui_manager,
                                                  text="Which problems did you work on? (textbook)")
    
    question5_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 280), (300, 30)),
                                                    manager=ui_manager,
                                                    text="Questions to revisit?")
    
    SUBMIT_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 350), (120, 30)),
                                                 text="Submit",
                                                 manager=ui_manager)
    
    BACK_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 350), (120, 30)),
                                                text="Back",
                                                manager=ui_manager)


    
    # Create input boxes for the questions
    math_subjects_input = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((60, 100), (200, 80)),
                                                           item_list=["Calc", "LinArg", "CSC240"],
                                                           manager=ui_manager,
                                                           allow_multi_select=True)  # Enable multi-selection
    theorems_solved_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((60, 210), (200, 30)),
                                                              manager=ui_manager)

    problems_solved_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((60, 260), (200, 30)),
                                                                manager=ui_manager)

    revisiting_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((60, 310), (200, 30)),
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
                    solved_dates = datetime.datetime.now().strftime("%c")
                    selected_subjects = math_subjects_input.get_multi_selection()  # Get the selected subjects as a list
                    solved_theorems = theorems_solved_input.get_text()
                    solved_problems = problems_solved_input.get_text()
                    revisiting = revisiting_input.get_text()
                    responses = [solved_dates, solved_theorems, solved_problems, revisiting]
                    for topic in selected_subjects:
                        with open (f"Custom_Pomodoro_dev/Data/{topic}.csv", "a", newline='') as file:
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