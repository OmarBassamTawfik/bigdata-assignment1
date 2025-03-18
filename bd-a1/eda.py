import pandas as pd
import os


df = pd.read_csv("res_dpre.csv") 

total_passengers = len(df)
with open("eda-in-1.txt", "w") as f: 
  f.write(f"Total Passengers: {total_passengers}\n")  

gender_count = df["Sex"].value_counts()
with open("eda-in-2.txt", "w") as f: 
    f.write(f"Passengers by gender:\n")
    f.write(gender_count.to_string()+"\n")

survival_count = df["Survived"].value_counts()
with open("eda-in-3.txt", "w") as f: 
    f.write(f"Survivors vs Non-Survivors:\n")
    f.write(survival_count.to_string()+"\n")

class_count = df["Pclass"].value_counts()
with open("eda-in-4.txt", "w") as f:
    f.write("Passengers by class:\n")
    f.write(class_count.to_string() + "\n")

survival_by_class = df.groupby("Pclass")["Survived"].mean().round(2)
with open("eda-in-5.txt", "w") as f:
    f.write("Survival Rate by Class:\n")
    f.write(survival_by_class.to_string() + "\n")

print("EDA insights saved")
os.system("python3 vis.py")
