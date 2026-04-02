import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Unemployment in India.csv")

print(df.head())

df.columns = df.columns.str.strip()
df = df[["Region", "Date", "Estimated Unemployment Rate (%)"]]
df.columns = ["Region", "Date", "Unemployment_Rate"]
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.dropna()

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Unemployment_Rate"])
plt.title("Unemployment Rate Over Time (India)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.show()

covid = df[df["Date"].dt.year == 2020]

plt.figure(figsize=(10,5))
plt.plot(covid["Date"], covid["Unemployment_Rate"])
plt.title("Covid-19 Impact on Unemployment (2020)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.show()


regions = df["Region"].unique()

for region in regions[:5]:   # first 5 regions (clean output)
    temp = df[df["Region"] == region]
    plt.plot(temp["Date"], temp["Unemployment_Rate"], label=region)

plt.legend()
plt.title("Unemployment by Region")
plt.xticks(rotation=45)
plt.show()

print("\nConclusion:")
print("1. Sharp increase in unemployment during 2020 (Covid period).")
print("2. Gradual recovery observed after lockdown.")
print("3. Different regions show different unemployment patterns.")
