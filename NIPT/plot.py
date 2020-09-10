import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

mu = 0.999
sigma = 0.001
# csigma = sigma * np.sqrt((100)
fig = plt.figure()
pp = fig.add_subplot(1,1,1)
pp.axvline(x=mu, color='r')

tmpx = np.linspace(mu - 3*sigma, mu+3*sigma,100)
tmpy = stats.norm.pdf(tmpx, mu, sigma)
plt.plot(tmpx, tmpy)

plt.show()