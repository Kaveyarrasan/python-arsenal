# Use Case 6: Import vs from import
#
# Create simple functions like add(a,b) and div(a,b) that returns sum and division of 2 input.
# Create a package/sub package/generic_functions.py and place this function.
# Create another package/sub package/consumer.py and import the above 2 functions using import, from import with and without alias.

from root_package_1.root_sub_package_1_1 import generic_functions as gf
from root_package_1.root_sub_package_1_1.generic_functions import add, div

a = 5
b = 3

# Operations with alias
result_gf_add = gf.add(a, b)   # Function returns total with alias
result_gf_div = gf.div(a, b)   # Function returns factor with alias
print(f"Result with alias - Add: {result_gf_add}, Div: {result_gf_div}")

# Operations without alias
result_add = add(a, b)   # Function returns total with alias
result_div = div(a, b)   # Function returns factor with alias
print(f"Result without alias - Add: {result_add}, Div: {result_div}")