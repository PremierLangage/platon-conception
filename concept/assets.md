  

#  Assets (actifs)


Assets (actifs): activités (ressource) affectées dans une classe. Les actifs sont utilisés dans une classe avec des étudiants, un actif est lié à une ressource (comme une instance à sa classe dans la POO). Le code de la ressource est utilisé dans l'actif, mais aucune modification de la ressource n'est effectuée dans la classe (à l'exception des situations de débogage exceptionnelles necessitant un rechargement (reload) ).
Les actifs contiennent un ensemble fini d'informations relatives à l'interaction de l'actif avec l'élève: (heures d'ouverture, conditions d'accès, ..., évaluations des enseignants, etc.). Cette structure d'informations est commune à tous les actifs et un éditeur HTML de ces valeurs est nécessaire;

Les actifs sont des instanciations des ressources. Une fois la ressource chargée la partie ressource ne peut pas être modifiée sur le serveur d'assets sans être préalablement changée sur le serveur de ressources.
Par contre l'asset contient un ensemble d'informations supplémentaires par rapport à la ressource.

## Les liens entre assets 
Il est possible d'ajouter des liens entre assets qui ont le même rôle (localement) que les liens entre ressources.
Les liens sont des couples (nomdulien, assetvisé) donc unidirectionel et typés.


##  Données d'assets

L'utilité de ces liens est de pouvoir faire des liens entre aav et ressources.
La structure de données d'asset contient:
* la visibilité de l'asset (accessible ou non par les étudiants) **isVisible de type BooleanField**
* la description **type de type ENUMField**
* les aav **aav de type CharFielf**
* le nom et le type **name et type de types CharField**
* le lien vers la ressource que l'asset représente **ressource de type CharField. ex: Ressource:36&versions!=0.3**
* les dates de debut, fin, ouverture, retard etc **opening et closing de types DateField**
* modalité d'évaluation : il est possible de surcharger les modalités d'évaluation de la ressource.

## Description des répertoires utilisées par les Assets
Le répertoire d'Assets a pour racine le dossier /Assets

Tous les assets respectent le schéma suivant : /Assets/Cours/Activite1/ Data  /exo 
                                                                       / usern /exo  où :
                                                                       
* **Cours** est le nom du cours dans lequel est placé l'asset
* **Activite** est le nom de l'activité à laquelle appartient l'asset 
* **Data** est le dossier dans lequel sont placées les données utiles pour l'exécution d'une activité
* **usern** est le dossier qui contient les données de l'utilisateur
* **Data/exo** est le dossier dans lequel sont placées les données pour lancer l'exercice
* **usern/exo** est le dossier dans lequel sont placées les données de l'utilisateur relatives à cet exercice


