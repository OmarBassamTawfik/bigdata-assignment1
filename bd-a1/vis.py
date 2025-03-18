import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


df = pd.read_csv("res_dpre.csv")

gender_count = df["Sex"].value_counts()
plt.figure(figsize=(6, 4))
gender_count.plot(kind="bar", color=["blue", "pink"])
plt.title("Passenger Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("vis-1-gender.png")
plt.close()

survival_count = df["Survived"].value_counts()
plt.figure(figsize=(6, 6))
survival_count.plot(kind="pie", autopct="%1.1f%%", colors=["red", "green"])
plt.title("Survivors vs Non-Survivors")
plt.ylabel("")  
plt.savefig("vis-2-survival.png")
plt.close()

plt.figure(figsize=(6, 4))
df["Age"].plot(kind="hist", bins=20, color="purple", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("vis-3-age.png")
plt.close()


os.system("python3 model.py")
print("Visualizations saved")
