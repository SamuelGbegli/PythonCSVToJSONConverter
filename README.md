# Python CSV to JSON converter

## Overview

This is a Python script designed to take a CSV file and output a JSON file with the item's contents.

## How the script works

Upon running the script, you will be asked to enter the path to a CSV file to the console. If the file is valid, data is parsed and you will be asked to enter the name you want the resulting JSON file to be saved as.

JSON files will be saved to the location of the script.

Files are valid if:
- Their name ends with .csv
- There is at least 1 line in the file

## CSV formatting

Items separated with a comma (,) are treated as separate properties of the row read. Items with semicolons (;) are treated as part of an array.

## Headers in the file

Each item needs a header to act as a JSON property name.

- If there is only one line in the open file, you will be asked to define headers for each value
- If there are two or more lines in the file, you will be asked to either manually name headers or use the first line as headers
- If you choose to use the first row for headers, you will be asked to name headers for each missing value if:
  - There are empty values in the first row 
  - Any row below the first row is longer
