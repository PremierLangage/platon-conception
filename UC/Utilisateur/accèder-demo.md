
# Cas d'utilisation N° 5 :  accèder-demo

Niveau 1

##	Description



FIXME _[One to two sentences that briefly describe the use case, including the primary actor’s goal]_   
FIXME N'oubliez pas de mensioner le concept **[demo](https://github.com/PremierLangage/plconception/blob/master/conception/concept/demo.md)**  

> **Niveau** :Haut niveau, Résumé, objectif utilisateur, sous fonction, Bas niveau , FIXME Remove unused   
> **Déclencheur** : _[Describe the event that initiates the use case.]_ TODO  
> **Acteur Primaire**: Utilisateur   
> **Acteurs secondaires**: None
> **Parties Prenantes concernées** : Tout le monde. ;)
 
 
## Preconditions

Pour que l'on puisse accèder à des démo il faut qu'elles ai été préalablement créées.
le cas d'utilisation pour créer une démo : [crud-ressource-demo](crud-ressource-demo.md)

## Scenario Nominal



1.	l'utilitateur (ou le visiteur) click sur le lien.
2. le système crée/alloue une session de démo.

Le nombre de session maximal de session de démo est 100. 
Quand on n'a plus de session de démo, on détruit la plus vielle.
2. le système fait jouer l'activité de la démo.
Les informations usuelles sont sauvegardé dans la session.
(on pourra faire des states sur les 100 sessions si cela amuse quelqu'un).

Ce référer au cas d'utilisation [interagir-exercice](../Etudiant/interagir-exercice.md) pour la description de l'interaction.

