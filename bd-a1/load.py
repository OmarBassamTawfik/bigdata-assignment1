import sys
import pandas as pd
import os
import subprocess


# check if the dataset path is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python3 load.py <dataset-path>")
    sys.exit(1)


# get the dataset path from the command-line argument
dataset_path = sys.argv[1]


# validate the dataset path
if not os.path.isfile(dataset_path):
    print(f"Error: The file '{dataset_path}' does not exist.")
    sys.exit(1)


# read the dataset
try:
    df = pd.read_csv(dataset_path)
    print(f"Dataset loaded successfully from {dataset_path}")

except Exception as e:
    print(f"Error loading dataset: {e}")
    sys.exit(1)


# save the dataset to a new file
output_path = "/home/doc-bd-a1/processed_data.csv"
try:
    df.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")

except Exception as e:
    print(f"Error saving dataset: {e}")
    sys.exit(1)


# invoke the next script (dpre.py)
try:
    subprocess.run(["python3", "dpre.py", output_path], check=True)
    print("dpre.py executed successfully")

except subprocess.CalledProcessError as e:
    print(f"Error executing dpre.py: {e}")
    sys.exit(1)

except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)