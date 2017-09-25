import pandas as pd
import os.path
import matplotlib.pyplot as plt 
import urllib.request
import statsmodels.api as sm
import numpy as np
workdir = '/Users/michalurdanivia/Documents/Enseignement/UGA_M1_Econometrics_1_2017_2018/Lecture_3_Regression/'

url = "http://wps.aw.com/wps/media/objects/3254/3332253/datasets2e/datasets/Growth.dta"
if os.path.exists('/Users/michalurdanivia/Documents/Données/Données_cours/ Growth.dt') == False:
    urllib.request.urlretrieve(url,'/Users/michalurdanivia/Documents/Données/Données_cours/ Growth.dta')
    
growth = pd.read_stata("/Users/michalurdanivia/Documents/Données/Données_cours/ Growth.dta")
growth.head()
labels = growth['country_name']

Y = growth['growth']
X1 = growth['rgdp60']
X2 = growth['yearsschool']

plt.style.use('seaborn')
plt.scatter(X1, Y)
for i, label in enumerate(labels):
    plt.annotate(label, (X1.iloc[i], Y.iloc[i]))
plt.xlabel('rgdp60')
plt.ylabel('growth')
plt.title('Relationship between growth and gdp')
plt.savefig(workdir+'GrowthGDP_fig.pdf')
plt.show() 

plt.scatter(X2, Y)
for i, label in enumerate(labels):
    plt.annotate(label, (X2.iloc[i], Y.iloc[i]))
plt.xlabel('yearschool')
plt.ylabel('growth')
plt.title('Relationship between growth and education')
plt.savefig(workdir+'GrowthSchool_fig.pdf')
plt.show() 

X = sm.add_constant(X1)
lreg1 = sm.OLS(endog = Y, exog = X, missing ='drop')
type(lreg1)
results = lreg1.fit()
type(results)
print(results.summary())

meanX1 = np.mean(X1)
meanX1

results.predict(exog=[1, meanX1])

plt.scatter(X1, results.predict(), alpha = 0.5, label = 'predicted')

plt.scatter(X1, Y, alpha=0.5, label = 'observed')
plt.legend()
plt.title('OLS predicted values')
plt.xlabel('rgdp60')
plt.ylabel('growth')
plt.show()


