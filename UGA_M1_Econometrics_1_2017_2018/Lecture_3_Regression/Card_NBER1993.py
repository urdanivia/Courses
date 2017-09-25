import pandas as pd
import os.path
import matplotlib.pyplot as plt 
import urllib.request
import statsmodels.api as sm

workdir = '/Users/michalurdanivia/Documents/Enseignement/UGA_M1_Econometrics_1_2017_2018/Lecture_3_Regression/'

url = "http://fmwww.bc.edu/ec-p/data/wooldridge/card.dta"
if os.path.exists('/Users/michalurdanivia/Documents/Données/Données_cours/ Card.dta') == False:
    urllib.request.urlretrieve(url,'/Users/michalurdanivia/Documents/Données/Données_cours/Card.dta')
    
card = pd.read_stata("/Users/michalurdanivia/Documents/Données/Données_cours/Card.dta")
card.head()
card.describe()

card['const'] = 1
lreg = sm.OLS(endog = card['lwage'], exog = card[['const', 'educ']], missing = 'drop')
results = lreg.fit()
print(results.summary())

# Plot fitted values
plt.scatter(card['educ'], results.predict(), alpha=0.5, label = 'fitted')

plt.scatter(card['educ'], card['lwage'], alpha=0.5, label = 'observed')
plt.legend()
plt.title('OLS fitted values')
plt.xlabel('educ')
plt.ylabel('lwage')
plt.savefig(workdir+'lreg_CardEducWage.pdf')
plt.show()


