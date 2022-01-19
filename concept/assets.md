  

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


##  Données d'assets TODO: NAME_FOR_THIS

L'utilité de ces liens est de pouvoir faire des liens entre aav et ressources.
La structure de données d'asset contient:
* la visibilité de l'asset (accessible ou non par les étudiants)
* les dates de debut, fin, ouverture, retard etc
* restrictions d'accès 
* modalité d'évaluation : il est possible de surcharger les modalités d'évaluation de la ressource.
* tags 



