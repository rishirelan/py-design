"""
Compute a sparse grid: Gauss Hermite Open Weakly Nested rule.

Author:
    Ilias Bilionis

Date:
    3/19/2014

"""


import design
import numpy as np
import matplotlib.pyplot as plt

# The number of input dimensions
num_dim = 2
# The maximum level of the grid
max_level = 4
# Draw the design
X, w = design.sparse_grid(num_dim, max_level, rule='GH')
print 'After:'
print 'Grid points:'
print X
print 'Weights:'
print w
# And plot it
plt.plot(X[:, 0], X[:, 1], '.', markersize=10)
plt.xlabel('$x_1$', fontsize=16)
plt.ylabel('$x_2$', fontsize=16)
plt.title('Gauss Hermite Open Weakly Nested rule', fontsize=16)
plt.show()