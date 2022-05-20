 import <package>.<module>
 import modules.calcuator as calc 
# OR 
 from modules.calculator import *

# you can use the function from calculator.py (import everything)
# import calculator

# print(calculator.add(10, 20))

# this is direct way to access add AND multiply
from modules.calculator import add, multiply

print(add(1, 3))

# import everything
# from calculator import *

# abbreviation of file name:
import modules.calculator as calc

# built-in library:
import math
