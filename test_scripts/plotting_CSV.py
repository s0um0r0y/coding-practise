import pandas as pd
import matplotlib.pyplot as plt

# Read your CSV file
df = pd.read_csv('coding-practise/test_scripts/log.csv', parse_dates=['timestamp'])

fig, axs = plt.subplots(3, 1, figsize=(12, 18))

# Plot 1: System Parameters
for col in ['cpu_percent', 'ram_percent', 'gpu_percent', 'vram_percent', 'cpuT', 'gpuT']:
    axs[0].plot(df['timestamp'], df[col], label=col)
axs[0].set_ylabel('Values')
axs[0].set_title('System Parameters Over Time')
axs[0].legend()
axs[0].grid(True)

# Plot 2: Velocity Parameters
for col in ['linVel', 'angVel']:
    axs[1].plot(df['timestamp'], df[col], label=col)
axs[1].set_ylabel('Values')
axs[1].set_title('Velocity Parameters Over Time')
axs[1].legend()
axs[1].grid(True)

# Plot 3: Position Path Traced
axs[2].plot(df['posX'], df['posY'], marker='o', linestyle='-', color='b', label='Path traced by position')
axs[2].set_xlabel('posX')
axs[2].set_ylabel('posY')
axs[2].set_title('Position Path Traced')
axs[2].legend()
axs[2].grid(True)
axs[2].axis('equal')  # Keeps the aspect ratio equal for x and y axes

plt.tight_layout()
plt.show()
