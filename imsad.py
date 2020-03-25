import numpy as np 
import matplotlib.pyplot as plt 
x = np.arange(0,10,0.1) 
y = np.sin(x)
plt.title("正弦信号")  
plt.plot(x, y) 
plt.show()