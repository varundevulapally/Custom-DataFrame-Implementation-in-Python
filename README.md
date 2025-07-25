# Custom-DataFrame-Implementation-in-Python
DataFrame Implementation

This project implements a simplified DataFrame class in Python for handling structured data in a tabular format, similar to the functionality provided by libraries like Pandas. The DataFrame class provides methods to read data from CSV files, manipulate columns, and display data.


---

Project Files

1. dataframe.py
Contains the DataFrame class implementation with methods for reading, processing, and manipulating data.


2. sachin.csv
A sample data file containing records of cricket matches for testing purposes.


3. main.py
Demonstrates the usage of the DataFrame class, including reading the file, displaying rows, and calculating strike rates.




---

Features

Read CSV: Load data from a file with optional custom column names and delimiters.

Display Data: Show the first n rows (head) or the last n rows (tail) of the data.

Access Columns: Fetch specific columns or subsets of columns.

Add Columns: Create new columns based on calculated or provided values.

Error Handling: Handles file not found and column mismatch errors gracefully.



---

How to Use

1. File Structure

Save the provided sachin.txt file in the same directory as your code.

Ensure the dataframe.py script contains the implementation of the DataFrame class.


2. Run the Program

1. Open a terminal and navigate to the directory containing the files.


2. Run the program:

python main.py




---

Input File Format

The input file (sachin.csv) should contain tabular data with rows separated by newlines and columns separated by a delimiter (default: space).

Example (sachin.csv)

22/2/1992 ENG 35 44
01/3/1992 AUS 11 19
04/3/1992 PAK 54 62
07/3/1992 ZIM 81 77


---

Example Output

First 5 Rows

Date         | Country      | Runs       | Balls
-------------------------------------------------
22/2/1992    | ENG          |          35 |          44
01/3/1992    | AUS          |          11 |          19
04/3/1992    | PAK          |          54 |          62
07/3/1992    | ZIM          |          81 |          77
10/3/1992    | WI           |           4 |          11

Runs and Balls

Runs        Balls
------------------
        35         44
        11         19
        54         62
        81         77
         4         11

Updated DataFrame (First 10 Rows)

Date         | Country      | Runs       | Balls      | Strike Rate
--------------------------------------------------------------------
22/2/1992    | ENG          |          35 |          44 |       79.55
01/3/1992    | AUS          |          11 |          19 |       57.89
04/3/1992    | PAK          |          54 |          62 |       87.10
07/3/1992    | ZIM          |          81 |          77 |      105.19
10/3/1992    | WI           |           4 |          11 |       36.36


---

Dependencies

Python 3.x

CSV Module: Standard Python library for CSV file handling.



---

Methods in DataFrame Class

1. read_csv(filename, names=None, delimiter=",")
Reads data from a CSV file. Optionally accepts column names and delimiter.


2. head(rows=5)
Displays the first n rows of the data.


3. tail(rows=5)
Displays the last n rows of the data.


4. getColumn(column)
Retrieves the data of a specific column.


5. getColumns(columns)
Retrieves multiple columns as a dictionary.


6. addColumn(column_name, values)
Adds a new column to the DataFrame.


