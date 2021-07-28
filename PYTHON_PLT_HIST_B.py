import matplotlib.pyplot as plt
import pandas as pd
  
d = {'CLASS_TYPE': ['A','B','C','D','E'], 'MEN': [20,25,30,19,38], 'WOMEN': [21,31,55,22,39]}

df = pd.DataFrame(data=d)


classType = df["CLASS_TYPE"]
men_count = df["MEN"]
women_count = df["WOMEN"]
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

ax = fig.add_axes([0,0,1.5,1.5])

ax.bar(classType, men_count, width, label='Men')
ax.bar(classType , women_count, width, bottom=men_count, label='Women')

ax.set_ylabel('Count')
ax.set_xlabel('Classes')
ax.set_title('Count of Classes By Gender')
ax.legend()

for x,y1,y2 in zip(classType,women_count,men_count):

    label = "{:.2f}".format(y1)

    plt.annotate(label, # label text
                 (x,y1), #  The point (x, y) to annotate
                 textcoords="offset points", # offset (in points) from the xy value
                 xytext=(0,6), # position (x, y) to place the text at. 
                 ha='center') # horizontal alignment is center in this case
    
    label = "{:.2f}".format(y2)

    plt.annotate(label, # label text
                 (x,y2), #  The point (x, y) to annotate
                 textcoords="offset points", # offset (in points) from the xy value
                 xytext=(0,-14), # position (x, y) to place the text at. 
                 ha='center') # horizontal alignment is center in this case

    label = "{:.2f}".format(y1+y2)

    plt.annotate(label, # label text
                 (x,y1+y2), #  The point (x, y) to annotate
                 textcoords="offset points", # offset (in points) from the xy value
                 xytext=(0,9), # position (x, y) to place the text at. 
                 ha='center') # horizontal alignment is center in this case

plt.show()