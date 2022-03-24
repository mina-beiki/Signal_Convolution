from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

def convolution(x, h):
    x = np.concatenate([np.zeros((len(h)-1,)) , x , np.zeros((len(h)-1,))])
    h = h[::-1]
    y = np.zeros((len(x) - len(h) + 1,))
    for i in range(len(y)):
        y[i] = (np.sum(x[i:i+len(h)]*h))
    return y


#signal a:
# start = -10
# end = 10
# step = 0.01
# x1 = np.linspace(start, end, int((end - start)/step))
# y1 = np.heaviside(x1-10, 1) - np.heaviside(x1, 1)
# style.use('ggplot')
# plt.plot(x1, y1)
# plt.title('a')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.show()

#signal b:
# start1 = 0
# end1 = 4
# start2 = 5
# end2 = 10
# x1_2 = np.linspace(start1, end1, end1-start1+1)
# y1_2 = -x1-1
# x2_2 = np.linspace(start2, end2, end2-start2+1)
# y2_2 = np.power(x2_2, 2)
# style.use('ggplot')
# plt.stem(x1_2, y1)
# plt.stem(x2_2, y2)
# plt.title('2')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.legend()
# plt.show()

#part3:

n3 = np.arange(-10, 10, 1)
x3 = np.power(1/3, n3)*(np.heaviside(n3, 1)-np.heaviside(n3-10, 1))
h3 = np.power(0.9, n3)*(np.heaviside(n3-5, 1)-np.heaviside(n3, 1))
y3 = convolution(x3, h3)
y3 = y3[int(len(y3)/4) : -1 * int(len(y3)/4) -1]
style.use('ggplot')
plt.stem(n3, y3)
plt.title('Part 3')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()