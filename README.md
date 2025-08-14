# Data Import Techniques Assignment

## Problem Description

In this assignment, you will practice importing data from various file formats using Python's pandas library. You will write functions to read data from CSV, JSON, and Excel files, demonstrating your ability to handle different data sources. This is a fundamental skill for any data analyst or engineer.

## Learning Objectives

By completing this assignment, you will learn:
- How to read data from a CSV file into a pandas DataFrame
- How to read data from a JSON file into a pandas DataFrame
- How to read data from an Excel file into a pandas DataFrame
- How to handle common issues when importing data, such as specifying delimiters and sheet names

## Setup Instructions

1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Make sure you have the following packages installed:
    -   pandas (>=1.3.0)
    -   openpyxl (>=3.0.0)

## Instructions

1.  Open the `assignment.py` file.
2.  You will find three function definitions: `import_csv`, `import_json`, and `import_excel`.
3.  Your tasks are to:
    *   **Task 1**: Implement the `import_csv` function to read a CSV file into a pandas DataFrame.
    *   **Task 2**: Implement the `import_json` function to read a JSON file into a pandas DataFrame.
    *   **Task 3**: Implement the `import_excel` function to read a specific sheet from an Excel file into a pandas DataFrame.

## Hints

*   Use `pd.read_csv()` for Task 1.
*   Use `pd.read_json()` for Task 2. You might need to set the `orient` parameter depending on the JSON structure.
*   Use `pd.read_excel()` for Task 3. Remember to specify the `sheet_name`.

## Testing Your Solution

Run the test file to verify your implementation:

```bash
python test.py
```

The tests will check:

-   That each function returns a pandas DataFrame
-   That the DataFrames have the expected shape and content
-   That the functions can handle different file formats correctly

## Expected Output

Each function should return a pandas DataFrame containing the data from the respective file.

## Sample Data Format

### CSV File (`data.csv`):

```csv
name,age,city
Alice,30,New York
Bob,25,Los Angeles
```

### JSON File (`data.json`):

```json
[
  {"name": "Charlie", "age": 35, "city": "Chicago"},
  {"name": "David", "age": 40, "city": "Houston"}
]
```

### Excel File (`data.xlsx`, Sheet: `Sheet1`):

| name  | age | city      |
| :---- | --: | :-------- |
| Eve   | 28  | Phoenix   |
| Frank | 45  | Miami     |

## Troubleshooting

### Common Errors

-   `FileNotFoundError`: Make sure the file paths in the test file are correct.
-   `ValueError`: Check the parameters you are passing to the pandas read functions (e.g., `delimiter`, `orient`, `sheet_name`).
-   `ModuleNotFoundError: No module named 'openpyxl'`: Ensure you have installed the `openpyxl` library for reading Excel files.

## Further Exploration (Optional)

*   How would you read a CSV file with a different delimiter (e.g., a tab-separated file)?
*   Explore reading data from other sources, such as an HTML table or a SQL database.
*   Can you write a single function that can handle multiple file formats based on the file extension?
*   Look into the different parameters available in the pandas read functions to handle more complex cases (e.g., skipping rows, parsing dates).

## Resources

-   [Pandas I/O tools (reading and writing data)](https://pandas.pydata.org/docs/user_guide/io.html)
-   [Reading CSV files with pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
-   [Reading JSON files with pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html)
-   [Reading Excel files with pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
