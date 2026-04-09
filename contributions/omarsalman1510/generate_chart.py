import pandas as pd
import matplotlib.pyplot as plt


data = {
    "city": ["Amman", "Irbid", "Zarqa", "Aqaba", "Salt", "Madaba"],
    "revenue": [125000, 72000, 68000, 54000, 49000, 43000]
}

df = pd.DataFrame(data)

df = df.sort_values("revenue", ascending=False)

top_city = df.iloc[0]["city"]
top_value = df.iloc[0]["revenue"]



fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(df["city"], df["revenue"])

ax.set_title("Amman Dominates Revenue Across Jordanian Cities")

ax.set_xlabel("City")
ax.set_ylabel("Revenue (JOD)")

ax.annotate(
    f"Top: {top_city}\n{top_value:,} JOD",
    xy=(0, top_value),
    xytext=(10, 15),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->")
)

plt.xticks(rotation=45)
plt.tight_layout()

fig.savefig("chart.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("chart.png created successfully.")