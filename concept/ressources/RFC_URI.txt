# RFC #

## Problème ##
Mettre en place un système d'URI permettant de référencer d'une façon humainement compréhensible et simple les cercles et resources

## Solution ##
### URI absolues ###
L'idée est de référencer les cercles en suivant leur arborescence sur Platon.
La racine est le cercle racine dans l'arborescence, et on descend étage par étage en utilisant les noms des cercles "sluggifiés".

Ainsi, un chemin "/info/python" pointe vers un cercle "Python", fils d'un cercle "Info", lui-même fils du cercle racine.

Il convient donc d'écrire un module permettant de résoudre ces URIs pour obtenir l'ID du cercle concernant, et inversement, puisque le chemin réel dans le système de fichier en dépend.

Pour référencer une resource, il suffit de renseigner l'URI du cercle qui le contient, puis indiquer après un ':' le nom de la resource "sluggifié".

Par exemple si le cercle "Python" contient une resource "Tableaux", l'URI complète de la resource sera "/info/python:tableaux".

Enfin, si on veut référencer un fichier dans le répertoire de la resource, on peut complèter cette adresse par le chemin du fichier, en séparant par un autre ':' pour éviter des ambiguités. Par exemple, "/info/python:tableaux:exos/exo1.pl".

Les ':' séparent l'URI en 3 parties :
- Cercle(s)
- Ressource
- Fichier

### URI relatives ###
Les URIs peuvent être relatives selon le contexte. On va surtout s'intéresser ici aux syntaxes dans les fichiers .pl/.pla

Dans le cas d'un "extends", nom d'un resource seul (ex: "tableaux") : le parseur hérite le main.pl/pla de la resource/modèle de ce nom contenu dans le cercle local. Si celui-ci n'existe pas, le parseur va essayer de trouver cette ressources dans un cercle parent, et recommencer jusqu'à atteindre la racine

Dans le cas d'un "@" (imports):

* Nom d'un fichier seul (ex: "exo1.pl"): cherche le fichier dans le répertoire local à la resource

* Chemin vers fichier seul (ex: "exos/exo1.pl"): cherche le fichier au chemin indiqué dans le répertoire local à la resource

* Nom de la resource (ex: "tableaux:exos/exo1.pl"): cherche le fichier au chemin indiqué dans la resource nommée "tableaux". Si c'est le nom de la resource actuelle, cherche dans le répertoire local, sinon, remonte dans les cercles parents en cherchant une resource avec le nom correspondant

Dans ces deux cas, l'URI absolue peut aussi être précisée.
