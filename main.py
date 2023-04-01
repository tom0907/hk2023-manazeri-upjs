import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl

def print_hi():
    # Set the path to the input and output files
    input_file = 'Data/dc_evt_modified2.csv'
    output_file = 'output.txt'

    # Specify the column number to count (starting from 0)
    column_number = 16

    # Define a dictionary to store the counts of each element
    count_dict = {}

    # Open the input CSV file
    with open(input_file, 'r') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Get the value of the specified column for the current row
            column_value = row[column_number]
            # If the value is not in the count dictionary, add it with a count of 1
            if column_value not in count_dict:
                count_dict[column_value] = 1
            # If the value is already in the count dictionary, increment its count
            else:
                count_dict[column_value] += 1

    # get the items from the count_dict as a list of tuples

    print(count_dict.items())
    items = count_dict.items()

    # unpack the tuples into two separate lists x and y
    x, y = zip(*items)

    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()

    plt.pie(y)
    plt.show()

    # Open the output file
    with open(output_file, 'w') as output_file:
        # Iterate over each element in the count dictionary
        for element, count in count_dict.items():
            # Write the element and its count to the output file
            output_file.write(f'{element}: {count}\n')

if __name__ == '__main__':
    print_hi()