# Chargement des bibliothèques qui seront utilisées.
import pandas as pd
import os.path
import matplotlib.pyplot as plt 
import urllib.request
import statsmodels.api as sm
import numpy as np

# Espace de travail.

workdir = '/Users/michalurdanivia/Documents/Enseignement/UGA_M1_Econometrics_1_2017_2018/Lecture_3_Regression/'

# Téléchargement des données si elle ne le sont pas encore dans le chemin ci-dessous.

url = "http://economics.mit.edu/files/1358"
if os.path.exists('/Users/michalurdanivia/Documents/Données/Données_cours/ AngristLavyQJE1999.dta') == False:
    urllib.request.urlretrieve(url, "/Users/michalurdanivia/Documents/Données/Données_cours/AngristLavyQJE1999.dta")

# Chargement des données qui sont au format Stata(extension "dta") comme "DataFrame" Pandas.    

aldat = pd.read_stata("/Users/michalurdanivia/Documents/Données/Données_cours/AngristLavyQJE1999.dta")
aldat.head() #Affichage des première lignes.
aldat.describe() # Quelques statistiques descriptives.


# Corrections faites sur les données.

## Correction des résultats supérieurs à 100.
aldat['avgmath'][(aldat['avgmath'] > 100) & (aldat['avgmath'].isnull() == False)] = \
aldat['avgmath'][(aldat['avgmath'] > 100) & (aldat['avgmath'].isnull() == False)] - 100
aldat['avgverb'][(aldat['avgverb'] > 100) & (aldat['avgverb'].isnull() == False)] = \
aldat['avgverb'][(aldat['avgverb'] > 100) & (aldat['avgverb'].isnull() == False)] - 100

## Suppression des observations(lignes) avec des tailles nulles et pourtant des résultats renseignés.
aldat['avgmath'][(aldat['mathsize'] == 0)] = np.nan
aldat['avgverb'][(aldat['verbsize'] == 0 )]= np.nan

## Suppression des observations(lignes) relatives aux faibles inscriptions(telles que "c_size < 5").
aldat = aldat[aldat.c_size >= 5]

## Suppression des observations(lignes) relatives aux tailles des classes de plus de 45(telles que "classize >= 45"),
## la taille légale ne pouvant pas dépasser 40.
aldat = aldat[aldat.classize < 45]

## Suppression des observations(lignes) avec résultats non renseignés.
aldat = aldat[(aldat.avgmath.isnull() == False) & (aldat.avgverb.isnull() == False)]

# Statistiques descriptives.

## Façon rapide mais sans quelques quantiles.
aldat[['classize','c_size','tipuach', 'verbsize','mathsize', 'avgverb', 'avgmath']].describe()

## Tableau avec moyennes.
aldat_mean = aldat[['classize','c_size','tipuach', 'verbsize','mathsize', 
                    'avgverb', 'avgmath']].mean()

## Tableau avec écart-types
aldat_std = aldat[['classize','c_size','tipuach', 'verbsize','mathsize',
                   'avgverb', 'avgmath']].std()

## Tableau avec quantiles.
aldat_quants = aldat[['classize','c_size','tipuach', 'verbsize','mathsize',
                      'avgverb', 'avgmath']].quantile([0.1, 0.25, 0.5, 0.75, 0.9])

## Tableau avec moyennes, écart-types, quantiles.
tab1 = pd.concat([aldat_mean, aldat_std, aldat_quants.T], axis = 1)

## On change le nom des deux premières colonnes.
tab1.rename(columns={0.00: 'Mean', 1.00: 'Std'})

## Tableau "latex".
tab1.to_latex()

# Régressions.

## Regression des résultats en mathématiques(variable "avgmath") sur la taille de 
## classes(variable "classize")

## On ajoute une constante au données.
aldat["const"] = 1
## On utilise la fonction OLS dans Statsmodels.
lreg_avmath = sm.OLS(endog = aldat['avgmath'], exog = aldat[['const', 'classize']], missing = 'drop')
## Ci-dessus le modèle a été construit. Pour l'estimer on utilise ".fit()" ci-après:
results = lreg_avmath.fit()
## Pour avoir un résumé des résultats on peut utiliser ".summary()" comme ici:
print(results.summary())

