
# Cas d'utilisation N° 45 :  modifier-completion

Niveau 1

##	Description

L'activité de fait pas de complétion et/ou n'a pas de modalité de calcul de la **[completion](https://github.com/PremierLangage/plconception/blob/master/conception/concept/completion.md)** .
L'enseignant souhaite quand même valider la bonne completion de l'activité.

> **Déclencheur** : Démmarre quand l'enseignant choisi modifier une evaluation dans la view evaluer 
> **Acteur Primaire**: Enseignant
> **Acteurs secondaires**:  
> **Parties Prenantes concernées** : Etudiant   
 
 
## Preconditions

L'enseignant est dans le cas d'utilisation  Evaluer.

## Scenario Nominal

1. le système affiche le selecteur de groupe (pour réduire la liste des élèves). L'enseignant modifi ou pas le selecteur de groupe.
2.	le système affiche la liste des etudiants du groupe avec un menu déroulant positionné par défaut à "pas évalué". Avec comme évaluations possibles: (pas évalué=-1, success=100, échec=0, partiel=50). 
3.	L'enseignant sélectionne pour chaque ligne l'évaluation. Après chaque modification d'une évaluation, le système met à jour l'information dans la base.
4. A la sortie de la page les modification sont accessibles. 


### Selecteur de groupes

Le selecteur de groupes affiche une liste (horizontale) de noms de groupes avec une case a cocher.  Et une case tout les groupes/aucun. Chaque étudiant dans le selecteur de groupes est sélectionné (peut être plusieurs fois les groupes n'étant pas exclusifs).
