## Project Title: Automatic Math Problem-Solving Tracking System with Pomodoro Timer

### Description:
This project is an automatic problem-solving tracking system with a 90-10 min Pomodoro timer, developed using Python and Pygame GUI. The system has the following features:
1. **Pomodoro Timer**: A timer that runs for 90 minutes of work and 10 minutes of short break and 20 minutes of long break.
2. **Questionnaire**: After each 90-minute study session (or if the countdown reaches at 0), a questionnaire window will prompt the user to select and type in the following properties:
    - Date I studied.
    - Subject I focused on during the session with multi-selection features.
    - Number of problems/theorems solved.
3. **Data Recording**: The responses to the questionnaire will be recorded in each CSV file titled with the subject name.

### Tech Stacks:
- **Python**: Programming language used for the backend and logic implementation.
- **Pygame GUI**: Used for building the graphical user interface.

### Step-by-Step Guide:
1. **Project Setup**: Prepare your environment (virtual environment is recommended), and you can just run my main.py file.
2. **Pygame GUI Installation**: Install Pygame GUI using the following command:
   ```python
   pip install pygame_gui
   ```
3. **Backend Development**: Implement the Pomodoro timer functionality and the questionnaire logic using Python and Pygame GUI. I set 90 minutes as default, you can change the time in main.py.
4. **Data Recording**: Create the csv file by yourself, which MUST BE TITLED AS '{subject}.csv'. 
5. **Testing and Deployment**: Test the application thoroughly and deploy it for use.

By following these steps, you can customize your own pomodoro timer, subjects to study, and many more. 

The search results provided information about the Pygame GUI and its installation, which is relevant to the project's tech stack. The project's description and tech stacks have been modified accordingly.

Reference (I copied the "Button" code from here:)
https://github.com/baraltech/Pomodoro-Timer-PyGame
