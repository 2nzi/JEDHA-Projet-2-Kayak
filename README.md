# JEDHA-Projet-2-Kayak

L'équipe marketing de Kayak souhaite développer une application qui aide les utilisateurs à planifier leur prochaine destination de vacances. Cette application utilisera des données en temps réel sur les conditions météorologiques et la disponibilité des hôtels dans divers endroits. En analysant ces variables, l'application fournira des recommandations personnalisées pour les meilleures destinations et hôtels à tout moment.

## Objectifs
- Utiliser des données météorologiques en temps réel pour évaluer les conditions climatiques dans différentes régions.
- Intégrer les données de disponibilité des hôtels pour recommander des hébergements adaptés aux préférences des utilisateurs.
- Offrir des recommandations personnalisées basées sur les préférences des utilisateurs, l'historique de leurs voyages et l'analyse des données.
- Améliorer l'expérience utilisateur en fournissant une interface intuitive et une fonctionnalité fluide.
- Livrer des résultats incluant des données enrichies au format CSV, une intégration avec une base de données SQL, et des cartes interactives présentant les meilleures destinations et hôtels.

## Fonctionnalités
- **Analyse Météorologique**: L'application analysera les conditions météorologiques actuelles dans différentes destinations pour suggérer des endroits avec des climats favorables.
- **Disponibilité des Hôtels**: Les données d'hôtels en temps réel seront utilisées pour recommander des hébergements en fonction des préférences, du budget et de la disponibilité des utilisateurs.
- **Recommandations Personnalisées**: En prenant en compte les préférences des utilisateurs, l'historique de leurs voyages et les données en temps réel, l'application offrira des suggestions de destinations et d'hôtels personnalisées.
- **Interface Utilisateur**: L'application proposera une interface conviviale, permettant aux utilisateurs de saisir facilement leurs préférences et de visualiser les destinations et hôtels recommandés.
- **Personnalisation**: Les utilisateurs auront la possibilité de personnaliser leurs critères de recherche, tels que le climat préféré, le budget et les dates de voyage, pour des recommandations plus précises.
- **Mécanisme de Feedback**: Intégrer un mécanisme de feedback pour permettre aux utilisateurs de donner leur avis sur les destinations et hôtels recommandés, améliorant ainsi les recommandations futures.

## Livrables 📬
1. **Données Enrichies**: Un fichier .csv contenant des informations enrichies sur la météo et les hôtels pour chaque ville française sera stocké dans un bucket S3.
2. **Base de Données SQL**: Les données nettoyées du bucket S3 seront intégrées dans une base de données SQL pour un accès et une récupération faciles.
3. **Cartes Interactives**: Deux cartes interactives seront créées en utilisant Plotly ou des bibliothèques similaires :
   - **Top 5 des Destinations**: Affichage des cinq meilleures destinations recommandées en fonction des préférences des utilisateurs et de l'analyse des données.
   - **Top 20 des Hôtels**: Présentation des vingt meilleurs hôtels de la région en fonction de la disponibilité, des évaluations des utilisateurs et d'autres facteurs pertinents.

## Équipe du Projet
- **Chef de Projet**: [Nom]
- **Développeurs**: [Noms]
- **Designer UI/UX**: [Nom]
- **Analyste de Données**: [Nom]

## Calendrier
- **Planification et Conception**: [Date de Début] - [Date de Fin]
- **Développement**: [Date de Début] - [Date de Fin]
- **Test et Assurance Qualité**: [Date de Début] - [Date de Fin]
- **Déploiement**: [Date de Début] - [Date de Fin]

---
# JEDHA-Projet-2-Kayak

The Kayak Marketing Team aims to develop an application that assists users in planning their next holiday destination. This application will leverage real-time data on weather conditions and hotel availability in various locations. By analyzing these variables, the application will provide personalized recommendations for the best destinations and hotels at any given time.

## Objectives
- Utilize real-time weather data to assess climate conditions in different regions.
- Incorporate hotel availability data to recommend accommodations suitable for users' preferences.
- Offer personalized recommendations based on user input and historical data analysis.
- Enhance user experience by providing intuitive interface and seamless functionality.
- Provide deliverables including enriched data in CSV format, SQL database integration, and interactive maps showcasing top destinations and hotels.

## Features
- **Weather Analysis**: The application will analyze current weather conditions in various destinations to suggest locations with favorable climates.
- **Hotel Availability**: Real-time hotel data will be used to recommend accommodations based on users' preferences, budget, and availability.
- **Personalized Recommendations**: By considering user preferences, past travel history, and real-time data, the application will offer tailored destination and hotel suggestions.
- **User Interface**: The application will feature a user-friendly interface, allowing users to easily input their preferences and view recommended destinations and hotels.
- **Customization**: Users will have the option to customize their search criteria, such as preferred climate, budget, and travel dates, for more accurate recommendations.
- **Feedback Mechanism**: Incorporate feedback mechanism to allow users to provide input on recommended destinations and hotels, enhancing future recommendations.

## Deliverables 📬
1. **Enriched Data**: A .csv file containing enriched information about weather and hotels for each French city will be stored in an S3 bucket.
2. **SQL Database**: The cleaned data from the S3 bucket will be integrated into a SQL database for easy access and retrieval.
3. **Interactive Maps**: Two interactive maps will be created using Plotly or similar libraries:
   - **Top 5 Destinations**: Displaying the top five recommended destinations based on user preferences and data analysis.
   - **Top 20 Hotels**: Showcasing the top twenty hotels in the area based on availability, user ratings, and other relevant factors.

## Technologies
- **Programming Language**: Python
- **Frameworks**: Flask for backend, React for frontend
- **APIs**: Weather API for weather data, Hotel API for hotel availability
- **Database**: MongoDB for storing user preferences and historical data

## Project Team
- **Project Manager**: [Name]
- **Developers**: [Names]
- **UI/UX Designer**: [Name]
- **Data Analyst**: [Name]

## Timeline
- **Planning and Design**: [Start Date] - [End Date]
- **Development**: [Start Date] - [End Date]
- **Testing and QA**: [Start Date] - [End Date]
- **Deployment**: [Start Date] -
