# eOnsightTestTechnique
Ce projet est un test technique en deux parties: DataEngineering et ImagesSatellite.
  ### **DataEngineering**
Ce projet vise à agréger d'une page wikipedia présentant des données de ponts (noms,  coordonnées géographiques...) qui se trouvent à Gênes en Italie et les mettre dans une base de données. Le tout doit être exécuté depuis un serveur distant au choix (GCP, AWS, Heroku, serveur perso, ...) puis exposer la base de données.

  ### **ImagesSatellite**
Ce projet vise à présenter ne méthode pour générer une image couleur avec un bon niveau de contraste (similaire à l’image « True color ») représentant un carré d’environ 2km centré autour du viaduc Gênes-Saint-Georges (44°25′34′′N, 8°53′19′′E) en se basant sur les images « Raw » produites par les capteurs optiques de Sentinel-2.
  
## Description
La première partie du test, DataEngineering, contient un fichier Python 'ponts.py' qui traite des données d'ingénierie des ponts, un 'Procfile' pour définir la commande à exécuter par Heroku, un 'requirements.txt' pour déclarer les dépendances Python et un 'runtime.txt' pour spécifier la version de Python utilisée. Heroku est utilisé pour afficher la base de données en sortie du code Python.

La deuxième partie du test, ImagesSatellite, contient un fichier Python imageSatellite.py qui traite des images satellites et une image pont_crop.png.

## Utilisation 
Les librairies nécessaires sont pandas, requests, bs4, psycopg2, os, osgeo (GDAL), numpy et PIL.
