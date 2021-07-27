import matplotlib.pyplot as plt
import pandas as pd
  
df = pd.DataFrame({'CLASS_TYPES': ['A','A','A','B','B',
       'C','C','C','D','E',
       'E','F','F','F','F',
       'G','G','G','G','G']})

fig = plt.figure()
ax = fig.add_axes([0,0,1.5,1.5])
classTypes = ['A','B','C','D','E','F','G']
classCount = [len(df[df.CLASS_TYPES == 'A']),
              len(df[df.CLASS_TYPES == 'B']),
              len(df[df.CLASS_TYPES == 'C']),
              len(df[df.CLASS_TYPES == 'D']),
              len(df[df.CLASS_TYPES == 'E']),
              len(df[df.CLASS_TYPES == 'F']),
              len(df[df.CLASS_TYPES == 'G'])]

ax.bar(classTypes,classCount,color=['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#ffc6ff','#9bf6ff','#a0c4ff'])

for x,y in zip(classTypes,classCount):

    label = "{:.2f}".format(y)

    plt.annotate(label, # label text
                 (x,y), # label position
                 textcoords="offset points", # offset (in points) from the xy value
                 xytext=(0,10), # position (x, y) to place the text at. 
                 ha='center') # horizontal alignment is center in this case
            
plt.show()