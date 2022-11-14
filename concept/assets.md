  

#  Assets (actifs)


Assets (actifs): élèment graphique avec lequel l'élève peut interagir (exercice, activité, page, vidéo, etc).
Les assets sont des instanciations des ressources (en fait, un asset est une ressource publiée). Une fois la ressource publiée, la partie ressource ne peut pas être modifiée sur le serveur d'assets sans être préalablement changée sur le serveur de ressources.
Par contre l'asset contient un ensemble d'informations supplémentaires par rapport à la ressource. Le code de la ressource est utilisé dans l'actif, mais aucune modification de la ressource n'est effectuée dans la classe (à l'exception des situations de débogage exceptionnelles necessitant un rechargement (reload)).
Les assets contiennent un ensemble fini d'informations TODO: NAME_FOR_THIS relatives à l'interaction de l'asset avec l'élève: (heures d'ouverture, conditions d'accès, voir plus bas.).


Cette structure d'informations est commune à tous les actifs et un éditeur HTML de ces valeurs est nécessaire;


## Les liens entre assets 

Certains assets sont "vides" c'est à dire qu'ils ne sont pas neccesairement liés a des ressources au moment de leur création.
* les cours 
* les sections 

Les cours sont des sections avec des informations supplémentaires: participants, notes, badges, etc.

Les assets sont liées selon une arboresence chaque Asset possède un lien vers sont parent à l'exception de certaines assets "vides".

##  Données d'assets TODO: NAME_FOR_THIS

L'utilité de ces liens est de pouvoir faire des liens entre aav et ressources.
La structure de données d'asset contient:
* modalité d'évaluation : il est possible de surcharger les modalités d'évaluation de la ressource.
* tags 
* la visibilité de l'asset (accessible ou non par les étudiants) **isVisible de type BooleanField**
* la description **type de type ENUMField**
* les aav **aav de type CharFielf**
* le nom et le type **name et type de types CharField**
* le lien vers la ressource que l'asset représente **ressource de type CharField. ex: Ressource:36&versions!=0.3**
* les dates de debut, fin, ouverture, retard etc **opening et closing de types DateField**
* modalité d'évaluation : il est possible de surcharger les modalités d'évaluation de la ressource.
* un numéro d'ordre pour savoir comment l'affiché sur la page.

## Description des répertoires utilisées par les Assets
Le répertoire d'Assets a pour racine le dossier /Assets

Tous les assets respectent le schéma suivant : /Assets/Cours/Activite1/ Data  /exo 
                                                                       / usern /exo  où :
                                                                       
* **Cours** est le nom du cours dans lequel est placé l'asset
* **Activite** est le nom de l'activité à laquelle appartient l'asset apriori un numéro d'activité
* **Data** est le dossier dans lequel sont placées les données utiles pour l'exécution d'une activité
* **usern** est le dossier qui contient les données de l'utilisateur "usern" apriori un numéro d'utilisateur 
* **Data/exo** est le dossier dans lequel sont placées les données pour lancer l'exercice de numéro exo
* **usern/exo** est le dossier dans lequel sont placées les données de l'utilisateur relatives à cet exercice


