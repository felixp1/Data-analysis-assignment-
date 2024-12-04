import matplotlib.pyplot as plt

# Data from the table
with_music = [304, 257, 174, 214, 69, 317, 387, 47, 157, 0, 332, 308, 317, 286, 236, 299, 206, 278, 188, 43, 0, 0, 0, 0, 0]
without_music = [292, 270, 47, 288, 324, 292, 364, 316, 287, 75, 282, 149, 274, 319, 213, 3, 324, 2, 128, 219, 94, 164, 0, 0, 0]

# 1. Histograms
plt.figure(figsize=(12, 6))
plt.hist(with_music, bins=10, alpha=0.7, label='With Music', color='blue', edgecolor='black')
plt.hist(without_music, bins=10, alpha=0.7, label='Without Music', color='green', edgecolor='black')
plt.title('Histogram of Plant Growth (With and Without Music)')
plt.xlabel('Plant Growth (mm)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Dot plots
plt.figure(figsize=(12, 6))
plt.scatter(['With Music'] * len(with_music), with_music, color='blue', label='With Music')
plt.scatter(['Without Music'] * len(without_music), without_music, color='green', label='Without Music')
plt.title('Dot Plot of Plant Growth (With and Without Music)')
plt.ylabel('Plant Growth (mm)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Variability Description
print("Comparison of Plant Growth Distributions:")
print("1. Histogram: Plants exposed to music show a wider distribution of growth values, with some very high growth values and several zeros. Without music, growth appears more consistent but with fewer extreme values.")
print("2. Dot Plot: The 'with music' group shows greater variability, with a mix of high and low values. The 'without music' group has fewer outliers and more mid-range values.")
