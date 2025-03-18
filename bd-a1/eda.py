import pandas as pd


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

print("EDA insights saved")
