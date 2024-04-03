## Keypress library
import pyautogui
import csv

## Converting .xlsx (Excel) files into .csv 
import pandas as pd

xlsx_file = "example.xlsx"
inp_file = "example.csv"
out_file_pattern = "modified_example.csv"

read_file = pd.read_excel (xlsx_file)

# Write the dataframe object into csv file 
read_file.to_csv (inp_file,
                  index = None,
                  header=True)

# Normalize data into single value columns in csv file
with open(inp_file, 'r', newline='') as f:

    reader = csv.reader(xlsx_file, quoting=csv.QUOTE_NONE)
    #next(reader, None) # skips header

    with open(out_file_pattern, 'w', newline='') as out_f:
        writer = csv.writer(out_f)

        for row in f:
            line = row.split(sep = ',')     #splits current row into an array, can be used to modify or compare data
            writer.writerow(line)           #writes back the array into the row


# Read the Data -- 
    # Different styles (Data can start differently, what are some common patterns?) -> Different functions?
# pyautogui/similar software to input keystrokes and keypresses