# 📊 PANDAS – COMPLETE CRISP NOTES
Beginner → Data Science → Interview Ready

===========================================================
1️⃣ WHAT IS PANDAS?
===========================================================

Pandas = Python library for data manipulation & analysis.

Used for:
- Reading CSV/Excel files
- Cleaning data
- Filtering & transforming data
- Grouping & aggregation
- Preparing data for ML

Think:
NumPy = Math Engine
Pandas = Data Handling Engine

===========================================================
2️⃣ INSTALL & IMPORT
===========================================================

pip install pandas

import pandas as pd

===========================================================
3️⃣ SERIES (1D DATA STRUCTURE)
===========================================================

Series = 1D labeled array

s = pd.Series([10,20,30])

With custom index:

s = pd.Series([10,20,30], index=["a","b","c"])

Access:

s["a"]
s[0]

Important:
Series = values + index

Useful:

s.head()
s.tail()
s.value_counts()
s.unique()
s.isnull()

===========================================================
4️⃣ DATAFRAME (2D STRUCTURE)
===========================================================

DataFrame = Table (rows + columns)

Create manually:

df = pd.DataFrame({
    "Name": ["A","B"],
    "Age": [20,25]
})

From list:

df = pd.DataFrame([[1,2],[3,4]], columns=["A","B"])

===========================================================
5️⃣ READING DATA
===========================================================

pd.read_csv("file.csv")
pd.read_excel("file.xlsx")

Always inspect after loading.

===========================================================
6️⃣ BASIC INSPECTION (VERY IMPORTANT)
===========================================================

df.head()        → first 5 rows
df.tail()        → last 5 rows
df.sample(5)     → random rows
df.shape         → (rows, columns)
df.size          → total values
df.columns       → column names
df.index         → row labels
df.info()        → datatypes + null count
df.describe()    → summary stats (mean, min, max)

Interview:
info() = structure
describe() = statistics

===========================================================
7️⃣ SELECTING DATA
===========================================================

Select column:

df["Age"]
df[["Name","Age"]]

Row by label:

df.loc[0]

Row by position:

df.iloc[0]

Key Difference:
loc → label-based
iloc → index-based

===========================================================
8️⃣ FILTERING DATA
===========================================================

Single condition:

df[df["Age"] > 20]

Multiple conditions:

df[(df["Age"] > 20) & (df["Age"] < 30)]

Operators:
& → AND
| → OR
~ → NOT

===========================================================
9️⃣ ADDING & MODIFYING
===========================================================

Add new column:

df["Salary"] = 50000

Modify column:

df["Age"] = df["Age"] + 1

===========================================================
🔟 DROPPING DATA
===========================================================

Drop column:

df.drop("Age", axis=1)

Drop row:

df.drop(0, axis=0)

axis=1 → column
axis=0 → row

===========================================================
1️⃣1️⃣ MISSING VALUES
===========================================================

Check missing:

df.isnull()

Remove rows:

df.dropna()

Fill missing:

df.fillna(0)

Very common in real projects.

===========================================================
1️⃣2️⃣ SORTING
===========================================================

df.sort_values("Age")

Descending:

df.sort_values("Age", ascending=False)

===========================================================
1️⃣3️⃣ GROUPBY (VERY IMPORTANT)
===========================================================

Group data:

df.groupby("Department")["Salary"].mean()

Concept:
Split → Apply → Combine

Common aggregations:

mean()
sum()
count()
max()
min()

Interview favorite topic.

===========================================================
1️⃣4️⃣ MERGE / JOIN
===========================================================

pd.merge(df1, df2, on="id")

Used to combine datasets.

===========================================================
1️⃣5️⃣ CHAINING OPERATIONS
===========================================================

df[df["Age"]>25].sort_values("Salary")

Powerful feature of Pandas.

===========================================================
1️⃣6️⃣ QUICK REAL-WORLD FLOW
===========================================================

1. Read file
2. Inspect (head, info, describe)
3. Handle missing values
4. Filter useful data
5. Group or aggregate
6. Prepare for ML

===========================================================
🔥 INTERVIEW SHORT NOTES
===========================================================

Q: loc vs iloc?
A: loc → labels, iloc → positions

Q: What does describe() show?
A: Summary statistics

Q: How to check null values?
A: df.isnull()

Q: What is groupby?
A: Split → Apply → Combine

Q: How to drop column?
A: df.drop("col", axis=1)

===========================================================
🔥 DAILY MEMORY SHORTCUTS
===========================================================

NumPy → Math
Pandas → Data handling

loc = label
iloc = index
axis=0 → row
axis=1 → column

Groupby = aggregation
describe = stats
info = structure

===========================================================