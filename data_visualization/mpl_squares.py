import matplotlib.pyplot as plt

input_values = list(range(1,6))
squares = [x**2 for x in input_values]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and lavel axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()