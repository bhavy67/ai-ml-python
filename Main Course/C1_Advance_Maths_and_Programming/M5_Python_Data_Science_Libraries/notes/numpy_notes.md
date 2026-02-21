# 🧮 NumPy – Beginner to Interview Notes

NumPy = Numerical Python  
Used for fast mathematical operations.

--------------------------------------------
WHY NUMPY?
--------------------------------------------
- Faster than Python lists
- Supports vectorized operations
- Used in ML, AI, Data Science
- Handles large numerical data

--------------------------------------------
INSTALL
--------------------------------------------
pip install numpy

--------------------------------------------
IMPORT
--------------------------------------------
import numpy as np

--------------------------------------------
CREATING ARRAYS
--------------------------------------------

a = np.array([1,2,3])
np.zeros(3)
np.ones(3)
np.arange(0,10,2)
np.linspace(0,1,5)
np.random.rand(3,3)

Trick:
arange → step
linspace → number of values

--------------------------------------------
ARRAY PROPERTIES
--------------------------------------------

a.shape
a.ndim
a.size
a.dtype

Important:
shape gives (rows, columns)

--------------------------------------------
INDEXING & SLICING
--------------------------------------------

a[0]
a[1:4]
a[:,1]
a[1,2]

: means all rows or columns

--------------------------------------------
RESHAPING
--------------------------------------------

a.reshape(2,3)
a.flatten()

--------------------------------------------
MATH OPERATIONS
--------------------------------------------

a + 5
a * 2
a1 + a2
np.sum(a)
np.mean(a)
np.max(a)
np.min(a)
np.std(a)

Important:
Vectorization = No loops = Faster

--------------------------------------------
BROADCASTING
--------------------------------------------

a + 10

Automatically applied to all elements.

--------------------------------------------
INTERVIEW QUESTIONS
--------------------------------------------

1. Why NumPy faster?
   → C implementation + vectorization

2. What is broadcasting?
   → Automatic element-wise operation

3. Difference list vs NumPy?
   → List slower, NumPy faster

--------------------------------------------
REMEMBER
--------------------------------------------

NumPy = Math Engine
Use for numerical calculations