import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('coding-practise/test_scripts/Test_CSV.csv', parse_dates=['timestamp'])

plt.figure(figsize=(10, 6))
for column in df.columns:
    if column != 'timestamp':
        plt.plot(df['timestamp'], df[column], label=column)

plt.xlabel('Timestamp')
plt.ylabel('Values')
plt.title('System Parameters Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
