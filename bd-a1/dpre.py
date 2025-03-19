import sys
import pandas as pd
import subprocess
from sklearn.preprocessing import MinMaxScaler

# function to perform data preprocessing:
#   1) handle missing values by filling them with the column mean.
#   2) nornmalize numerical columns using MinMaxScaler.
#   3) save the cleaned dataset as 'res_dpre.csv'.
#   4) pass the processed dataset to eda.py.

def preprocess_data(file_path):
    try:
        # load dataset
        df = pd.read_csv(file_path)
        print("\noriginal data snapshot (first 5 rows): ")
        print(df.head())

        # rename "2urvived" to "Survived"
        df.rename(columns={"2urvived": "Survived"}, inplace=True)

        # check missing values before handling
        print("\nmissing values before cleaning: ")
        print(df.isnull().sum())

        # handling missing values (filling with mean for simplicity)
        df.fillna(df.mean(), inplace=True)

        # check missing values after handling
        print("\nmissing values after cleaning: ")
        print(df.isnull().sum())

        # identify numerical columns for normalization
        num_cols = df.select_dtypes(include=['number']).columns

        # print numerical data before normalization
        print("\nnumerical data before normalization (first 5 rows):")
        print(df[num_cols].head())

        # apply MinMaxScaler to normalize numerical columns
        scaler = MinMaxScaler()
        df[num_cols] = scaler.fit_transform(df[num_cols])

        # print numerical data after normalization
        print("\nnumerical data after normalization (first 5 rows):")
        print(df[num_cols].head())

        # save the processed dataset
        processed_file = "res_dpre.csv"
        df.to_csv(processed_file, index=False)
        print(f"\npreprocessing completed!! data saved as {processed_file}")

        # call eda.py with the processed file
        subprocess.run(["python3", "eda.py", processed_file])

    except Exception as e:
        print(f"error in preprocessing: {e}")

if __name__ == "__main__":
    # ensure the user provides a dataset file path
    if len(sys.argv) < 2:
        print("usage: python3 dpre.py <input_file>")
    
    else:
        preprocess_data(sys.argv[1])  # call the function with the dataset path