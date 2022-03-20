import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] =  'serif'

# option strike
k = 8000

# graphical output
s = np.linspace(7000, 9000, 100) # index level values
h = np.maximum(s - k, 0) # inner values of call options

plt.figure()
plt.plot(s, h, lw=2.5) # plot inner values at maturity
plt.xlabel('index level $s_t$ at maturity')
plt.ylabel('inner value of european call option')
plt.grid(True)
plt.show() # test
