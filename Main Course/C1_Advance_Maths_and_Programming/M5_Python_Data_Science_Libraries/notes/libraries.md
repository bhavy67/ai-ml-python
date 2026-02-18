# 🐍 PYTHON DATA SCIENCE – COMPLETE LAST MINUTE NOTES
Simple | Interview Ready | Daily Use | Easy Grammar | Quick Revision

============================================================
SECTION 1️⃣  NUMPY
============================================================

🔹 Why NumPy?
- Faster than Python lists
- Uses C internally
- Supports vectorized operations
- Used in ML, Data Science, AI

------------------------------------------------------------
🔹 Creating Arrays
------------------------------------------------------------

import numpy as np

a = np.array([1,2,3])
np.zeros(3)
np.ones(3)
np.arange(0,10,2)       # start, stop, step
np.linspace(0,1,5)      # start, stop, number of values
np.random.rand(3,3)

🧠 Trick:
arange → step
linspace → count

------------------------------------------------------------
🔹 Important Attributes
------------------------------------------------------------

a.shape     # (rows, columns)
a.ndim      # dimensions
a.size      # total elements
a.dtype     # data type

Interview: shape returns tuple.

------------------------------------------------------------
🔹 Indexing & Slicing
------------------------------------------------------------

a[0]
a[1:4]
a[:,1]
a[1,2]

: means full row or column

------------------------------------------------------------
🔹 Reshape
------------------------------------------------------------

a.reshape(2,3)
a.flatten()

------------------------------------------------------------
🔹 Math Operations (Vectorized)
------------------------------------------------------------

a + 5
a * 2
a1 + a2
np.sum(a)
np.mean(a)
np.max(a)
np.min(a)
np.std(a)

Interview: Vectorization = No loops = Faster.

------------------------------------------------------------
🔹 Broadcasting
------------------------------------------------------------

a + 10

Automatically applies to all elements.

============================================================
SECTION 2️⃣  PANDAS SERIES
============================================================

🔹 What is Series?
- 1D labeled array
- Like Excel column

import pandas as pd

s = pd.Series([10,20,30])

------------------------------------------------------------
🔹 Custom Index
------------------------------------------------------------

s = pd.Series([10,20,30], index=['a','b','c'])
s['a']

------------------------------------------------------------
🔹 Useful Methods
------------------------------------------------------------

s.head()
s.tail()
s.value_counts()
s.unique()
s.isnull()

============================================================
SECTION 3️⃣  PANDAS DATAFRAME
============================================================

🔹 What is DataFrame?
- 2D table (rows + columns)

df = pd.DataFrame({
    "Name": ["A","B"],
    "Age": [20,25]
})

------------------------------------------------------------
🔹 Load Data
------------------------------------------------------------

pd.read_csv("file.csv")
pd.read_excel("file.xlsx")

------------------------------------------------------------
🔹 Quick Inspection
------------------------------------------------------------

df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns

Interview:
info() → datatypes + nulls
describe() → numeric summary

------------------------------------------------------------
🔹 Selecting Data
------------------------------------------------------------

df["Age"]
df[["Name","Age"]]
df.loc[0]      # label based
df.iloc[0]     # index based

🧠 loc → label
🧠 iloc → index number

------------------------------------------------------------
🔹 Filtering
------------------------------------------------------------

df[df["Age"] > 20]

Multiple conditions:

df[(df["Age"] > 20) & (df["Age"] < 30)]

------------------------------------------------------------
🔹 Add / Drop
------------------------------------------------------------

df["New"] = 100
df.drop("Age", axis=1)
df.drop(0, axis=0)

axis=1 → column
axis=0 → row

------------------------------------------------------------
🔹 Missing Data
------------------------------------------------------------

df.isnull()
df.dropna()
df.fillna(0)

------------------------------------------------------------
🔹 GroupBy (VERY IMPORTANT)
------------------------------------------------------------

df.groupby("Dept")["Salary"].mean()

Interview favorite.

------------------------------------------------------------
🔹 Sorting
------------------------------------------------------------

df.sort_values("Age")

------------------------------------------------------------
🔹 Merge
------------------------------------------------------------

pd.merge(df1, df2, on="id")

============================================================
SECTION 4️⃣  MATPLOTLIB
============================================================

🔹 Basic Plot

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.show()

------------------------------------------------------------
🔹 Common Plots
------------------------------------------------------------

plt.bar(x,y)
plt.scatter(x,y)
plt.hist(data)
plt.pie(data)

------------------------------------------------------------
🔹 Customization
------------------------------------------------------------

plt.title("Title")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()

Interview:
Matplotlib = Base plotting library.

============================================================
SECTION 5️⃣  SEABORN
============================================================

Built on Matplotlib.
Better visuals. Less code.

import seaborn as sns

------------------------------------------------------------
🔹 Common Plots
------------------------------------------------------------

sns.lineplot(x="x", y="y", data=df)
sns.barplot(x="x", y="y", data=df)
sns.histplot(df["Age"])
sns.boxplot(x="Gender", y="Salary", data=df)
sns.heatmap(df.corr(), annot=True)

------------------------------------------------------------
🔹 Why Seaborn?
------------------------------------------------------------
- Beautiful default themes
- Statistical plots
- Easy heatmaps

Interview:
Seaborn = High level
Matplotlib = Low level

============================================================
🔥 MOST ASKED INTERVIEW QUESTIONS
============================================================

1️⃣ List vs NumPy array?
- List slow
- NumPy fast (vectorized)

2️⃣ loc vs iloc?
- loc → label
- iloc → index

3️⃣ What is broadcasting?
- Automatic element-wise operation.

4️⃣ What does groupby do?
- Split → Apply → Combine

5️⃣ Why Pandas?
- Data cleaning
- Data manipulation
- Easy CSV handling

============================================================
🔥 DAILY USE SHORTCUT MEMORY
============================================================

NumPy → Math
Pandas → Data handling
Matplotlib → Basic plots
Seaborn → Beautiful plots

loc = label
iloc = index
axis=0 row
axis=1 column

Vectorization > Loop
Groupby = Interview magnet

============================================================