Purpose of this Application
==============================
This application was created for training purposes.
No warranty given

Important hints when using Python as programming language
=========================================================

1) General Guidelines
See "PEP 8"


2) Install new libraries
Command:
python -m pip install -U matplotlib

3) Include additional libraries
# reading file with csv module AND plotting it with matplotlib
import csv
import matplotlib.pyplot as plt


4) More info about reading CSV files
Below you can find links for reading CSV files (official Python documentation) 

https://docs.python.org/3/library/csv.html


5) Basics in matplotlib module (official basics tutorial in the website of matplotlib.org)

https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

6)  official Python documentation

It includes very useful explanations and a complete list of python functions etc...
https://docs.python.org/

7) Linear Programming using PuLP
https://towardsdatascience.com/linear-programming-and-discrete-optimization-with-python-using-pulp-449f3c5f6e99
PuLP — a Python library for linear optimization
There are many libraries in the Python ecosystem for this kind of optimization problems. PuLP is an open-source linear programming (LP) package which largely uses Python syntax and comes packaged with many industry-standard solvers. It also integrates nicely with a range of open source and commercial LP solvers.
You can install it using pip (and also some additional solvers)
$ sudo pip install pulp            # PuLP
$ sudo apt-get install glpk-utils  # GLPK
$ sudo apt-get install coinor-cbc  # CoinOR

8.) Separators:
Tab = \t
