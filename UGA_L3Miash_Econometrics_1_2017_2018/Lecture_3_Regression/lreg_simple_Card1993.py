import pandas as pd
import numpy as np
import urllib.request
import os.path

# As an example we use Card's 1993 data.
url = "http://fmwww.bc.edu/ec-p/data/wooldridge/card.dta"
if os.path.exists('/Users/michalurdanivia/Documents/Données'
                  r'/Données_cours/ Card.dta') == False:
                     urllib.request.urlretrieve(url,
                     '/Users/michalurdanivia/Documents/Données
                     r'/Données_cours/Card.dta')

card = pd.read_stata("/Users/michalurdanivia/Documents/Données"
                     r"/Données_cours/Card.dta")
card.head() # First rows
card.describe() # Some summary statistics of data.

beta1  = card.lwage.cov(card.educ) / card.educ.cov(card.educ)
beta0 = np.mean(card.lwage) - beta1 * np.mean(card.educ)
beta1
beta0
