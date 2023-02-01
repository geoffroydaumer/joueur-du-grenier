# Le joueur du Grenier, célèbre Youtubeur français a besoin de vous pour son prochain épisode spécial : "Papy grenier : Attrape les tous !".

# Son équipe a déjà une développeuse front-end mais elle ne se sent pas très à l'aise avec le back-end et le NoSQL.

# Ainsi, vous devrez, à partir de l'API suivante " https://pokebuildapi.fr/api/v1 ", récupérer la liste de tous les pokemon puis la stocker dans une nouvelle collection "pokemon" de votre base de données que vous nommerez "JDG".

# ​

# Ensuite, vous y ajouterez un 899ème Pokemon :

# { "id": 899, "pokedexId": 899, "name": "Darty Papa", "image": "https://tenor.com/fr/view/kassos-darty-papa-gif-5752923", "videoYoutube": "https://www.youtube.com/watch?v=Gt5-xU1-Ows", "slug": "Darty Papa", "stats": { "HP": 100000000, "attack": 100000000, "defense": 2, "special\_attack": 100000000, "special\_defense": 2, "speed": 1 }

# }

# ​

# Enfin vous allez créer deux queries pour faire un update et un delete sur Darty Papa.

# ​

# NB : Peuplerez votre collection via un script python "app.py", vous noterez vos queries d'update et delete dans un fichier "queries.txt" et enfin vous exporterez votre base de données dans un fichier database.json en suivant le tuto suivant (ou un autre ) https://www.geeksforgeeks.org/export-data-from-mongodb/

# ​

# Le JDG vous remercie...





# DEROULEMENT DU BRIEF

# Connexion au docker et au mongo shell :

# docker exec -it mongodb_4_tutorial bash

# mongosh "mongodb://root:example@localhost:27017"


# """use JDG"""
# """db.createCollection("pokemon")"""

import json
from pymongo import MongoClient

# connexion à la base de données

client = MongoClient("mongodb://root:example@localhost:27017")
db = client["JDG"]
collection = db["pokemon"]

# chargement du fichier JSON

with open(r'C:\VS_Progs\Projets\brief\2023-01-02 joueur du grenier\pokemon.json') as json_file:
    objet_json = json.load(json_file)

# insertion de l'objet JSON dans la collection

collection.insert_many(objet_json)

# { "id": 899, "pokedexId": 899, "name": "Darty Papa", "image": "https://tenor.com/fr/view/kassos-darty-papa-gif-5752923", "videoYoutube": "https://www.youtube.com/watch?v=Gt5-xU1-Ows", "slug": "Darty Papa", "stats": { "HP": 100000000, "attack": 100000000, "defense": 2, "special\_attack": 100000000, "special\_defense": 2, "speed": 1 }

#  }



# mongoexport –db JDG –collection pokemon –out "C:/VS_Progs/Projets/brief/2023-01-02 joueur du grenier/data.json"
# mongoexport --uri mongodb://root:example@localhost:27017 -db JDG --collection pokemon --out "C:/VS_Progs/Projets/brief/2023-01-02 joueur du grenier/data.json"