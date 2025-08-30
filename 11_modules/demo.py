# importing of modules
# 1st approach -> whole module
import math
print(math.sqrt(25))

# 2nd approach -> specific functionality in module
from math import sqrt
print(sqrt(25))

# optional -> can use alias names as well for easy readability
import math as m 
print(m.sqrt(25))



