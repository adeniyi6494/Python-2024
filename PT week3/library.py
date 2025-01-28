# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
# Replace 'your_dataset.csv' with your actual dataset file name
try:
    dataset = pd.read_csv('your_dataset.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Dataset file not found.")
    exit()

# Step 2: Data exploration
print("\n--- Dataset Overview ---")
print(dataset.head())  # Display the first 5 rows
print("\n--- Dataset Info ---")
print(dataset.info())  # Display column data types and non-null counts
print("\n--- Dataset Summary Statistics ---")
print(dataset.describe())  # Display basic statistics

# Step 3: Basic data analysis
# Example: Group data by a specific column (e.g., 'Category') and calculate total sales
if 'Category' in dataset.columns and 'Sales' in dataset.columns:
    category_sales = dataset.groupby('Category')['Sales'].sum()
    print("\n--- Total Sales by Category ---")
    print(category_sales)

# Step 4: Visualizations
# Example 1: Bar chart of total sales by category
if 'Category' in dataset.columns and 'Sales' in dataset.columns:
    category_sales.plot(kind='bar', color='skyblue', figsize=(8, 5))
    plt.title('Total Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example 2: Histogram of a numerical column (e.g., 'Sales')
if 'Sales' in dataset.columns:
    dataset['Sales'].plot(kind='hist', bins=10, color='orange', edgecolor='black', figsize=(8, 5))
    plt.title('Distribution of Sales')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Example 3: Line plot of sales over time (if a 'Date' column exists)
if 'Date' in dataset.columns and 'Sales' in dataset.columns:
    dataset['Date'] = pd.to_datetime(dataset['Date'])  # Convert to datetime format
    sales_over_time = dataset.groupby('Date')['Sales'].sum()
    sales_over_time.plot(kind='line', figsize=(10, 6), marker='o', color='green')
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.grid()
    plt.tight_layout()
    plt.show()

# Step 5: Findings/Observations
# Print observations
print("\n--- Observations ---")
if 'Category' in dataset.columns and 'Sales' in dataset.columns:
    print(f"The category with the highest total sales is: {category_sales.idxmax()} with sales of {category_sales.max():.2f}.")
if 'Sales' in dataset.columns:
    print(f"The average sales amount is: {dataset['Sales'].mean():.2f}.")
