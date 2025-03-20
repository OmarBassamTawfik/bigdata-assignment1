import sys
import subprocess
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(file_path, output_file="processed_titanic.csv"):
    """
    Preprocess the Titanic dataset:
    - Handle missing values
    - Encode categorical columns
    - Normalize numerical columns
    - Save the processed dataset

    Args:
        file_path (str): Path to the input Titanic dataset.
        output_file (str): Path to save the processed dataset.
    """
    try:
        # Load the dataset
        df = pd.read_csv(file_path)
        print("\nOriginal data snapshot (first 5 rows):")
        print(df.head())

        # Check missing values before handling
        print("\nMissing values before cleaning:")
        print(df.isnull().sum())

        # Handle missing values
        if 'Age' in df.columns:
            df['Age'].fillna(df['Age'].mean(), inplace=True)
        if 'Embarked' in df.columns:
            df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
        if 'Cabin' in df.columns:
            df.drop(columns=['Cabin'], inplace=True)  # Drop 'Cabin' due to excessive missing values

        # Encode categorical columns
        if 'Sex' in df.columns:
            df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
        if 'Embarked' in df.columns:
            df['Embarked'] = df['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

        # Check missing values after handling
        print("\nMissing values after cleaning:")
        print(df.isnull().sum())

        # Identify numerical columns for normalization
        num_cols = df.select_dtypes(include=['number']).columns

        # Print numerical data before normalization
        print("\nNumerical data before normalization (first 5 rows):")
        print(df[num_cols].head())

        # Apply MinMaxScaler to normalize numerical columns
        scaler = MinMaxScaler()
        df[num_cols] = scaler.fit_transform(df[num_cols])

        # Print numerical data after normalization
        print("\nNumerical data after normalization (first 5 rows):")
        print(df[num_cols].head())

        # Save the processed dataset
        df.to_csv("res_dpre.csv", index=False)
        print(f"\nPreprocessing completed! Data saved as {"res_dpre.csv"}")
        
        # call eda.py with the processed file
        subprocess.run(["python3", "eda.py", "res_dpre.csv"])

    except Exception as e:
        print(f"Error in preprocessing: {e}")


if __name__ == "__main__":
    # ensure the user provides a dataset file path
    if len(sys.argv) < 2:
        print("usage: python3 dpre.py <input_file>")
    
    else:
        preprocess_data(sys.argv[1])  # call the function with the dataset path
        