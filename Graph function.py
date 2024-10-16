# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating vectors X and Y
x = np.linspace(0, 5, 20)
y = 2*x

fig = plt.figure(figsize=(12, 7))
# Create the plot
plt.plot(x, y, alpha=0.5, label='y = 2x',
		color='red', linestyle='-',
		linewidth=1, marker='+',
		markersize=10, markerfacecolor='blue',
		markeredgecolor='blue')

# Add a title
plt.title('Linear Equation PLot')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=.6, linestyle='--')

# Add a Legend
plt.legend()

# Show the plot
plt.show()