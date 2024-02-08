# Adv-Python-Lab
The AdvPythonLab repository is a comprehensive collection of advanced Python programming lab exercises and projects. It serves as a valuable resource for individuals seeking to enhance their Python programming skills through hands-on practice and exploration of advanced concepts.

# Lab 1 - Product Review from text file

## Project Overview
In this lab, we simulate a scenario where we analyze customer feedback data stored in multiple text files. The Python script provided performs the following operations:

1. Reads the contents of all text files in a specified directory.
2. Extracts relevant information from each review, including Customer ID, Product ID, Review date, Review rating, and Review text.
3. Calculates the average review rating for each product and stores it in a dictionary.
4. Determines the top 3 products with the highest average review ratings.
5. Creates a "summary.txt" file with key statistics and information.

## Python Script - `analyze_reviews.py`

The main Python script, `analyze_reviews.py`, is responsible for processing the customer feedback data. It performs the following steps:

1. **Reading Files:** Reads all text files in the specified directory.

2. **Extracting Information:** Extracts Customer ID, Product ID, Review date, Review rating, and Review text from each review.

3. **Calculating Average Ratings:** Calculates the average review rating for each product and stores it in a dictionary.

4. **Determining Top Products:** Identifies the top 3 products with the highest average review ratings.

5. **Writing Summary File:** Creates a "summary.txt" file with key statistics and information.

6. **Robust Error Handling:** Implements robust error handling to deal with potential issues during file processing.

## Usage

To use the script, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/AdvPythonLab.git
    cd AdvPythonLab
    ```

2. Execute the Python script with the desired directory path:

    ```bash
    python analyze_reviews.py /path/to/your/directory
    ```

3. Check the generated "summary.txt" file for the results.

## Summary.txt Example

