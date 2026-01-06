import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = ['sun', 'tue', 'mon', 'fri', 'web', 'sat', 'thu']

y = [6,2.7,1,8,4,3,5]

ax = sns.stripplot(x = x, y = y)

ax.set(xlabel = 'Days', ylabel = ' Values' )

plt.title('Daily Spending Values')

plt.show()