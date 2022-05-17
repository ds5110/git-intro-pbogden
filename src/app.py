import pandas as pd
import matplotlib.pyplot as plt

# Get the "raw" URL from github
url = "https://raw.githubusercontent.com/ds5110/rdata/main/data/Wage.csv"

# Load the CSV into a pandas DataFrame
df = pd.read_csv(url)

# Create the scatterplot
df.plot.scatter('age', 'wage')

plt.title("Scatterplot of the wage dataset")
plt.savefig("figs/fig.png")
plt.show()
