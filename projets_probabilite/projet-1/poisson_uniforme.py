from numpy.random import binomial
import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt
plt.figure()
plt.subplot(2,2,1)
a, b, n = 0, 10, 50
X=range(0,6)
plt.bar(X,scs.poisson.pmf(X,0.5))
plt.title("Densite de la loi de poisson")

plt.subplot(2,2,2)
plt.step(X,scs.poisson.cdf(X,6))
plt.title("Fonction de répartition de la loi poisson")

plt.subplot(2,2,3)
X=np.random.uniform(low=a,high=b,size=n)
plt.bar(X,scs.uniform.pdf(X,6))
plt.title("Densite de la loi uniforme")

plt.subplot(2,2,4)
plt.bar(X,scs.uniform.cdf(X,6))
plt.title("Fonction de répartition de la loi uniforme")

plt.show()
