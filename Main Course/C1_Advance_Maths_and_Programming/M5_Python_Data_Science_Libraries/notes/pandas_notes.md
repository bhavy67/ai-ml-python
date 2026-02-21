# 📊 Pandas – Beginner to Interview Notes

Pandas = Data Manipulation Library

--------------------------------------------
INSTALL
--------------------------------------------
pip install pandas

--------------------------------------------
IMPORT
--------------------------------------------
import pandas as pd

--------------------------------------------
WHAT IS SERIES?
--------------------------------------------
1D labeled array (like Excel column)

s = pd.Series([10,20,30])

With custom index:

s = pd.Series([10,20,30], index=['a','b','c'])
s['a']

--------------------------------------------
WHAT IS DATAFRAME?
--------------------------------------------
2D table (rows + columns)

df = pd.DataFrame({
    "Name": ["A","B"],
    "Age": [20,25]
})

--------------------------------------------
LOAD DATA
--------------------------------------------

pd.read_csv("file.csv")
pd.read_excel("file.xlsx")

--------------------------------------------
QUICK INSPECTION
--------------------------------------------

df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns

Important:
info() → data types + null
describe() → numeric summary

--------------------------------------------
SELECTING DATA
--------------------------------------------

df["Age"]
df[["Name","Age"]]
df.loc[0]
df.iloc[0]

loc → label
iloc → index

--------------------------------------------
FILTERING
--------------------------------------------

df[df["Age"] > 20]

Multiple conditions:

df[(df["Age"] > 20) & (df["Age"] < 30)]

--------------------------------------------
ADD / DROP
--------------------------------------------

df["New"] = 100
df.drop("Age", axis=1)
df.drop(0, axis=0)

axis=1 → column
axis=0 → row

--------------------------------------------
MISSING DATA
--------------------------------------------

df.isnull()
df.dropna()
df.fillna(0)

--------------------------------------------
GROUPBY (VERY IMPORTANT)
--------------------------------------------

df.groupby("Dept")["Salary"].mean()

Interview favorite.

--------------------------------------------
SORTING
--------------------------------------------

df.sort_values("Age")

--------------------------------------------
MERGE
--------------------------------------------

pd.merge(df1, df2, on="id")

--------------------------------------------
INTERVIEW QUESTIONS
--------------------------------------------

1. loc vs iloc?
2. What is groupby?
3. How to handle missing data?
4. How to merge dataframes?

--------------------------------------------
REMEMBER
--------------------------------------------

Pandas = Data Cleaning + Manipulation
Most used in real projects