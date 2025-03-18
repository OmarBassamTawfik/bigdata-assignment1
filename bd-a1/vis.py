import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


df = pd.read_csv("res_dpre.csv")

sns.set_style("whitegrid")
plt.figure(figsize=(6, 4))

sns.countplot(x="Survived", data=df, palette="viridis")
plt.xlabel("Survival Status")
plt.ylabel("Passenger Count")
plt.title("Survivors vs Non-Survivors")


plt.savefig("vis.png")
os.system("python3 model.py")
print("Visualization saved as vis.png")
