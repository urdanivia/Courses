# Chargement des bibliothèques utilisées.

import numpy as np
import pandas as pd
import statsmodels.api as sm
import scipy as sp

# Répertoire où sont les données issues de l'enquête emploi 2012.

workdir =  '/Users/michalurdanivia/Google Drive/Enseignement/UGA/Econ_S2_UGA_M1_MIASH/Donnees/David_Card_NBER_1993/'

# Lecture des données.
"""
Remarque.
Les données sont celles utilisées par D. Card dans son travail "Using Geographic Variation in College Proximity 
to Estimate the Return to Schooling." 
Vous devez lire ce travail.

"""
card_data = pd.read_stata(workdir+'card.dta') 

# Réplication de certains résultats de D. Card.

## Tableau 2, colonne 1(page 34): MCO.

card_data['expersq100'] = card_data['expersq'] / 100
Y = card_data['lwage']
X = card_data[['educ', 'exper' , 'expersq100' , 'black' , 'south' , 'smsa' , 'smsa66', \
               'reg661' , 'reg662' , 'reg663' , 'reg664' , 'reg665' , 'reg666' , 'reg667',\
               'reg668']]

X = sm.add_constant(X) # On ajoute une constante.
param_names = [col for col in list(X)]

# Estimation de la régression par MCO.

# Matrice de variances-convariances robuste à l'hétéroscédasticité de White(1980).
lin_reg_ols = sm.OLS(Y, X).fit(cov_type='HC0')
print ('------------------------------------------------------------------------------')
print ('- Rendement des études: estimation par MCO                              ')
print ('------------------------------------------------------------------------------')
print ('')
print(lin_reg_ols.summary())


# Estimation de la régression par VIs.
"""
Dans cette partie nous allons d'abord définir une fonction permettant de calculer l'estimateur des VIs dans le cas
juste-identifié.
"""

def ivreg(Y, X, Z):
    # INPUTS:
    # Y = numpy array N x 1 pour la variable dépendante.
    # X = numpy array N x K pour le vecteur des régresseurs.
    # Z = numpy array N x J pour le vecteur d'instruments avec J==K).
    
    # OUTPUTS:
    # beta_hat = vecteur des paramètres estimés.
    # vcov_hat = matrice K x K des variances-covariances des paramètres estimés.
    
    K = X.shape[1]
    
    # Estimateur des VIs.
    ZZ = Z.T.dot(Z)
    iZZ = numpy.linalg.inv(ZZ)
    pZ = Z.dot(iZZ).dot(Z.T)
    beta_hat = numpy.linalg.inv(X.T.dot(pZ).dot(X)).dot(X.T.dot(pZ).dot(Y))
    
    # Matrice de variances-covariances robuste.
    U = Y - X.dot(beta_hat)
    XZU = (pZ.dot(X)) * (U.dot(np.ones((1, K))))
    iXZX = numpy.linalg.inv(X.T.dot(pZ).dot(X))
    vcov_hat = iXZX.dot(XZU.T).dot(XZU).dot(iXZX)
    
    beta_hat = beta_hat.reshape(-1)  
    
    return [beta_hat, vcov_hat]

## Estimation.

Z = card_data[['nearc4', 'exper' , 'expersq100' , 'black' , 'south' , 'smsa' , 'smsa66', \
               'reg661' , 'reg662' , 'reg663' , 'reg664' , 'reg665' , 'reg666' , 'reg667',\
               'reg668']]
Z = sm.add_constant(Z)
N = len(Y)
Y = np.array(Y).reshape(N, 1)
X = np.array(X).reshape(N,-1)
Z = np.array(Z).reshape(N,-1)
[beta_hat, vcov_hat] = ivreg(Y, X, Z)

## Affichage des résultats.

se_beta = np.sqrt(np.diag(vcov_hat))
iv_estim = {'beta':param_names, 'beta_hat':beta_hat, 'se':se_beta}
results = pd.DataFrame(iv_estim)
print('------------------------------------------------------------------------------')
print('- Rendement des études: Estimation par VIs -')
print('------------------------------------------------------------------------------')
print('')
print(results)

