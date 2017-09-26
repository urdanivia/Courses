import matplotlib.pyplot as plt 
import numpy as np

workdir = '/Users/michalurdanivia/Documents/Enseignement/UGA_M1_Econometrics_1_2017_2018/Lecture_3_Regression/'

# E(U|X) \neq 0.

N = 1000
X = np.random.normal(0, 1, N) 
U = np.sqrt(0.5) * np.random.normal(0, 1, N) + np.sqrt(0.5) * X
Y = X + U


plt.scatter(X, Y)
plt.plot(np.unique(X), np.unique(X), color='black')
plt.plot(np.unique(X),
         np.poly1d(np.polyfit(X, Y, 1))(np.unique(X)),
         color='red')

plt.savefig(workdir+'endogenousX.pdf')
plt.show()
