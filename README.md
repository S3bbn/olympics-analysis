# 🏅 120 ans d'histoire des Jeux Olympiques – Analyse et Visualisation

## Contexte
Ce projet explore l’évolution des Jeux Olympiques modernes (été et hiver) entre 1896 et 2016.  
   |Dataset original : [120 years of Olympic history: athletes and results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) – publié sur Kaggle en mai 2018.

## Projet _(en cours)_ : 
Nous allons analyser l’évolution des Jeux Olympiques modernes afin d'en tirer les grandes tendances : nombres de participants, parité femmes-hommes, palmarès par pays etc...   

Passionné par le sport et notamment les Jeux olympiques que je regardais assidument plus jeune j’ai décidé de m’intéresser de plus prêt aux données, car cette compétition est une _vitrine_ mondiale à travers laquelle nous retrouvons l'impact d'évènements historiques importants, sur différents plans : 
   - la géopolitique mondiale, 
   - l’évolution de la place des femmes dans le sport 
   - des valeurs sociétales. 

Puis nous irons plus loin en analysant _(en cours)_ :
- Apparition/disparition de disciplines  
- Tendances physiques des athlètes

Pour y parvenir, les données brutes ont été nettoyées et enrichies avec Python (pandas, numpy) et SQL (SQLite), puis analysées et visualisées dans Power BI. 
   - Le travail a inclus la gestion des valeurs manquantes et des doublons, la traduction partielle en français, la création d’une clé unique.
   
---

## Objectifs
- Montrer l’évolution du nombre d’athlète en fonction des années.
- Montrer l’évolution du nombre de pays participant en fonction des années
- Montrer l’évolution de la place de la femme aux JO
- Mettre en valeur les pays ayant gagné le plus de médailles d’or (JO d’été ou d’hiver)
- Les pays ayant gagné le plus de médailles à travers le monde entre 1896 et 2016.

$${\color{green}work \space in\space  progress}$$
- Étudier l’apparition et la disparition de sports
- Identifier les caractéristiques physiques des athlètes par discipline
- Explorer des corrélations entre performances et données physiques

---

## Données utilisées
- **`athlete_events.csv`** : données brutes des athlètes, disciplines, pays, médailles etc...
- **`noc_regions.csv`** : table de correspondance des codes pays (NOC → nom + région)

---

## Outils & Technologies
- **Excel** : vérifications initiales du **`athlete_events.csv`**
- **Python** (Pandas, NumPy) : nettoyage et préparation des données de **`athlete_events.csv`** vers **`olympics_clean.csv`**
- **SQLite** : stockage et requêtes SQL, jointure entre **`olympics_clean.csv`** et **`noc_regions.csv`** pour créer *`olympics_VD.csv`**
- **Power BI** : visualisations interactives

---

## Étapes de préparation des données (Excel et Python)
1. **Chargement et inspection** du CSV (271 116 lignes, 15 colonnes)
2. **Traduction** des noms de colonnes et des sports en français
3. **Gestion des valeurs manquantes** :
   - Remplacement des `NA` dans les médailles par `-`
   - Imputation de l’âge, taille, poids par **moyennes par discipline**
4. **Nettoyage des valeurs extrêmes** après vérification des sources
5. **Suppression des disciplines non pertinentes** (ex. : compétitions artistiques)
6. **Création d’une clé unique**
7. **Export** vers `olympics_VD.csv` 

---

## SQL
- Comptage et suppression des doublons
- Jointure avec `noc_regions` et vérification des NOC orphelins
- Création de la table  `olympics_VD.csv` pour analyses

---

## Power BI
- Traduction des noms de pays  _(étape à refaire en amont sur python)_
- Graphiques :
   - Nombre d’athlètes en fonction des années
 <img width="1436" height="804" alt="Capture d'écran 2025-08-15 144511" src="https://github.com/user-attachments/assets/e6cdbc2f-0f91-4bf4-85fd-da9214734c3b" />

 
      - Nombre de pays participants en fonction des années 
 <img width="1287" height="727" alt="Capture d'écran 2025-08-15 150800" src="https://github.com/user-attachments/assets/90bda7e2-28c8-4ccd-8b90-1b37a6d5ab96" />

 
      - Evolution de la place de la femme au cœur des Jeux Olympiques 
<img width="1283" height="724" alt="Capture d'écran 2025-08-15 152122" src="https://github.com/user-attachments/assets/d85ab31e-ad46-435c-ad7f-9bbe03df0bcf" />


      - Nombre de médaille d’OR remportées par pays
<img width="1297" height="730" alt="Capture d'écran 2025-08-15 155820" src="https://github.com/user-attachments/assets/ddc66aa3-708d-485d-9df3-030ca52f1b71" />


      - Tableau total de médailles / pays
<img width="1295" height="735" alt="Capture d'écran 2025-08-15 160503" src="https://github.com/user-attachments/assets/0d0cfdf2-b2f5-41ba-8652-66b668a47238" />





---

## État d’avancement
- [x] Nettoyage et préparation des données en Python
- [x] Création de la base SQLite et nettoyage via SQL
- [x] Visualisations finales dans Power BI
- [x] Documentation complète du projet (PDF)
- [x] Ajout des captures d’écran et insights Power BI
- [ ] Work in progress
---

## Structure du dépôt
```
├── data/               # CSV et fichiers sources
   ├── JO.rar (SQLlite)
   ├── athlete_events.csv.rar (CSV d'origine)
   ├── noc_regions.csv.zip (CSV d'origine)
   ├── olympics_VD.zip (CSV après script Python + SQL ; utilisé sur Power BI)
├── scripts/            # Scripts Python
   ├── JO - Athletes - 1896 - 2016.py
├── README
└── Analyse complète.pdf

```

## Sources
- Dataset Kaggle : [120 years of Olympic history](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)
- Données originales : [sports-reference.com](https://www.sports-reference.com)

---

## Contact
Projet en cours réalisé par Sébastien BONNIN – En recherche d’alternance Data Analyst - sebastienbonnin@hotmail.fr
