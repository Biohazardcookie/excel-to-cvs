## Keypress library
import pyautogui
import csv

## Converting .xlsx (Excel) files into .csv 
import pandas as pd

"""
def read_func():
    filename = input('Enter the csv ...')
    if filename:
        with open(filename) as csvfile:
"""

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
            line = row.split()
            writer.writerow(line)

# Get Excel File
# Convert to CSV
    # How to normalize it?
        # Make a counter -> count number of commas? -> use that to get each element of the row -> write into new csv file (which becomes the modified version)
        # You can access string characters like an array
        # Make a vector -> get the line -> loop(use the split function)
        #                                   -> write to new file -> nextline when char is comma
# Read the Data -- 
    # Different styles (Data can start differently, what are some common patterns?) -> Different functions?
# pyautogui to input keystrokes and keypresses

"""
writerows(rows)

for row in rows:
    writerow(row)
"""