import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("jobs.csv")

if df.empty:
    print("No data found in jobs.csv")
    exit()

company_count = df["Company"].value_counts()

if company_count.empty:
    print("No company data found")
    exit()

company_count.head(10).plot(kind="bar")

plt.title("Top Hiring Companies")
plt.xlabel("Company")
plt.ylabel("Number of Jobs")

plt.tight_layout()

plt.show()