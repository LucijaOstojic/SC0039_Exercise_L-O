# Import the csv module

import csv

# Define a function which makes the loc_start and loc_end variables
#  and calculates a new variable seq_length

def new_column(row):
    loc_start = int(row[2])
    loc_end = int(row[3])
    seq_length = loc_end - loc_start
    return int(seq_length)

# Open the input file in reading mode with csv.reader
#  and define that the rows in the file belong to a 'list' class 

with open('brca_cnvs_tcga-1.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    rows = list(reader)

# To add a header for the new column, define a variable 'title' which
#  specifies that it is the first row of the file, and add a new header
#  called seq_length

title = rows[0]
title.append("seq_length")

# For all other rows, use a for loop which calls the previously 
#  defined new_column function and adds the calculated values to the
#  new column with row.append command 

for row in rows[1:]:
    seq_length = new_column(row)
    row.append(seq_length)

# Create an output file in writing mode with csv.writer and write all
#  rows with writer.writerows command

with open('brca_cnvs_tcga-1_output.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file) 
    writer.writerows(rows)
