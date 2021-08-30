import numpy as np

v = np.array([2,3]) 
w = np.array([3,3])
vw = v+w
print(vw[:, np.newaxis])
#Example 1 Output
#[[5]
# [6]]

v = np.array([-2,-3])
w = np.array([3,3])
vw = v+w
print(vw[:, np.newaxis])
#Example 2 Output
#[[1]
# [0]]


v = np.array([2,3])
w = np.array([3,3])
vw = v-w
print(vw[:, np.newaxis])
#Example 3 Output
#[[-1]
# [0]]

v = np.array([-2,-3])
w = np.array([3,3])
vw = v-w
print(vw[:, np.newaxis])
#Example 4 Output
#[[-5]
# [-6]]

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def plot_vector2d(vector2d, s, origin=[0, 0], **options):
    plt.gca().annotate(f'{s}({vector2d[0]},{vector2d[1]})', (vector2d[0],vector2d[1]),fontsize=13)
    plt.scatter(vector2d[0],vector2d[1], s=5,c='black')
    return plt.arrow(origin[0], origin[1], vector2d[0], vector2d[1],
          head_width=0.2, head_length=0.3, length_includes_head=True,
          width=0.02, 
          **options)

figure(figsize=(8, 6), dpi=80)
v = np.array([4,2])
w = np.array([-1,2])
vw = v+w
plot_vector2d(v,'v', color='black')  #v
plot_vector2d(w,'w', color='black')  #w
plot_vector2d(vw, 'v+w', color='b') #v+w

vw = v-w
plot_vector2d(vw, 'v-w', color='r') #v-w

plt.axis([-5, 11, -2, 11])
plt.grid()
plt.gca().set_aspect("equal")

plt.show()



