import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("scores.csv")
plt.figure()
plt.scatter(df.index, df['math'], label='Math')
plt.scatter(df.index, df['python'], label='Python')
plt.scatter(df.index, df['database'], label='Database')
plt.title("Student Scores")
plt.xlabel("Student Index")
plt.ylabel("Scores")
plt.legend()
plt.savefig("scattered.png")
plt.show()
df[['math', 'python', 'database']].plot(
    kind='hist', 
    subplots=True, 
    figsize=(8, 6),
    title="Histogram"
)
plt.savefig("histo.png")
plt.show()
plt.figure()
df[['math', 'python', 'database']].boxplot()

plt.title("Box")
plt.ylabel("Scores")
plt.savefig("box.png")
plt.show()