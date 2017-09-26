import matplotlib.pyplot as plt 
import numpy as np

workdir = '/Users/michalurdanivia/Documents/Enseignement/UGA_M1_Econometrics_1_2017_2018/Lecture_3_Regression/'

N = 1000
X = np.random.uniform(0, 1, N) * 5
U = np.random.normal(0, 1, N)
Y = 0.25 + 0.5 * X + U * 0.25

plt.style.use('seaborn')
plt.scatter(X, Y)
plt.plot(np.unique(X),
         np.poly1d(np.polyfit(X, Y, 1))(np.unique(X)),
         color='red')

plt.savefig(workdir+'lreg_homoskedastic.pdf')
plt.show()

