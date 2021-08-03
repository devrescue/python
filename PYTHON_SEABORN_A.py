import seaborn as sns
import pandas as pd

d = {'YEARS': ['2008','2009','2010','2011','2012'], 
     'SALES': [20000,25000,30000,19000,35000] }

df = pd.DataFrame(data=d)
sns.set_theme(style="whitegrid", rc={'figure.figsize':(11.7,8.27)})
ax = sns.barplot(x="YEARS", y="SALES", data=df)

for p in ax.patches:
    ax.annotate(f"{p.get_height()}", 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')
                   

import matplotlib.pyplot as plt
plt.show()