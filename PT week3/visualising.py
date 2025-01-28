# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
def load_and_explore_dataset(filename):
    """
    Load a CSV dataset, handle errors, and inspect the data.
    """
    try:
        # Load the dataset
        df = pd.read_csv(filename)
        print("\nDataset Loaded Successfully!\n")

        # Display first few rows
        print("First 5 rows of the dataset:")
        print(df.head())

        # Display data info
        print("\nDataset Information:")
        print(df.info())

        # Check for missing values
        print("\nMissing Values in Dataset:")
        print(df.isnull().sum())

        # Clean dataset by dropping rows with missing values
        df_cleaned = df.dropna()
        print("\nMissing values removed (if any).")

        return df_cleaned
    
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Task 2: Basic Data Analysis
def basic_data_analysis(df):
    """
    Perform basic statistical analysis on the dataset.
    """
    print("\nBasic Statistics:")
    print(df.describe())  # Summary statistics

    # Perform groupings (Example: Group by species and compute mean petal length)
    if "species" in df.columns:
        print("\nAverage values per species:")
        print(df.groupby("species").mean())

# Task 3: Data Visualization
def visualize_data(df):
    """
    Create various visualizations from the dataset.
    """
    # Set plot style
    sns.set_style("whitegrid")

    # Line Chart (Example: Sepal Length over index)
    plt.figure(figsize=(8, 5))
    plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="b")
    plt.xlabel("Index")
    plt.ylabel("Sepal Length")
    plt.title("Line Chart: Sepal Length Trend")
    plt.legend()
    plt.show()

    # Bar Chart (Example: Average Sepal Length by Species)
    if "species" in df.columns:
        plt.figure(figsize=(8, 5))
        df.groupby("species")["sepal_length"].mean().plot(kind="bar", color=["blue", "green", "red"])
        plt.xlabel("Species")
        plt.ylabel("Average Sepal Length")
        plt.title("Bar Chart: Sepal Length by Species")
        plt.xticks(rotation=45)
        plt.show()

    # Histogram (Example: Sepal Length Distribution)
    plt.figure(figsize=(8, 5))
    plt.hist(df["sepal_length"], bins=10, color="purple", alpha=0.7)
    plt.xlabel("Sepal Length")
    plt.ylabel("Frequency")
    plt.title("Histogram: Sepal Length Distribution")
    plt.show()

    # Scatter Plot (Example: Sepal Length vs. Petal Length)
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df["sepal_length"], y=df["petal_length"], hue=df["species"], palette="Set1")
    plt.xlabel("Sepal Length")
    plt.ylabel("Petal Length")
    plt.title("Scatter Plot: Sepal Length vs Petal Length")
    plt.legend()
    plt.show()

# Main Execution
if __name__ == "__main__":
    # Load the dataset
    filename = "iris.csv"  # Change this to your dataset file
    df = load_and_explore_dataset(filename)

    if df is not None:
        # Perform basic analysis
        basic_data_analysis(df)

        # Visualize the data
        visualize_data(df)

        print("\nAnalysis Completed! 🎉")
