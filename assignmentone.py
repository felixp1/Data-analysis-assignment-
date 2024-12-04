import matplotlib.pyplot as plt
# Data for the bar chart
categories = ['Spinach', 'Sausage', 'Prawns', 'Pineapple', 'Mushroom']
proportions = [0.25, 0.2, 0.1, 0.27, 0.18]

# Create the horizontal bar chart
plt.figure(figsize=(8, 6))  # Optional: Set figure size
plt.barh(categories, proportions, color='purple', edgecolor='black')

# Add labels and title
plt.xlabel('Proportion of Total')
plt.ylabel('Categories')
plt.title('Proportion of Categories')

# Add grid lines for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
