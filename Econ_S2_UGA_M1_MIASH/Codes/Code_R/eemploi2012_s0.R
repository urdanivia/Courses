#########################Construction de l'échantillon utilisé dans le cours###########################.

library(dplyr)
library(dummies)
library(dae)
# Lecture des données issues de l'enquête emploi 2012.

eemploi2012 <- read.csv("/Users/michalurdanivia/Google Drive/Enseignement/UGA/Econ_S2_UGA_M1_MIASH/Donnees/eemploi2012/eemploi2012.csv")
dim(eemploi2012)

# On sélectionne des variables.

data <- select(eemploi2012, ACTEU, SEXE, DDIPL, FORDAT, MATRI, TYPMEN5, ZUS, REG, 
                      AG, AGQ, AGEQ,AGE, AG5,
                      NBENF3, NBENF6, NBENF18, SALRED, NBHEUR, NATPERC, 
                      NATMERC, PAIPERC,PAIMERC,TRIM, RGI, IDENT, NOI, TRIM, DIP, DIP11,  CONTRA,
                      CSER, CSPM, CSPP, ANNEE, CHPUB, NAFG4N, ANCENTR4)
dim(data)

# On sélectionne des observations.

data <- filter(eemploi2012, is.na(ACTEU) == FALSE, is.na(TYPMEN5) == FALSE, 
               is.na(NBENF3) == FALSE, is.na(NBENF6) == FALSE, is.na(SEXE) == FALSE, RGI == 1,
               is.na(ZUS) == FALSE, is.na(REG) == FALSE, is.na(NATMERC) == FALSE, is.na(NATPERC) == FALSE, 
               is.na(AGE) == FALSE, AG5 != 60, (is.na(ANCENTR4) == FALSE & ACTEU == 1) | ACTEU != 1,
               (is.na(CHPUB) == FALSE & ACTEU == 1) | (is.na(CHPUB) == TRUE & ACTEU != 1),
               is.na(NBENF18) == FALSE, is.na(FORDAT) == FALSE,
               is.na(DDIPL) == FALSE, is.na(DIP11) == FALSE, is.na(DIP) == FALSE,
               is.na(CSPP) == FALSE, is.na(CSPM) == FALSE,
               (ACTEU != 1 | (ACTEU == 1 & is.na(SALRED) == FALSE 
                              & is.na(NBHEUR) == FALSE & NBHEUR > 0 & SALRED > 0))
               )
dim(data)

# On construit des variables.

## Logarithme du salaire horaire.

data$lsalhor <- ifelse((data$SALRED != 0 & data$NBHEUR != 0 & is.na(data$SALRED) == FALSE 
                        & is.na(data$NBHEUR) == FALSE), log(data$SALRED / data$NBHEUR), NA)

## Expérience.

data$adfe <- data$FORDAT - (2012 - data$AG)
data$exper <- data$AG - data$adfe

## On regroupe des modalités.

data$NBENF6B <- ifelse(data$NBENF6 >= 2, 2, data$NBENF6)
data$NBENF3B <- ifelse(data$NBENF3 >= 2, 2, data$NBENF3)

## Indicatrices associées aux modalités des variables qualitatives.

acteu <- dummy(data$ACTEU)
ag5 <- dummy(data$AG5)
zus <- dummy(data$ZUS)
typmen5 <- dummy(data$TYPMEN5)
nbenf3 <- dummy(data$NBENF3)
nbenf6 <- dummy(data$NBENF6)
ddipl <- dummy(data$DDIPL)
dip <- dummy(data$DIP)
dip11 <- dummy(data$DIP11)
contra <- dummy(data$CONTRA)
chpub <- dummy(data$CHPUB)
sexe <- dummy(data$SEXE)
cser <- dummy(data$CSER)
ancentr4 <- dummy(data$ANCENTR4)
trim <- dummy(data$TRIM)
reg <- dummy(data$REG)
cspp <- dummy(data$CSPP)
cspm <- dummy(data$CSPM)
nbenf6b <- dummy(data$NBENF6B)
nbenf3b <- dummy(data$NBENF3B)
enf6typmen <- fac.combine(list(as.factor(data$TYPMEN5), as.factor(data$NBENF6B)), 
                          combine.levels = TRUE, sep = '')
enf6typmen <- dummy(enf6typmen)
enf3typmen <- fac.combine(list(as.factor(data$TYPMEN5), as.factor(data$NBENF3B)), 
                          combine.levels = TRUE, sep = '')
enf3typmen <- dummy(enf3typmen)
regzus <- fac.combine(list(as.factor(data$REG), as.factor(data$ZUS)), combine.levels = TRUE, sep = '')
regzus <- dummy(regzus)

# Sauvegarde des données.
data <- data.frame(data, acteu, ag5, zus, typmen5, nbenf3, nbenf6, ddipl, dip, dip11, 
                   contra, chpub, sexe, cser, ancentr4, trim, reg, cspp, cspm,
                   nbenf6b, nbenf3b, enf6typmen, enf3typmen, regzus)

write.csv(data, '/Users/michalurdanivia/Google Drive/Enseignement/UGA/Econ_S2_UGA_M1_MIASH/Donnees/eemploi2012/eemploi2012_s0.csv')
