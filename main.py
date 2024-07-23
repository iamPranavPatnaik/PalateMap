import pandas as pd

# Load the CSV file
csv_file_path = r"C:\Users\prana\Downloads\foodrecipes.csv"
df = pd.read_csv(csv_file_path)

print("Columns in the Excel file:", df.columns)

# Function to search in column A and return values in columns B and C
def search_column_a(search_value):
    result = df[df['Title'] == search_value][['Ingredients', 'Instructions']]
    return result.values.tolist()

# Example search value
search_value = input()
search_result = search_column_a(search_value)

# Print each result row
for row in search_result:
    print(row[0], row[1])
