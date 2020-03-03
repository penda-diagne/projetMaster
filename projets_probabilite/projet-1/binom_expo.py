from numpy.random import binomial
import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt
from scipy.stats import binom
plt.figure()
plt.subplot(2,2,1)
n, p, N = 20, 0.3, 50
X=np.random.binomial(n,p,N)
plt.bar(X,scs.norm.pdf(X,6))
plt.title("Densite de la loi Binomiale")

plt.subplot(2,2,2)
plt.bar(X,scs.norm.cdf(X,3))
plt.title("Fonction de répartition de la loi Binomiale")

Y=np.random.exponential(scale=2,size=300)
plt.subplot(2,2,3)
plt.hist(Y,normed=True,bins=15)
plt.title("Fonction de répartition de la loi exponentielle")

plt.subplot(2,2,4)
plt.step(np.sort(Y),np.arange(0,1,1./len(Y)))
plt.title("Fonction de répartition de la loi exponentielle")
plt.show()
