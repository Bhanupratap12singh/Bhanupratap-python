# Step 1: City-wise Average Temperature Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel(r"C:\Users\Bhanupratap singh\Downloads\India_Weather_Data.xlsx")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Group by city to calculate average temperature
city_temp = df.groupby("City")["Temperature (°C)"].mean().sort_values(ascending=False)

# Plot city-wise average temperature
plt.figure(figsize=(12,6))
sns.barplot(x=city_temp.index, y=city_temp.values, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Average Temperature by City")
plt.ylabel("Average Temperature (°C)")
plt.xlabel("City")
plt.tight_layout()
plt.show()

