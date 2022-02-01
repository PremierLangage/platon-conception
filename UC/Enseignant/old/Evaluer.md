
# Cas d'utilisation N° 38 : Evaluer

##	Description

Ce use-case rassemble des dispositifs (visuels, numériques ou autre) de mise en valeurs des traces des élèves pour permettre à l’[enseignant](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Enseignant.md) de réaliser des évaluations/collecter les évaluations, c'est un mode d'accès différent aux assets.
* Ce mode permet definir les modalités d'évaluation. 
* Ce mode permet de réaliser des évaluations à la main (lorsque nécessaire pour certaine activité pédagogique). 
* Ce mode permet de faire les exports des traces et évaluations. 
* Ce mode permet d'indiquer quelles évaluations sont visible oar les élèves. 


> **Déclencheur** : l'enseignant passe en "mode évaluation" (bouton, menu , etc.?  a choisir FIXME) 
> **Acteur Primaire**: Enseignant   
> **Acteurs secondaires**: Etudiant (notification)   
> **Parties Prenantes concernées** : Pour l'export des notes les formations concernées.   
 
 
## Preconditions

Etre connecté comme enseignant sur un cours/classe.

## Scenario Nominal

1. L'enseignant choisi le mode evaluation. 
2. Le système affiche la view Evaluer qui permet de modifier les modalités d'évaluation des assets,
toutes les activités de façon héirachique sont affichées et les boutons (completion,modalités,programme) sont disponible ainsi qu'un lien vers l'export des notes.  
3.	Les boutons ouvrent de nouvelles pages et donc le cas d'utilisation est terminé.

###	Extensions

Les extensions ont lieux entre 2 et 3.


