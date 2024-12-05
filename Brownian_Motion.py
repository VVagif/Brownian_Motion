import random
import matplotlib.pyplot as plt

# Parameters
steps = 100
position = 0
positions = [position]

# Simulate random walk
for _ in range(steps):
    step = random.choice([-1, 1])  # Move left or right randomly
    position += step
    positions.append(position)

# Plot the random walk
plt.plot(positions, marker='o', markersize=4)
plt.title('1D Random Walk Simulation')
plt.xlabel('Step Number')
plt.ylabel('Position')
plt.grid()
plt.show()
