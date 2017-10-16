import matplotlib.pyplot as plt 
import numpy as np

workdir = '/Users/michalurdanivia/Documents/Enseignement/UGA_M1_Econometrics_1_2017_2018/Lecture_3_Regression/'

# Non linear CEF.
def cef(X):
    cef = np.exp(X) / (1 + np.exp(X)) ## True CEF
    return cef

N = 1000
X = np.random.normal(0, 1, N) * 5
U = np.random.normal(0, 1, N) * 0.1
cefyx = cef(X)
Y = cefyx + U

plt.scatter(X, Y)
plt.plot(np.unique(X), np.unique(cefyx), color='black')
plt.plot(np.unique(X),
         np.poly1d(np.polyfit(X, Y, 1))(np.unique(X)),
         color='black')

plt.savefig(workdir+'nonlinearCEF.pdf')
plt.show()
