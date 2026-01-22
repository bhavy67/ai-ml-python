====================================================
M1 Advance Mathematics for ML and DS – NOTES
====================================================

-------------------------
BINOMIAL PROBABILITY
-------------------------

The formula for finding binomial probability is:

P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)

where,

C(n, k) = n! / (k! * (n - k)!)
n = total number of trials
k = number of successes
p = probability of success in ONE trial
1 - p = probability of failure in ONE trial

----------------------------------------------------

STEP 1: Learn to RECOGNIZE a Binomial Question

A question is BINOMIAL-TYPE if ALL of the following conditions are true:

✔ Fixed number of trials  
Examples:
- 4 coin tosses
- 5 balls drawn with replacement
- 10 students tested
- 6 matches played

👉 Number of trials is FIXED.

✔ Only TWO outcomes per trial  
Examples:
- Success / Failure
- Red / Blue
- Pass / Fail
- Win / Lose

👉 No third option is allowed.

✔ Probability stays the SAME every trial  
Examples:
- Coin toss → always 0.5
- With replacement → same probability
- Same machine → same defect rate

👉 This condition is VERY IMPORTANT.

✔ Trials are independent  
What happens in one trial does NOT affect the next trial.

👉 If ALL four conditions are satisfied → use BINOMIAL probability.

----------------------------------------------------

STEP 2: Understand what the question is ASKING

Typical binomial questions use keywords such as:

- exactly
- at least
- at most
- no
- only
- number of successes

👉 These keywords tell you HOW to apply the binomial formula.

----------------------------------------------------

====================================================
VECTORS – COMPLETE REVISION NOTES (2D FOCUS)
====================================================

-------------------------
1. WHAT IS A VECTOR?
-------------------------

A VECTOR is a quantity that has:
✔ Magnitude (size)
✔ Direction

Examples:
- Displacement
- Velocity
- Force
- Acceleration

A SCALAR has only magnitude (no direction).
Examples:
- Speed
- Mass
- Temperature
- Time

----------------------------------------------------

-------------------------
2. REPRESENTATION OF A VECTOR
-------------------------

In 2D (two dimensions), a vector is written as:

v = <x, y>

or

v = xi + yj

where:
i = unit vector along x-axis
j = unit vector along y-axis

Example:
v = <3, 4> = 3i + 4j

----------------------------------------------------

-------------------------
3. MAGNITUDE OF A 2D VECTOR
-------------------------

If v = <x, y>, then magnitude |v| is:

|v| = √(x² + y²)

Example:
v = <3, 4>

|v| = √(3² + 4²)
    = √(9 + 16)
    = √25
    = 5

----------------------------------------------------

-------------------------
4. ZERO VECTOR
-------------------------

A ZERO VECTOR has:

Magnitude = 0
Direction = undefined

Written as:
0 = <0, 0>

----------------------------------------------------

-------------------------
5. UNIT VECTOR
-------------------------

A UNIT VECTOR is a vector with:

Magnitude = 1

Formula to find unit vector in direction of v:

v̂ = v / |v|

Example:
v = <3, 4>
|v| = 5

Unit vector:
v̂ = <3/5, 4/5>

----------------------------------------------------

-------------------------
6. VECTOR ADDITION
-------------------------

If:
a = <a₁, a₂>
b = <b₁, b₂>

Then:
a + b = <a₁ + b₁, a₂ + b₂>

Example:
a = <2, 3>
b = <4, 1>

a + b = <6, 4>

----------------------------------------------------

-------------------------
7. VECTOR SUBTRACTION
-------------------------

a − b = <a₁ − b₁, a₂ − b₂>

Example:
a = <5, 4>
b = <2, 1>

a − b = <3, 3>

----------------------------------------------------

-------------------------
8. SCALAR MULTIPLICATION
-------------------------

If k is a scalar and v = <x, y>:

k v = <kx, ky>

Example:
2 <3, −1> = <6, −2>

----------------------------------------------------

-------------------------
9. DOT PRODUCT (SCALAR PRODUCT)
-------------------------

For vectors:
a = <a₁, a₂>
b = <b₁, b₂>

Dot product formula:

a · b = a₁b₁ + a₂b₂

Alternate formula:

a · b = |a||b|cosθ

where θ is the angle between the vectors.

----------------------------------------------------

EXAMPLES:

Example 1:
a = <1, 2>
b = <3, 4>

a · b = (1×3) + (2×4)
      = 3 + 8
      = 11

----------------------------------------------------

-------------------------
10. PROPERTIES OF DOT PRODUCT
-------------------------

✔ a · b = b · a  
✔ a · a = |a|²  
✔ a · 0 = 0  

If:
a · b = 0 → vectors are PERPENDICULAR

----------------------------------------------------

-------------------------
11. ANGLE BETWEEN TWO VECTORS
-------------------------

cosθ = (a · b) / (|a||b|)

θ = cos⁻¹[(a · b) / (|a||b|)]

----------------------------------------------------

-------------------------
12. PROJECTION OF A VECTOR
-------------------------

Projection of vector a on vector b:

proj_b(a) = (a · b / |b|²) b

Scalar projection (length only):

comp_b(a) = (a · b) / |b|

----------------------------------------------------

-------------------------
13. DIRECTION COSINES (2D)
-------------------------

If v = <x, y> and |v| is magnitude:

cosα = x / |v|
cosβ = y / |v|

----------------------------------------------------

-------------------------
14. IMPORTANT EXAM SHORTCUTS
-------------------------

✔ Zero vector has no direction  
✔ Unit vector magnitude is always 1  
✔ Dot product gives a SCALAR  
✔ Perpendicular vectors → dot product = 0  
✔ Projection always uses dot product  

----------------------------------------------------

-------------------------
15. QUICK FORMULA SUMMARY
-------------------------

Magnitude:
|v| = √(x² + y²)

Unit vector:
v̂ = v / |v|

Dot product:
a · b = a₁b₁ + a₂b₂

Angle:
cosθ = (a · b) / (|a||b|)

Projection:
proj_b(a) = (a · b / |b|²) b

----------------------------------------------------