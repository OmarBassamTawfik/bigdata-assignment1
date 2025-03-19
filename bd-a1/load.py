import sys
import subprocess

# function to load the dataset path and pass it to dpre.py
def load_data(file_path):
    print(f"dataset path received: {file_path}")

    # directly call dpre.py with the original dataset [no need to create a temp dataset]
    subprocess.run(["python3", "dpre.py", file_path])

if __name__ == "__main__":
    
    # ensure the user provides a dataset file path
    if len(sys.argv) < 2:
        print("usage: python3 load.py <dataset_path>")
    
    else:
        load_data(sys.argv[1])