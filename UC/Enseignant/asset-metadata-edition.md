
# Cas d'utilisation N° 12 :  asset-metadata-edition


## Description

Les enseignants doivent être en mesure d'éditer les métadata d'un **[asset](https://github.com/PremierLangage/plconception/blob/master/conception/concept/assets.md)**. Pour cela, nous devons fournir un formulaire permétant d'éditer les champs déjà existant, ou d'en créer de nouveaux.


> **Niveau** : Haut niveau
> **Déclencheur** : L'utilisateur clique sur le bouton d'édition des métadata de l'asset. 
> **Acteur Primaire**: Utilisateur    
 
 
## Preconditions

Existance d'un asset accessible par l'enseignant.


## Scenario Nominal

1.	L'enseignant clique sur le bouton d'édition de l'asset (voire IHM). 
1.5 le système affiche les méta-données avec la possibilité d'éditer. 
2.	L'enseignant édite / ajoute des champs.
2.1 l'enseignant ne peut retirer des champs définis dans la ressource.
2.2 il peut créer un nouveau champs: nom, type, 
2.3 il peut modifier la valeur des champs existant 
3.	L'enseigant clique sur un bouton "valider".
4.	Si aucune nouvelle version a été créée depuis que l'enseignant a commencé l'édition des métadata, ses modifications sont sauvegardé dans une nouvelle version

### Extensions
Annulation:  
2.	L'enseignant édite / ajoute des champs.
3. L'enseignant annule ses modifications à l'aide d'un bouton annuler

___
Ecriture concurante:
Modification disjointes.
4. Si les champs modifiés sont distincs juste une notification aux deux utilisateurs et les deux modifications sont prises en compte.

Modification conflictuelles.
3.	L'enseignant clique sur un bouton "valider".
4. Un autre enseignant sauvegarder des modifications des métadatas pendant que le premier enseignant était en train de modifier
5. L'enseignant à la possibilité de voir en parallèles ses modifications et celles sauvegardé par l'autre enseignant.
FIXME cela veux dire quoi en parallèle ??? 
6. L'enseignant règle les conflits entre les deux versions
7.	L'enseignant clique sur un bouton "valider".
8.	Si aucune nouvelle version a été créée depuis que l'enseignant a commencé l'édition des métadata, ses modifications sont sauvegardé dans une nouvelle version

___

3.	L'enseignant clique sur un bouton "valider".
4. Un autre enseignant sauvegarder des modifications des métadatas pendant que le premier enseignant était en train de modifier
5. L'enseignant à la possibilité de voir en parallèles ses modifications et celles sauvegardé par l'autre enseignant.
6. L'enseignant annule ses modifications à l'aide d'un bouton annuler


## Post Conditions
### Conditions de succès 
Les modifications de l'enseignants sont sauvegardé dans une nouvelle version des metadata.

### Minimal Guarantees
Les modifications de l'enseignant ne sont perdu que si celui-ci annule personnellement sont édition.

### Conditions final en cas d'échec
Les métadata n'ont pas été modifiés

### Frequence
Souvent.

### Besoins Spéciaux (optionel)  
Garantir la gestion des conflits en cas d'édition simultanés de la part de plusieurs enseignants.
