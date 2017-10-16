# Chargement des bibliothèques utilisées.
import pandas as pd
import numpy as np
import urllib.request
import os.path
import statsmodels.api as sm
# On télécharge les données dans un répertoire.
url = "http://fmwww.bc.edu/ec-p/data/wooldridge/card.dta"
os.path.exists("/Users/michalurdanivia/Documents/Données/Données_cours/Card.dta") == False:
     urllib.request.urlretrieve(url, "/Users/michalurdanivia/Documents/Données/Données_cours/Card.dta")
# On lit les données comme un DataFrame Pandas.
card = pd.read_stata("/Users/michalurdanivia/Documents/Données"
                     r"/Données_cours/Card.dta")
card.shape # Dimensions(lignes x colonnes)
card.head() # Les premières lignes pour avoir une idée.
card.describe() # Quelques statistiques descriptives.

# On calcule beta et alpha suivant les formules dans le cours:
# beta_hat  = C(lwage, educ)/ V(educ), alpha_hat = Ybar - beta_hatXbar
beta_hat  = card.lwage.cov(card.educ) / card.educ.cov(card.educ)
beta_hat
alpha_hat = np.mean(card.lwage) - beta_hat * np.mean(card.educ)
alpha_hat

