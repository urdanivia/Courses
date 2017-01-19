# Chargement des bibliothèques utilisées.

import numpy as np
import pandas as pd
import statsmodels.api as sm

# Répertoire où sont les données issues de l'enquête emploi 2012.

workdir =  '/Users/michalurdanivia/Google Drive/Enseignement/UGA/Econ_S2_UGA_M1_MIASH/Donnees/eemploi2012/'

# Lecture des données.
"""
Remarque.
Les données sont un extrait de l'enquête emploi 2012 construit par le script "eemploi2012_s0.R".

"""
eedata = pd.read_csv(workdir+'eemploi2012_s0.csv') 
eedata.shape # dimensions du fichiers: nombre de lignes/observations x nombre de colonnes/variables.

# Sélection d'un échantillon pour travailler.

"""
Remarque.
Pour comprendre les différentes variables vous devez vous reporter aux dictionnaire
correspondant à l'enquête emploi 2012, et au script R utilisé pour construire plusieurs 
d'entre elles.

"""

## On considère les individus en emploi.
eedata = eedata[['DDIPL1' , 'DDIPL3' , 'DDIPL4' , 'DDIPL5' , 'DDIPL6', 'DDIPL7','SEXE2', 'SEXE1', \
                 'ANCENTR41' , 'ANCENTR42', 'ANCENTR43', 'ANCENTR44', 'AG', \
                 'lsalhor' ]][eedata.ACTEU1 == 1]
eedata.shape
eedata.head() # Premières lignes.
eedata.describe() # Quelques statistiques descriptives.

# Regression linéaire.
"""
Nous allons commencer par la régression linéaire du log du salaire sur les indicatrices du diplôme, 
du sexe, de l'experience, et de l'ancienneté.
"""
eedata['AG2'] = np.log(eedata.AG) # Expérience au carré.

Y    = eedata['lsalhor'] # Régressande.
X    = eedata[['DDIPL1' , 'DDIPL3' , 'DDIPL4' , 'DDIPL5' , 'DDIPL6', 'SEXE2', \
              'ANCENTR42', 'ANCENTR43', 'ANCENTR44', 'AG', 'AG2']] # Régresseurs.
X = sm.add_constant(X) # On ajoute une constante.

# Estimation de la régression par MCO.
# Matrice de variances-convariances robuste à l'hétéroscédasticité de White(1980).
lin_reg_ols = sm.OLS(Y, X).fit(cov_type='HC0')
print ('------------------------------------------------------------------------------')
print ('- Régression linéaire pour le log du salaire                                  ')
print ('------------------------------------------------------------------------------')
print ('')
print(lin_reg_ols.summary())


