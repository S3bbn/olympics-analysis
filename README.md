# 🏅 120 ans d'histoire des Jeux Olympiques – Analyse et Visualisation

## Contexte
Ce projet analyse l’évolution des Jeux Olympiques modernes (1896 – 2016), en croisant les données des Jeux d’été et d’hiver.  
Dataset original : [120 years of Olympic history: athletes and results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) – publié sur Kaggle en mai 2018.

## Projet : 
Nous allons analyser l’évolution des Jeux Olympiques modernes entre Athènes 1896 et Rio 2016.  
Le dataset regroupe les jeux olympiques d’hiver et d’été. A noter qu’avant 1992, les jeux d’hivers et avait lieu la même année et tous les 4 ans. 

Passionné par le sport et notamment les Jeux olympiques que je regardais assidument plus jeune j’ai décidé de m’intéresser de plus prêt aux résultats, pays membres participants, place de la femme au sein des JO. 
Car cette compétition est une « vitrine » à travers laquelle nous retrouvons l'histoire mondiale : 
- la géopolitique mondiale, 
- l’évolution de la place des femmes dans le sport 
- des valeurs sociétales. 

Nous allons mettre en lumière les grandes tendances de l'histoire olympique. 

Puis nous irons plus loin en analysant :
- Apparition/disparition de disciplines  
- Tendances physiques des athlètes

---

## Objectifs
- Suivre l’évolution des performances par pays
- Analyser la participation féminine à travers l’histoire
- Étudier l’apparition et la disparition de sports
- Mesurer l’évolution du nombre d’athlètes et de pays participants
- Identifier les caractéristiques physiques des athlètes par discipline (work in progress)
- Explorer des corrélations entre performances et données physiques (work in progress)

---

## Données utilisées
- **`athlete_events.csv`** : données brutes des athlètes, épreuves et médailles
- **`noc_regions.csv`** : table de correspondance des codes pays (NOC → nom + région)

---

## Outils & Technologies
- **Excel** : vérifications initiales
- **Python** (Pandas, NumPy) : nettoyage et préparation des données
- **SQLite** : stockage et requêtes SQL
- **Power BI** : visualisations interactives

---

## Étapes de préparation des données (Excel et Python)
1. **Chargement et inspection** du CSV (271 116 lignes, 15 colonnes)
2. **Traduction** des noms de colonnes et des sports en français
3. **Gestion des valeurs manquantes** :
   - Remplacement des `NA` dans les médailles par `-`
   - Imputation de l’âge, taille, poids par moyennes **par discipline**
4. **Nettoyage des valeurs extrêmes** après vérification avec des sources sportives
5. **Suppression des disciplines non pertinentes** (ex. : compétitions artistiques)
6. **Création d’une clé unique** : `ID_Année_Discipline_Sexe`
7. **Export** vers `olympics_clean.csv` 

---

## Exemple de requêtes SQL
- Comptage et suppression des doublons
- Jointure avec `noc_regions`
- Vérification des NOC orphelins
- Création de la table enrichie `olympics_enriched` pour analyses

---

## Visualisations Power BI
**À venir**  
- Traduction des noms de pays  
- Graphiques par saison, pays, sexe, sport  
- Comparaison des tendances physiques par discipline

---

## 📌 État d’avancement
- [x] Nettoyage et préparation des données en Python
- [x] Création de la base SQLite et nettoyage via SQL
- [ ] Visualisations finales dans Power BI
- [ ] Documentation complète du projet
- [ ] Ajout des captures d’écran et insights Power BI

---

## 📂 Structure du dépôt
```
.
├── data/               # CSV et fichiers sources
├── scripts/            # Scripts Python et SQL
├── docs/               # README, captures Power BI
├── JO - Athletes - 1896 - 2016.py
├── noc_regions.xlsx
├── olympics_cleanV2.csv
└── JO.sqlite
```

---

## 🚀 Instructions pour exécuter le projet
1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/votre-utilisateur/olympics-analysis.git
   ```
2. **Installer les dépendances**
   ```bash
   pip install pandas numpy
   ```
3. **Lancer le script Python**
   ```bash
   python "scripts/JO - Athletes - 1896 - 2016.py"
   ```
4. **Explorer la base SQLite**
   - Ouvrir `JO.sqlite` avec [DB Browser for SQLite](https://sqlitebrowser.org/) ou un autre outil compatible

---

## Sources
- Dataset Kaggle : [120 years of Olympic history](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)
- Données originales : [sports-reference.com](https://www.sports-reference.com)

---

## Contact
Projet réalisé par Sébastien BONNIN – En recherche d’alternance Data Analyst  
📍 Rennes / Paris – 📅 Disponibilité : Immédiate
