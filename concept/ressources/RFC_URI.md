# URIs #

## Problème ##
Mettre en place un système d'URI permettant de référencer d'une façon humainement compréhensible les ressources. Une API doit permettre de convertir une URI en un chemin vers le dossier contenant la ressource ou le fichier voulu sur le disque physique.

## Spécifications ##

Une URI complète se compose de 3 parties:

cercle:ressource/fichier

Il y a 2 séparateurs importants:
* ':' sépare cercle et ressource
* '/' sépare ressource et chemin vers le fichier

### Cercle ###

La première partie est une URI vers un cercle. Les cercles forment une arborescence à racine unique, un cercle racine. Ainsi, les URIs de cercle correspondent à un chemin de la racine vers le cercle voulu. Des slugs sont utilisés pour faire référence aux cercles, séparés par des '/'.

Par exemple, un chemin "/info/python" pointe vers un cercle "Python", fils d'un cercle "Info", lui-même fils du cercle racine.

Cette partie peut être omise, rendant l'URI relative du point de vue des cercles.

### Ressource ###

Il s'agit du nom de la ressource voulue, sous forme de slug.

Si le cercle n'est pas précisé, l'URI est relative, et fera référence à la ressource du nom voulu dans le cercle local. Si aucune ressource dans le cercle local n'est trouvée, alors il fera référénce à la première ressource de ce nom trouvée en remontant les cercles parents jusqu'à la racine.

Par exemple si le cercle "Python" contient une resource "Tableaux", l'URI complète de la resource sera "/info/python:tableaux".

Si la partie cercle est omise, ':' doit quand même être mis avant le nom de la ressource pour éviter des ambiguités.
Exemple: ":tableaux"
Cette URI fera référence à la première ressource "tableaux" trouvée en regardant dans le cercle local, puis en remontant.

Cette partie peut aussi être omise (la partie cercle le sera aussi dans ce cas). L'interprétation d'un tel chemin relatif est faite dans la partie fichier.

### Fichier ###
Il s'agit d'un chemin classique dans le système de fichier. Le chemin est relatif à partir du dossier de la ressource indiquée. 

La référence '.' est liée au répertoire de la ressource.
La référence '..' est interdite (on ne veut pas permettre de remonter dans des dossiers hors de la ressource).

Un chemin complet pourra avoir cet aspect : "/info/python:tableaux/exos/exo1.pl"

Si seule cette partie est présente, le fichier sera cherché directement dans le répertoire de la ressource locale.
Exemple: "exos/exo1.pl".
Si on se trouve déjà dans la ressource tableaux, ce chemin est équivalent au précédent.

La présence ou non d'un ':' permet d'éviter l'ambiguïté. Par exemple :
* ":tableaux/exos/exo1.pl" : recherche le fichier exos/exo1.pl dans la ressource tableaux, en remontant dans les cercles si nécessaire
* "tableaux/exos/exo1.pl" : recherche le fichier tableaux/exos/exo1.pl dans la ressource locale

## API ##

L'API doit proposer une méthode getlocation qui prend en paramètres :
* un string correspondant à l'URI
* working directory
* une référence à la ressource locale (nécessaire pour les URI locales)
* une 
et qui renvoie un chemin direct vers le dossier/fichier correspondant sur le disque.



