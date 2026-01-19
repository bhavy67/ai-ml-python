========================================================
PROBABILITY, STATISTICS & COMBINATORICS – MASTER NOTES
========================================================

(Use for exams, interviews, revision, quick reference)
--------------------------------------------------------

--------------------------------------------------------
SECTION 1: BASIC PROBABILITY
--------------------------------------------------------

1. Probability Formula
----------------------
P(A) = Number of favourable outcomes / Total outcomes

Example:
Rolling a die, probability of getting 3:
P = 1 / 6


2. Addition Rule (OR Rule)
--------------------------
Used when events can happen together or separately.

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

If A and B are mutually exclusive:
P(A ∪ B) = P(A) + P(B)

Example:
Card is red OR king:
P(red) = 26/52
P(king) = 4/52
P(red king) = 2/52

P = 26/52 + 4/52 − 2/52 = 28/52


3. Multiplication Rule (AND Rule)
---------------------------------
Used when events happen together.

P(A ∩ B) = P(A) × P(B|A)

If independent:
P(A ∩ B) = P(A) × P(B)

Example:
Two dice, both give 6:
P = 1/6 × 1/6 = 1/36


--------------------------------------------------------
SECTION 2: CONDITIONAL PROBABILITY
--------------------------------------------------------

4. Conditional Probability
--------------------------
P(A|B) = P(A ∩ B) / P(B)

Meaning: Probability of A given B has happened.


5. Bayes Theorem
----------------
Used to reverse conditional probability.

P(A|B) = [P(B|A) × P(A)] / P(B)

Where:
P(B) = P(B|A)P(A) + P(B|A')P(A')

Example (Spam Filter):
20% mails are spam
Spam detected correctly = 90%
Normal wrongly marked spam = 10%

Use Bayes to find actual probability.


--------------------------------------------------------
SECTION 3: PERMUTATION & COMBINATION
--------------------------------------------------------

6. Factorial
------------
n! = n × (n−1) × (n−2) ... × 1
0! = 1

Example:
5! = 120


7. Permutation (Order matters)
------------------------------
nPr = n! / (n−r)!

Example:
Arranging 3 people from 5:
5P3 = 5 × 4 × 3 = 60


8. Combination (Order does NOT matter)
--------------------------------------
nCr = n! / [r!(n−r)!]

Example:
Selecting 3 people from 5:
5C3 = 10

Shortcut:
nCr = nC(n−r)


--------------------------------------------------------
SECTION 4: DESCRIPTIVE STATISTICS
--------------------------------------------------------

9. Mean (Average)
-----------------
Mean = Sum of values / Number of values

Example:
(2,4,6,8) → Mean = 5


10. Median
----------
Sort values first.

If odd count:
Median = middle value

If even count:
Median = average of two middle values

Example:
(1,3,5,7) → Median = 4
(1,3,5) → Median = 3


11. Mode
--------
Value that occurs most frequently.

Example:
(1,2,2,3,4) → Mode = 2


--------------------------------------------------------
SECTION 5: QUARTILES, DECILES, PERCENTILES
--------------------------------------------------------

12. Quartiles
-------------
Q1 = 25th percentile
Q2 = Median
Q3 = 75th percentile

Used to understand data spread.


13. Deciles
-----------
Divide data into 10 equal parts.
D1 = 10%, D5 = Median, D9 = 90%


14. Percentiles
---------------
Divide data into 100 equal parts.

Example:
90th percentile means 90% data is below it.


--------------------------------------------------------
SECTION 6: MEASURES OF DISPERSION
--------------------------------------------------------

15. Range
---------
Range = Max − Min

Example:
(3,7,10) → Range = 7


16. Mean Deviation
------------------
Mean of absolute deviations from mean or median.

MD = Σ|xi − Mean| / n


17. Variance
------------
Population Variance:
σ² = Σ(x − μ)² / n

Sample Variance:
s² = Σ(x − x̄)² / (n−1)


18. Standard Deviation
---------------------
SD = √Variance

Low SD → data close to mean
High SD → data spread out


--------------------------------------------------------
SECTION 7: COVARIANCE & CORRELATION
--------------------------------------------------------

19. Covariance
--------------
Cov(X,Y) = Σ[(xi−x̄)(yi−ȳ)] / n

Positive → move together
Negative → move opposite


20. Correlation
---------------
r = Cov(X,Y) / (σx × σy)

Range:
-1 ≤ r ≤ +1

r = 1 → perfect positive
r = -1 → perfect negative
r = 0 → no relation


--------------------------------------------------------
SECTION 8: IMPORTANT PROBABILITY DISTRIBUTIONS
--------------------------------------------------------

21. Binomial Distribution
-------------------------
Used for fixed trials with success/failure.

P(X=k) = nCk × p^k × (1−p)^(n−k)

Example:
Probability of 2 heads in 4 tosses.


22. Normal Distribution
-----------------------
Bell-shaped curve.
Mean = Median = Mode

68% data → ±1σ
95% data → ±2σ
99.7% → ±3σ


--------------------------------------------------------
SECTION 9: SHORTCUTS & EXAM TRICKS
--------------------------------------------------------

• Complement Rule:
P(A') = 1 − P(A)

• At least one:
P(at least one) = 1 − P(none)

• Without replacement → probabilities change
• With replacement → probabilities constant

• Permutation → ORDER matters
• Combination → ORDER does not matter

• Mean affected by extreme values
• Median not affected by outliers

• High variance → unstable data
• Low variance → consistent data


--------------------------------------------------------
SECTION 10: QUICK REVISION CHECKLIST
--------------------------------------------------------

✔ Addition rule
✔ Multiplication rule
✔ Conditional probability
✔ Bayes theorem
✔ Permutations vs combinations
✔ Mean / Median / Mode
✔ Quartiles / Percentiles
✔ Variance & Standard deviation
✔ Covariance & Correlation
✔ Common shortcuts

--------------------------------------------------------
END OF NOTES
--------------------------------------------------------