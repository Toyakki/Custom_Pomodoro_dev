import pandas as pd
import os

subject_lst = ['Calc', 'LinArg', 'CSC240']
for topic in subject_lst:
    input_file = os.path.join("Custom_Pomodoro_dev", "Data", f"{topic}.csv")
    output_file = os.path.join("Custom_Pomodoro_dev", "Data", "revisiting.data.csv")
    # Only retrieve 'Date' and 'Revisiting' columns
    try:
        df = pd.read_csv(input_file)
        column_titles = df.columns.tolist()
        print(f"Columns in {topic}.csv: {column_titles}")
        # selected_columns = df[['Column1', 'Column2', 'Column3']]
        # df = pd.read_csv(input_file, usecols=['Date', 'Revisiting'])
        # df = df.dropna(subset=['Revisiting'])
        # df['Labels'] = topic
        # df.to_csv(output_file, mode='a', header=False, index=False)
    except ValueError:
        print("Add the 'Revisiting' column to the csv file")
    