Creating and Exploring Packages

To tell Python that a particular directory is a package, we create a file named __init__.py inside it and then it is considered as a package and we may create other modules and sub-packages within it. This __init__.py file can be left blank or can be coded with the initialization code for the package.
To create a package in Python, we need to follow these three simple steps:

First, we create a directory and give it a package name, preferably related to its operation.
Then we put the classes and the required functions in it.
Finally we create an __init__.py file inside the directory, to let Python know that the directory is a package.
Example of Creating Package

Let’s look at this example and see how a package is created. Let’s create a package named Cars and build three modules in it namely, Bmw, Audi and Nissan.



First we create a directory and name it Cars.
Then we need to create modules. To do this we need to create a file with the name Bmw.py and create its content by putting this code into it.


Then we create another file with the name Audi.py and add the similar type of code to it with different members.

Then we create another file with the name Nissan.py and add the similar type of code to it with different members.


Finally we create the __init__.py file. This file will be placed inside Cars directory and can be left blank or we can put this initialisation code into it.

from Bmw import Bmw
from Audi import Audi
from Nissan import Nissan