====================================================
SQL WINDOW FUNCTIONS – COMPLETE REVISION NOTES
====================================================

-------------------------
1. WHAT IS A WINDOW FUNCTION?
-------------------------

A WINDOW FUNCTION performs a calculation across a set of rows
that are RELATED to the current row.

IMPORTANT:
✔ It does NOT collapse rows (unlike GROUP BY)
✔ Each row still appears in the output
✔ It adds extra calculated columns

----------------------------------------------------

-------------------------
2. WINDOW FUNCTION SYNTAX
-------------------------

SELECT
    column_name,
    WINDOW_FUNCTION(...) OVER (
        PARTITION BY column_name
        ORDER BY column_name
        ROWS / RANGE
    ) AS alias
FROM table_name;

----------------------------------------------------

KEYWORDS MEANING:

WINDOW_FUNCTION → function to apply (SUM, AVG, RANK, etc.)
OVER()          → defines the window
PARTITION BY   → divides data into groups
ORDER BY       → orders rows inside each partition
ROWS / RANGE   → defines frame (subset of rows)

----------------------------------------------------

-------------------------
3. DIFFERENCE: GROUP BY vs WINDOW FUNCTION
-------------------------

GROUP BY:
✔ Reduces rows
✔ One row per group
✔ Aggregates only

WINDOW FUNCTION:
✔ Keeps all rows
✔ Calculates over related rows
✔ Can show row-level + aggregate together

----------------------------------------------------

-------------------------
4. PARTITION BY
-------------------------

PARTITION BY splits the data into GROUPS
(similar to GROUP BY but does not reduce rows)

Example:
Calculate total salary per department

SELECT
    emp_name,
    department,
    salary,
    SUM(salary) OVER (PARTITION BY department) AS dept_total
FROM employees;

----------------------------------------------------

-------------------------
5. ORDER BY IN WINDOW FUNCTIONS
-------------------------

ORDER BY defines the ORDER inside each partition

Example:
Running total of salary per department

SELECT
    emp_name,
    department,
    salary,
    SUM(salary) OVER (
        PARTITION BY department
        ORDER BY salary
    ) AS running_total
FROM employees;

----------------------------------------------------

-------------------------
6. ROWS vs RANGE
-------------------------

ROWS:
✔ Physical row count
✔ Exact number of rows

RANGE:
✔ Logical range
✔ Based on ORDER BY value

Example (ROWS):

ROWS BETWEEN 2 PRECEDING AND CURRENT ROW

----------------------------------------------------

-------------------------
7. COMMON WINDOW FUNCTIONS
-------------------------

-------------------------
A. AGGREGATE FUNCTIONS
-------------------------

SUM()
AVG()
COUNT()
MIN()
MAX()

Example:
Average salary per department

AVG(salary) OVER (PARTITION BY department)

----------------------------------------------------

-------------------------
B. RANKING FUNCTIONS
-------------------------

RANK()       → skips ranks if tie
DENSE_RANK() → no gaps
ROW_NUMBER() → unique number

Example:

SELECT
    emp_name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;

----------------------------------------------------

-------------------------
C. OFFSET FUNCTIONS
-------------------------

LAG()  → previous row
LEAD() → next row

Example:
Compare salary with previous employee

SELECT
    emp_name,
    salary,
    LAG(salary) OVER (ORDER BY salary) AS prev_salary
FROM employees;

----------------------------------------------------

-------------------------
D. VALUE FUNCTIONS
-------------------------

FIRST_VALUE()
LAST_VALUE()
NTH_VALUE()

Example:
Highest salary in each department

FIRST_VALUE(salary)
OVER (
    PARTITION BY department
    ORDER BY salary DESC
)

----------------------------------------------------

-------------------------
8. RUNNING TOTAL
-------------------------

SELECT
    date,
    sales,
    SUM(sales) OVER (
        ORDER BY date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_sales
FROM sales_table;

----------------------------------------------------

-------------------------
9. MOVING AVERAGE
-------------------------

SELECT
    date,
    sales,
    AVG(sales) OVER (
        ORDER BY date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg
FROM sales_table;

----------------------------------------------------

-------------------------
10. WINDOW FRAME CLAUSES
-------------------------

UNBOUNDED PRECEDING
UNBOUNDED FOLLOWING
CURRENT ROW
N PRECEDING
N FOLLOWING

Example:
ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING

----------------------------------------------------

-------------------------
11. IMPORTANT RULES (VERY IMPORTANT)
-------------------------

✔ OVER() is mandatory for window functions
✔ WHERE clause is applied BEFORE window function
✔ WINDOW functions cannot be used in WHERE
✔ Use subquery if filtering is needed
✔ ORDER BY inside OVER() is optional but powerful

----------------------------------------------------

-------------------------
12. WINDOW FUNCTION vs SUBQUERY
-------------------------

Window functions are:
✔ Faster
✔ Cleaner
✔ More readable
✔ Preferred in interviews

----------------------------------------------------

-------------------------
13. COMMON INTERVIEW QUESTIONS
-------------------------

✔ Find highest salary per department
✔ Find second highest salary
✔ Running total
✔ Rank employees
✔ Compare current row with previous row
✔ Remove duplicates using ROW_NUMBER()

----------------------------------------------------

-------------------------
14. QUICK CHEAT SHEET
-------------------------

ROW_NUMBER() → unique numbering
RANK()       → skips numbers on tie
DENSE_RANK() → no skips
LAG()        → previous row
LEAD()       → next row
SUM() OVER   → running total
AVG() OVER   → moving average

----------------------------------------------------

-------------------------
15. ONE-LINE MEMORY RULE
-------------------------

WINDOW FUNCTIONS = AGGREGATES WITHOUT LOSING ROWS

----------------------------------------------------