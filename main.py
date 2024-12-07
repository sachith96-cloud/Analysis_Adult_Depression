
import numpy as np
import pandas as pd

data = pd.read_csv('C:/Users/sachi/Downloads/bday/adult-depression-lghc-indicator-24.csv')
print (data.head())

import matplotlib.pyplot as plt
import seaborn as sns


subset_data = data[['Year', 'Strata', 'Strata Name', 'Percent']]


pivot_data = subset_data.pivot_table(index='Year', columns=['Strata', 'Strata Name'], values='Percent', aggfunc='mean')


plt.figure(figsize=(14, 8))
sns.heatmap(pivot_data, cmap='coolwarm', annot=True, fmt=".1f", cbar_kws={'label': 'Percent'})
plt.title('Relationship Between Year, Strata, and Strata Name on Depression Percentage')
plt.ylabel('Year')
plt.xlabel('Strata and Strata Name')
plt.tight_layout()
plt.show()


