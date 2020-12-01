

# les exercices préparés (prepared)

Les exercices préparés sont des exercices définis sur un model comportant des éléments syntaxique permettant la création d'un formulaire pour la saisie es éléments variables de l'exercices.

## Syntaxe de préparation du modèle 

Pour chaque variable (balise) du modèle qui doit être définie par le formulaire, le modèle doit contenir une ligne de la forme :

```
   # linter:name:type:default:lambda
```
Où:
  - linter est le mot clef de définition.
  - name doit être le identifiant de la balise
  - type doit être un type python (en utilisant la syntaxe du typage statique de python) 
  - default est une valeur par défaut qui rempli la zone de saisie corespondante
  - lambda est une fonction de verification de la valeur entrée dans le champs de saisie, retourne "une string non nul en cas de problème"
 
 Un modèle sera considéré préparé si il n'y a pas besoin de définir d'autre balises pour faire fonctionner l'exercice.
 
