import seaborn as sb
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
print("WE BE FINDING HOUSE RENT WITH THIS ONE🗣️🗣️🗣️🔥🔥🔥")
fil = pd.read_csv("USA_Housing.csv")
fil.head(10)
fil.info()
fil.describe()
fil.columns
sb.pairplot(fil)
sb.heatmap(fil)
plt.show()
