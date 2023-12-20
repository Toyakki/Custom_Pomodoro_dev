
import pandas as pd

# Read the responses.csv file into a data frame
df = pd.read_csv("Pomodoros/MAT157.csv")

# Rename the columns with appropriate headers
df.columns = ["Date", "Topics", "Solved P/Thm"]

# Save the DataFrame back to the responses.csv file
df.to_csv("Pomodoros/MAT157.csv", index=False)

print(df.head())