# 📈 Matplotlib – Beginner Notes

Matplotlib = Base plotting library

--------------------------------------------
INSTALL
--------------------------------------------
pip install matplotlib

--------------------------------------------
IMPORT
--------------------------------------------
import matplotlib.pyplot as plt

--------------------------------------------
BASIC PLOT
--------------------------------------------

plt.plot(x,y)
plt.show()

--------------------------------------------
COMMON PLOTS
--------------------------------------------

plt.bar(x,y)
plt.scatter(x,y)
plt.hist(data)
plt.pie(data)

--------------------------------------------
CUSTOMIZATION
--------------------------------------------

plt.title("Title")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()

--------------------------------------------
IMPORTANT
--------------------------------------------

Always use:
plt.show()

--------------------------------------------
INTERVIEW
--------------------------------------------

Matplotlib is low-level plotting library.
Seaborn is built on top of it.