# Load

Ce session est dédiée au fonctionnement de la commande **Load**.

La commande load permet au serveur de déposer une frozen ressource sur la sandbox.

le sénario est le suivant:

Sur le front l'enseignant responsable du cours souhaite ajouter une activité.

Soit l'activité est un asset simple (chapitre section ... fait directement sur le serveur)
Soit l'activité est une ressource il faut récupérer celle-ci sur le serveur de ressource (cf MC), sous forme d'une archive et ou un json (cf. mc), ce qui implique une compilation (vérification des toutes les références et autres tests).

En suite cette archive (json) est transmise à la sandbox qui valide la bonne reception en fournissant un identifiant de la FR sur la sandbox copiée dans le repertoire du cours.


## Les repertoires dans la sandbox 

Chaque cours à un répertoire réservé /coursID à la racine du disque de données.
Chaque activités du cours est stockée dans un répertoire spécifique :  /coursID/activityID/.
Chaque exercice à une copie de la frozenressource (FR) associe dans ce répertoire. La création de ces sous-répertoires est faite au moment du chargement (load) de l’activité dans le cours. 
Chaque instance de l’activité (pour un utilisateur donnée) est stockée dans le répertoire correspondant /coursID/activityID/hashIDUSER/ ou hashIDUSER est l’identifiant associé à cet activité et cet utilisateur. 
Chaque instance d’exercice associé a cet utilisateur dans cette activité est stocker dans un repertoire /coursID/activityID/hashIDUSER/envid/ ou envid est une clef fabriqué à partir de l’ID de l’exercice et du paramètre param de l’exercice (en particulier la seed).

Ainsi à tout moment un script "cours" peut accéder à toutes les informations du cours en parcourant le répertoire et les fichiers.
Une version “compilé” du cours est dans le fichier cours.json. 
Un script “update.py” permet de mettre a jour le fichier “cours.json”.
Le script “update” est défini dans le cours (version 2021: fichier non modifiable).



