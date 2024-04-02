# JEDHA-Projet-2-Kayak

L'équipe marketing de Kayak souhaite développer une application qui aide les utilisateurs à planifier leur prochaine destination de vacances. Cette application utilisera des données en temps réel sur les conditions météorologiques et la disponibilité des hôtels dans divers endroits. En analysant ces variables, l'application fournira des recommandations personnalisées pour les meilleures destinations et hôtels à tout moment.

## Objectifs 🎯
☁️ Utiliser des données météorologiques de différentes ville à partir d'une API.
🏨 Récupérer les données enrichies des hôtels sur le site de booking.
📂 Livrer des résultats incluant des données enrichies dans un DataLake, une intégration avec une base de données, et des cartes interactives présentant les meilleures destinations et hôtels.

## Fonctionnalités ⚙️
- **Analyse Météorologique**: Le script analysera les conditions météorologiques actuelles dans différentes destinations pour suggérer des endroits avec des climats favorables.
- **Disponibilité des Hôtels**: Les données d'hôtels en temps réel seront utilisées pour recommander des hébergements en fonction des préférences, du nombre et de la disponibilité des utilisateurs.
- **Personnalisation**: Les utilisateurs auront la possibilité de personnaliser leurs critères de recherche, tels que le climat préféré, le budget et les dates de voyage, pour des recommandations plus précises.

## Livrables 📬
1. **Données Enrichies**: Un fichier .csv contenant des informations enrichies sur la météo et les hôtels pour chaque ville française sera stocké dans un bucket S3.
2. **Base de Données SQL**: Les données nettoyées du bucket S3 seront intégrées dans une base de données SQL (AWS RDS) pour un accès et une récupération faciles.
3. **Cartes Interactives**: Deux cartes interactives seront créées en utilisant Plotly ou des bibliothèques similaires :
   - **Top 5 des Destinations**: Affichage des cinq meilleures destinations recommandées en fonction des préférences des utilisateurs et de l'analyse des données.
   - **Top 20 des Hôtels**: Présentation des vingt meilleurs hôtels de la région en fonction de la disponibilité, des évaluations des utilisateurs et d'autres facteurs pertinents.


## Utilisation
