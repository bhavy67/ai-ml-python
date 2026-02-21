# 🌊 Seaborn – Beginner Notes

Seaborn = Statistical Visualization Library
Built on Matplotlib
Cleaner and better visuals

--------------------------------------------
INSTALL
--------------------------------------------
pip install seaborn

--------------------------------------------
IMPORT
--------------------------------------------
import seaborn as sns

--------------------------------------------
COMMON PLOTS
--------------------------------------------

sns.lineplot(x="x", y="y", data=df)
sns.barplot(x="x", y="y", data=df)
sns.histplot(df["Age"])
sns.boxplot(x="Gender", y="Salary", data=df)
sns.heatmap(df.corr(), annot=True)

--------------------------------------------
WHY SEABORN?
--------------------------------------------
- Better design
- Less code
- Easy heatmaps
- Statistical plots

--------------------------------------------
INTERVIEW
--------------------------------------------

Matplotlib → Base
Seaborn → High-level wrapper