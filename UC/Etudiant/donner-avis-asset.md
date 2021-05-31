

# Cas d'utilisation N° 101 : Donner son avis 

Niveau 3

##	Description

Donner son avis est une activité qui permet de donner son avis sur une activité.


**Niveau** :objectif utilisateur,  
**Déclencheur** : l'asset a un bouton donner son avis accessible quand l'activité est un success ou terminée et que l'activité admet un avis.
**Acteur Primaire**: Utilisateur   
**Parties Prenantes concernées** : Pour les organismes qui veulent des informations de satisfaction.
 
 
## Preconditions

Que le prof est coché (ou pas a voir ) la demande d'avis.

l'activité demande d'avis est une activité générique utilisable par tous.
IL faut qu'au niveau du serveur elle soit définie. 
Pour cela l'administrateur Ygddrasil doit valider l'activité /model/std/avis.pla

## Scenario Nominal


1. Le prof souhaite avoir des avis sur des acitivté dans son cours. IL valide le bonton corresponant dans les paramètres du cours.	 
2.	En suite il choisi l'activité qui permettra d'avoir un avis dans son cours. (Load acitivity)
3.	les étudiants donnent leur avis.
4.	le prof peut voir les stats de l'activité avis par activité.
5.	Dans le cas d'avis ecrit il peut faire une "correction" de l'activité. Ce qui lui permet de lire les avis.



