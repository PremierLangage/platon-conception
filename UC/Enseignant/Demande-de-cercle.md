
# Cas d'utilisation N° 99 :  Demande-de-cercle

Niveau 1

##	Description

Permet de faire une demande de création de cercle (fait par un administrateur).
Deux posibilités au cours de la création d'un cours/classe, soit l'enseignant connait le cercle auquel il veut appartenir et créer le lien avec son cours en faisant une demande d'entrée dans le cercle au près du physionomiste.

Soit il ne le connait pas et donc demande la création d'un **[cercle](https://github.com/PremierLangage/plconception/blob/master/conception/concept/cercle.md)**  correspondant aux particularités de son cours (niveau, discipline ,etc). C'est l'administrateur qui créer le cercle correspondant (ou inscrit le profe et son cours dans un cercle existant).




> **Déclencheur** : La création d'un cours implique de lier le cours à un cercle. 
> **Acteur Primaire**: Enseignant   
> **Acteurs secondaires**: Soit l'administateur soit le physionomiste   
> **Parties Prenantes concernées** : 
 
 
## Preconditions

Nous somme dans le cas d'utilisation 

## Scenario Nominal

1.	Le système demande a l'enseignant dans quel cercle il inscrit le nouveau cours.  
2. le système propose la liste de cercle dont l'enseignant fait parti, un bouton création, une liste de tout les cercles. 
3.	L'enseignant choisi un cercle parmis les cercle dont il fait parti.
4.	Le cours est ajouté au cours du cercle. Le cercle est associé au cours.


###	Extensions
3. l'enseignant choisi de créer un cours. 
3.1 le système propose un formulair de demande de création de cercle seul:
> Nom du cercle   
> Description du cercle   
> Discipline principale   
> President: loginname or email (par défaut l'utilisateur qui fait la demande)
> Physio :loginname or email 
> DirecteurScientifique : loginname or email 
3.2 l'enseignant rempli le formulaire 
3.3 le système valide l'ensemble des champs. 
3.4 Un cercle temporaire est créer sans membres.
3.5 l'adminsitrateur est notifié qu'il doit valider la création d'un cercle. [Cf uc creation cercle](../Administrateur/creation-cercle.md)
4. le cercle temporaire est associé au cours.


## Post Conditions
### Conditions de succès 
Un cercle est associé au cours.

### Minimal Guarantees

### Frequence
A chaque fois que l'on créer un cours.
