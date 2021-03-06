#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import pandas 

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()

x_1 = pandas.read_csv('http://pastebin.com/raw.php?i=ksM4FvZS', skiprows=2, header=None).values
y_1 = pandas.read_csv('http://pastebin.com/raw.php?i=0WhjjMkb', skiprows=2, header=None).values
fig, bx = plt.subplots()
bx.plot(x ,y)


# # Plotting a fast fourier transform using numpy and matplotlib

# In[ ]:




