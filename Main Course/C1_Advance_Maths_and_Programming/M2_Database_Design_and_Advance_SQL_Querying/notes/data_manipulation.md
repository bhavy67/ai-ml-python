====================================================
DATA MANIPULATION – LONG & WIDE TABLE FORMATS
====================================================

-------------------------
1. WHAT IS DATA SHAPE?
-------------------------

Data shape refers to HOW data is arranged in a table:
- Number of rows
- Number of columns
- How variables are stored

Two most common shapes:
✔ LONG format
✔ WIDE format

----------------------------------------------------

-------------------------
2. LONG TABLE FORMAT
-------------------------

In LONG format:
✔ Each row is ONE observation
✔ A single column stores variable names
✔ Another column stores values

Characteristics:
- More rows
- Fewer columns
- Easier for analysis & visualization
- Preferred for SQL, Python (pandas), R

----------------------------------------------------

EXAMPLE: LONG FORMAT

| student | subject | marks |
|--------|---------|-------|
| A      | Math    | 80    |
| A      | Science | 70    |
| B      | Math    | 90    |
| B      | Science | 85    |

----------------------------------------------------

WHEN TO USE LONG FORMAT

✔ Time series data
✔ Multiple categories
✔ Grouped analysis
✔ Visualization (charts, plots)
✔ SQL aggregations

----------------------------------------------------

-------------------------
3. WIDE TABLE FORMAT
-------------------------

In WIDE format:
✔ Each variable has its own column
✔ Fewer rows
✔ More columns
✔ Easier to read manually

----------------------------------------------------

EXAMPLE: WIDE FORMAT

| student | Math | Science |
|--------|------|---------|
| A      | 80   | 70      |
| B      | 90   | 85      |

----------------------------------------------------

WHEN TO USE WIDE FORMAT

✔ Reporting
✔ Dashboards
✔ Machine learning input
✔ Spreadsheet usage

----------------------------------------------------

-------------------------
4. LONG vs WIDE (KEY DIFFERENCES)
-------------------------

| Feature        | Long Format       | Wide Format       |
|---------------|------------------|------------------|
| Rows          | More             | Fewer            |
| Columns       | Fewer            | More             |
| Analysis      | Easier           | Harder           |
| Visualization | Preferred        | Not ideal        |
| Readability   | Lower            | Higher           |

----------------------------------------------------

-------------------------
5. CONVERTING LONG → WIDE
-------------------------

This process is called:
✔ PIVOT
✔ SPREAD
✔ RESHAPE

----------------------------------------------------

LONG → WIDE LOGIC

- Choose identifier columns
- Choose column to spread into headers
- Choose values to fill cells

----------------------------------------------------

SQL EXAMPLE (PIVOT using CASE)

SELECT
    student,
    MAX(CASE WHEN subject = 'Math' THEN marks END) AS Math,
    MAX(CASE WHEN subject = 'Science' THEN marks END) AS Science
FROM students
GROUP BY student;

----------------------------------------------------

PYTHON (PANDAS)

df.pivot(
    index='student',
    columns='subject',
    values='marks'
)

----------------------------------------------------

WHEN CONVERT LONG → WIDE

✔ Reporting
✔ Summary tables
✔ Feature engineering
✔ ML models

----------------------------------------------------

-------------------------
6. CONVERTING WIDE → LONG
-------------------------

This process is called:
✔ UNPIVOT
✔ MELT
✔ GATHER

----------------------------------------------------

WIDE → LONG LOGIC

- Keep identifier columns fixed
- Convert multiple columns into:
  - one variable column
  - one value column

----------------------------------------------------

SQL EXAMPLE (UNPIVOT style)

SELECT student, 'Math' AS subject, Math AS marks FROM table
UNION ALL
SELECT student, 'Science', Science FROM table;

----------------------------------------------------

PYTHON (PANDAS)

df.melt(
    id_vars=['student'],
    var_name='subject',
    value_name='marks'
)

----------------------------------------------------

WHEN CONVERT WIDE → LONG

✔ Aggregations
✔ Group-by analysis
✔ Visualization
✔ SQL queries
✔ Window functions

----------------------------------------------------

-------------------------
7. COMMON MISTAKES
-------------------------

❌ Using wide format for analytics
❌ Forgetting GROUP BY after pivot
❌ Losing identifiers during reshape
❌ Using long format for ML directly

----------------------------------------------------

-------------------------
8. INTERVIEW & EXAM TIPS
-------------------------

✔ Long format is ANALYSIS-FRIENDLY
✔ Wide format is REPORTING-FRIENDLY
✔ Pivot = rows → columns
✔ Unpivot = columns → rows
✔ Most SQL problems prefer LONG data

----------------------------------------------------

-------------------------
9. ONE-LINE MEMORY RULES
-------------------------

LONG FORMAT:
"More rows, fewer columns"

WIDE FORMAT:
"More columns, fewer rows"

PIVOT:
"Rows become columns"

UNPIVOT:
"Columns become rows"

----------------------------------------------------

-------------------------
10. QUICK CHEAT SHEET
-------------------------

Operation            | Name
---------------------|---------
Long → Wide          | Pivot
Wide → Long          | Unpivot / Melt
SQL                  | CASE + GROUP BY
Python (pandas)      | pivot(), melt()

----------------------------------------------------