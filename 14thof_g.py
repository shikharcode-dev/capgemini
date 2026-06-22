
# Pandas is a powerful, open-source data analysis and manipulation library for Python
# It provides high-performance, easy-to-use data structures and data analysis tools

# Key Features of Pandas:
# 1. DataFrame: A 2-dimensional labeled data structure with columns of potentially different types
#    - Similar to a spreadsheet or SQL table
#    - Can handle missing data elegantly
#    - Supports indexing, slicing, and subsetting of large datasets

# 2. Series: A 1-dimensional labeled array capable of holding any data type
#    - Can be thought of as a single column of a DataFrame
#    - Has both a data array and an associated array of labels (index)

# 3. Data Input/Output: Pandas can read and write data from various formats:
#    - CSV files (read_csv, to_csv)
#    - Excel files (read_excel, to_excel)
#    - SQL databases (read_sql, to_sql)
#    - JSON (read_json, to_json)
#    - HTML tables, Parquet, HDF5, and many more

# 4. Data Cleaning and Preparation:
#    - Handle missing data (dropna, fillna, interpolate)
#    - Remove duplicates (drop_duplicates)
#    - Replace values (replace)
#    - Data type conversion (astype)

# 5. Data Selection and Filtering:
#    - Select columns by name or position
#    - Filter rows based on conditions
#    - Use loc (label-based) and iloc (integer position-based) indexing

# 6. Data Transformation:
#    - Apply functions to data (apply, map, applymap)
#    - Group data and perform aggregations (groupby)
#    - Merge, join, and concatenate datasets
#    - Pivot tables and cross-tabulations

# 7. Time Series Functionality:
#    - Date range generation
#    - Frequency conversion and resampling
#    - Moving window statistics
#    - Time zone handling

# 8. Statistical Analysis:
#    - Descriptive statistics (mean, median, std, min, max)
#    - Correlation and covariance
#    - Ranking and sorting
#    - Unique value counts

# 9. Visualization Integration:
#    - Built-in plotting capabilities using matplotlib
#    - Easy integration with other visualization libraries

# Common Use Cases:
# - Data cleaning and preprocessing for machine learning
# - Exploratory data analysis (EDA)
# - Financial analysis and time series analysis
# - Business intelligence and reporting
# - Scientific computing and research

# Installation: pip install pandas
# Import: import pandas as pd 


import pandas as pd
import numpy as np

# Example 1: Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin'],
    'Salary': [70000, 80000, 75000, 90000, 85000]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Example 2: Creating a Series
ages = pd.Series([25, 30, 35, 28, 32], index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
print("\nSeries:\n", ages)

# Example 3: Reading from CSV (example - file must exist)
# df_csv = pd.read_csv('data.csv')

# Example 4: Handling missing data
df_with_missing = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, 12]
})
print("\nDataFrame with missing values:\n", df_with_missing)
print("\nFill missing values with 0:\n", df_with_missing.fillna(0))
print("\nDrop rows with missing values:\n", df_with_missing.dropna())

# Example 5: Data selection and filtering
print("\nSelect 'Name' column:\n", df['Name'])
print("\nFilter rows where Age > 30:\n", df[df['Age'] > 30])
print("\nUsing loc (label-based):\n", df.loc[0:2, ['Name', 'Age']])
print("\nUsing iloc (position-based):\n", df.iloc[0:3, 0:2])

# Example 6: Data transformation with apply
df['Salary_Bonus'] = df['Salary'].apply(lambda x: x * 1.1)
print("\nDataFrame with bonus column:\n", df)

# Example 7: GroupBy and aggregation
df_sales = pd.DataFrame({
    'Region': ['East', 'West', 'East', 'West', 'East'],
    'Product': ['A', 'B', 'A', 'B', 'C'],
    'Sales': [100, 150, 200, 120, 180]
})
print("\nGroupBy Region and sum Sales:\n", df_sales.groupby('Region')['Sales'].sum())

# Example 8: Merging DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [85, 90, 78]})
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("\nMerged DataFrame:\n", merged_df)

# Example 9: Statistical analysis
print("\nDescriptive statistics:\n", df['Salary'].describe())
print("\nMean salary:", df['Salary'].mean())
print("\nMedian age:", df['Age'].median())

# Example 10: Time series example
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
ts_data = pd.DataFrame({
    'Date': date_range,
    'Value': np.random.randint(10, 100, size=len(date_range))
})
ts_data.set_index('Date', inplace=True)
print("\nTime series data:\n", ts_data)

# Example 11: Pivot table
df_pivot = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'Product': ['A', 'B', 'A', 'B'],
    'Sales': [100, 150, 120, 180]
})
pivot = df_pivot.pivot_table(values='Sales', index='Date', columns='Product')
print("\nPivot table:\n", pivot)

# Example 12: Removing duplicates
df_duplicates = pd.DataFrame({
    'A': [1, 2, 2, 3, 4],
    'B': [5, 6, 6, 7, 8]
})
print("\nDataFrame with duplicates:\n", df_duplicates)
print("\nAfter removing duplicates:\n", df_duplicates.drop_duplicates()) 