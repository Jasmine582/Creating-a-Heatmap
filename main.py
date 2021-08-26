import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("tips.csv", "r") as csvfile:
  tips = pd.read_csv(csvfile, delimiter=",")

tips_pivoted = tips.pivot_table(
    values = "tip",
    index = ["size"],
    columns = ["time"]
  )
fig = sns.heatmap(tips_pivoted, annot=True, cmap="coolwarm")

fig.set_ylim(0, 6)

plt.xlabel("Time")
plt.ylabel("Group Size")
plt.title("Average tip Amount According to Time & Group Size")

plt.savefig("average_tip")