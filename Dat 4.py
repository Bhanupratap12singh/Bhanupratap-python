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

# Step 2: Seasonal Weather Trends Analysis
# Group by Season and calculate average for each metric
seasonal_data = df.groupby("Season")[["Temperature (°C)", "Humidity (%)", "Rainfall (mm)"]].mean()

# Plot seasonal temperature trends
plt.figure(figsize=(10,5))
sns.barplot(x=seasonal_data.index, y=seasonal_data["Temperature (°C)"], palette="YlOrRd")
plt.title("Average Temperature by Season")
plt.xlabel("Season")
plt.ylabel("Temperature (°C)")
plt.show()

# Plot seasonal humidity trends
plt.figure(figsize=(10,5))
sns.barplot(x=seasonal_data.index, y=seasonal_data["Humidity (%)"], palette="Blues")
plt.title("Average Humidity by Season")
plt.xlabel("Season")
plt.ylabel("Humidity (%)")
plt.show()

# Plot seasonal rainfall trends
plt.figure(figsize=(10,5))
sns.barplot(x=seasonal_data.index, y=seasonal_data["Rainfall (mm)"], palette="Greens")
plt.title("Average Rainfall by Season")
plt.xlabel("Season")
plt.ylabel("Rainfall (mm)")
plt.show()

# Step 3: Weather Condition Distribution
# Count the occurrences of each weather condition
condition_counts = df["Weather Condition"].value_counts()

# Plot weather condition distribution
plt.figure(figsize=(10,6))
sns.barplot(x=condition_counts.index, y=condition_counts.values, palette="Set2")
plt.xticks(rotation=45)
plt.title("Distribution of Weather Conditions Across Cities")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.show()

# Step 4: Rainfall vs Temperature Relationship
# Scatter plot to show correlation between rainfall and temperature
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="Rainfall (mm)", y="Temperature (°C)", hue="City", palette="tab10", alpha=0.7)
plt.title("Rainfall vs Temperature Across Cities")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Temperature (°C)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


