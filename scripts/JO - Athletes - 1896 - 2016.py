import pandas as pd
import numpy as np 

# Chargement du CSV
JO = pd.read_csv('Projet JO/athlete_events.csv.csv')
print(JO.head())

# Vérification des données 
print(JO.info())
# Comme vu sur le Excel nous avons 27116 lignes et 15 colonnes 
# avec des problèmes dans les colonnes Age, Height, Weight et Medal

# Changement noms des colonnes 
JO.columns = ["ID", "Nom", "Sexe", 'Age', 'Taille', 'Poids', 'Pays', 'NOC', 'Jeux',
       'Année', 'Saison', 'Lieu', 'Sport', 'Discipline', 'Medailles']
print(JO.info())

# Regardons si nous avons des homonymes (même nom pour ID différent)
doublons_nom = JO.groupby("Nom")["ID"].nunique()
doublons_nom = doublons_nom[doublons_nom > 1]

print(f"{len(doublons_nom)} athlètes ont plusieurs IDs :") 
# Nous avons donc 713 homonymes (information à garger en mémoire) ! ID ne nous servira pas de clé unique !

# Maintenant on s'interesse aux valeurs manquantes des colonnes : 'Age', 'Taille', 'Poids', 'Médailles
colonnes_cibles = ['Age', 'Taille', 'Poids', 'Medailles']
for col in colonnes_cibles:
    pourcentage = JO[col].isnull().mean() * 100
    print(f"{col} : {pourcentage:.2f}% de valeurs manquantes")

# Pour les médailles nous remplaçons les valeurs manquantes par un simple tiret (-)
JO['Medailles'] = JO['Medailles'].fillna('-')
print(JO["Medailles"].unique())

# Age = 3.49% de valeurs manquantes ; Taille : 22.19% ; Poids : 23.19% de valeurs manquantes
print("Valeurs manquantes: \n", JO[['Age', 'Taille', 'Poids']].isnull().sum())

#Comme nous avons beaucoup de valeurs manquantes nous ne pouvons pas supprimer les lignes
#Nous complétons les éléments manquants par la moyenne d'âge par Discipline

age_sport = JO.groupby('Discipline')['Age'].transform('mean')
JO['Age'] = JO['Age'].fillna(age_sport)

print("Valeurs manquantes après imputation :\n", JO[['Age']].isnull().sum()) 

#Il nous reste 142 valeurs manquantes pour les Age, 2083 pour la taille et 4660 pour le poids
colonnes_cibles = ['Age', 'Taille', 'Poids']
for col in colonnes_cibles:
    pourcentage = JO[col].isnull().mean() * 100
    print(f"{col} : {pourcentage:.2f}% de valeurs manquantes")
print(JO[['Age']].describe())

#Vérification sur internet : 
# il existe bien un athetle ayant 10 ans (en 1896 maintenant le règlement a évolué)
# l'age maximal de participation au JO semble être de 72 ans nous allons chercher qui est l'individu ayant eu 97 ans

# Afficher les 5 personnes les plus âgées
print(JO.sort_values(by='Age', ascending=False)[['Nom','Age','Sport']].head(5))

#Nous venons de voir qu'il a eu une compétition d'art pendant les JO, sur une idée de coubertin etc... afficher dans le README
#Je décide de supprimer toutes les lignes où le sport est "Art Competitions"  
JO = JO[JO['Sport'] != 'Art Competitions']
print(JO.sort_values(by='Age', ascending=False)[['Nom','Age','Sport']].head(5))
#L'âge maximal est bien de 72 ans (source internet, hors compétition d'art)

#Passons aux colonnes Taille et Poids, dont nous allons  
#Nous allons arrondir à la première décimal tous les résultats 
JO['Taille'] = JO['Taille'].round(1)
JO['Poids'] = JO['Poids'].round(1)

#Source vérifiable sur internet du poids et de la taille minimal et maximal de participants aux JO
print(JO.sort_values(by='Poids', ascending=False)[['Nom','Poids','Sport']].head(5))
print(JO.sort_values(by='Taille', ascending=False)[['Nom','Taille','Sport']].head(5))
#Les valeurs sont bonnes à +- 4/5 unités en fonction des donnes trouvées topendsports.com
print(JO.sort_values(by='Poids', ascending=True)[['Nom','Poids','Sport']].head(5))
print(JO.sort_values(by='Taille', ascending=True)[['Nom','Taille','Sport']].head(5))
#Les valeurs sont bonnes à +- 4/5 unités en fonction des donnes trouvées sur topendsports.com

#Nous allons donc effectuer des moyenne par discipline pour les athlètes dont le poids et la taille ne sont pas renseigné
JO['Taille'] = JO['Taille'].fillna(JO.groupby('Discipline')['Taille'].transform('mean'))
JO['Poids'] = JO['Poids'].fillna(JO.groupby('Discipline')['Poids'].transform('mean'))
print("Valeurs manquantes après imputation :\n", JO[['Taille', 'Poids']].isnull().sum())
print(JO[JO['Taille'].isnull() | JO['Poids'].isnull()][['Nom', 'Discipline', 'Taille', 'Poids']])

colonnes_cibles = ['Age', 'Taille', 'Poids']
for col in colonnes_cibles:
    pourcentage = JO[col].isnull().mean() * 100
    print(f"{col} : {pourcentage:.2f}% de valeurs manquantes")

#Nous avons maintenant Age : 0.05% de valeurs manquantes ; Taille : 0.48% de valeurs manquantes ; Poids : 1.47% de valeurs manquantes

#Nous allons créer une colonnes pour identifier les lignes où les données sont complètes :
JO['Donnees_completes'] = (~JO['Age'].isnull()) & (~JO['Taille'].isnull()) & (~JO['Poids'].isnull())
print(JO['Donnees_completes'].value_counts())

# Passons à la partie vérification et traduction de la colonne sport
# Liste unique et triée des sports
nb_sports = JO['Sport'].value_counts().sum()
print(f"Nous avons {JO['Sport'].nunique()} sports différents") #avant traduction

sports_uniques = sorted(JO['Sport'].unique())
for sport in sports_uniques:
    print(sport)
trad_sport = {
       'Aeronautics' : 'Aéronautique', # Il y a eu une remise de médaille d'or en 1936 pour un aviateur Suisse, on ne garde pas cette information
       'Alpine Skiing' : 'Ski Alpin',
       'Alpinism' : 'Alpinisme',
       'Archery' : "Tir à l'arc",
       'Athletics': 'Athlétisme',
       'Basque Pelota' : 'Pelote Basque', # Il y a eu qu'une seule édition en 1900 pour les JO de Paris (on ne garde pas car nous avons que le nom des gagnants)
       'Boxing' : 'Boxe',
       'Canoeing' :'Canoë-kayak',
       'Cricket' :'Cricket',  # Il y a eu qu'une seule édition en 1900 pour les JO de Paris (on ne garde pas car nous avons que le nom des gagnants)
       'Croquet' : 'Croquet',  # Il y a eu qu'une seule édition en 1900 pour les JO de Paris (on ne garde pas car nous avons que le nom des gagnants)
       'Cross Country Skiing': 'Ski de fond',
       'Cycling' : 'Cyclisme',
       'Diving' : 'Plongeon',
       'Equestrianism': 'Sports équestres',
       'Fencing': 'Escrime',
       'Figure Skating': 'Patinage artistique',
       'Freestyle Skiing': 'Ski acrobatique',
       'Gymnastics':'Gymnastique',
       'Hockey' : 'Hockey sur gazon',
       'Ice Hockey' : 'Hockey sur glace',
       'Jeu De Paume' : 'Jeu de Paume', # Il y a eu qu'une seule édition en 1908 pour les JO de Londres (on ne garde pas car nous avons que le nom des gagnants)
       'Judo': 'Judo',
       'Lacrosse' : 'Crosse', 
       'Military Ski Patrol' : 'Ski militaire', #Ancetre du Biathlon, une édition au JO d'hiver 1924
       'Modern Pentathlon': 'Pentathlon moderne',
       'Motorboating' : 'Motonautisme', # Il y a eu qu'une seule édition en 1908 pour les JO de Londres (on ne garde pas car nous avons que le nom des gagnants)
       'Nordic Combined': 'Combine nordique',
       'Racquets' : 'Jeu de raquettes', #intermédiraire entre tennis et squash à eu lieu qu'au JO de Londres 1908
       'Rhythmic Gymnastics': 'Gymnastique rythmique',
       'Roque': 'Roque', #Variante americaine du croquet a eu lieu aux JO de St Louis USA en 1904
       'Rowing': 'Aviron',
       'Rugby': 'Rugby',
       'Rugby Sevens' : 'Rubgy à 7',
       'Sailing': 'Voile',
       'Shooting': 'Tir sportif',
       'Short Track Speed Skating': 'Patinage de vitesse sur courte piste',
       'Skeleton': 'Skeleton',
       'Ski Jumping': 'Saut à ski',
       'Snowboarding': 'Snowboard',
       'Softball': 'Softball',
       'Speed Skating': 'Patinage de vitesse',
       'Swimming': 'Natation',
       'Synchronized Swimming': 'Natation synchronisée',
       'Table Tennis': 'Tennis de table',
       'Taekwondo': 'Taekwondo',
       'Tennis': 'Tennis',
       'Trampolining': 'Trampoline',
       'Triathlon': 'Triathlon',
       'Tug-Of-War': 'Tir à la corde',
       'Volleyball': 'Volley-ball',
       'Water Polo': 'Water-polo',
       'Weightlifting': 'Haltérophilie',
       'Wrestling': 'Lutte',
}
JO['Sport'] = JO['Sport'].replace(trad_sport)

#verification : 
sports_uniques = sorted(JO['Sport'].unique())
for sport in sports_uniques:
    print(sport)
nb_sports = JO['Sport'].value_counts().sum()
print(f"Nous avons {JO['Sport'].nunique()} sports différents") #après traduction

#le résultat est bon nous avons toujours 65 sports

#Passons maintetant à la traduction des diciplines : 
print(f"Nous avons {JO['Discipline'].nunique()} disciplines différentes")
#Nous avons 736 nom de disciplines différentes, je décide de ne pas traduire tout de suite 

#Avant d'exporter vers SQL nous allons créer une clé unique que l'on nommera cle
JO["cle"] = (
    JO["ID"].astype(str) + "_" +
    JO["Année"].astype(str) + "_" +
    JO["Discipline"] + "_" +
    JO["Sexe"]
)
print(JO['cle'].value_counts())

print(f"Nous avons {JO['NOC'].nunique()} NOC différentes")

print(JO.info())
JO.to_csv(r"C:\Users\Sebas\Desktop\DA - Projet - Dataset JO\olympics_clean.csv", index=False)