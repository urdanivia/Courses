import pandas as pd
import os.path
import matplotlib.pyplot as plt 
import urllib.request
import statsmodels.api as sm


workdir = '/Users/michalurdanivia/Documents/Enseignement/UGA_L3Miash_Econometrie_1/TDs/TD_27092017/'

url = "http://fmwww.bc.edu/ec-p/data/wooldridge/bwght.dta"
if os.path.exists('/Users/michalurdanivia/Documents/Données/Données_cours/bwght.dta') == False:
    urllib.request.urlretrieve(url,'/Users/michalurdanivia/Documents/Données/Données_cours/bwght.dta')
    
bwght = pd.read_stata("/Users/michalurdanivia/Documents/Données/Données_cours/bwght.dta")
bwght.head()

beta1  = bwght.bwght.cov(bwght.cigs) / bwght.cigs.cov(bwght.cigs)
beta1
beta0 = np.mean(bwght.bwght) - beta1 * np.mean(bwght.cigs)
beta0
