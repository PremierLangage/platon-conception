
# Cas d'utilisation N° 6 :  afficher-completion

Niveau 1

##	Description

L'enseignant souhaite savoir la progression d'un étudiant sur une activité, et sur chacune des sous-activités.
Il doit avoir une vue d'ensemble de tout les étudiants et une vue pour chaque étudiant.
**[completion](https://github.com/PremierLangage/plconception/blob/master/conception/concept/completion.md)**  

> **Niveau** : objectif utilisateur

> **Déclencheur** : L'utilisateur accède à un tableau de bord

> **Acteur Primaire**: Enseignant   

> **Parties Prenantes concernées** : Etudiants et enseignants   
 
 
## Preconditions

Des activités ont été ajoutées à un cours.
Il y a des étudiants dans le cours.
Des étudiants ont répondu à des exercices dans une activité.
Les groupes de classe sont créés (par défaut tout les etudiants de classe).

## Scenario Nominal

1.	L'enseignant accède au tableau de bord de l'activité.
2.	Il clique sur "afficher l'avancée des étudiants"
3. Le tableau récapitulatif de l'avancement est affiché : 
3.1 Voir schéma ![schema](https://raw.githubusercontent.com/PremierLangage/platon-conception/master/UC/Enseignant/%5Bimg%5Dafficher_completion.jpg)
4. le prof est content il vu ce qu'il voulait voir.


###	Extensions

3. Il est possible de clicker sur un élève pour avoir la vue avancement élève (la même que l'élève). 
3. Il est possible de clicker sur un activité composite pour avoir la vue détaillé de l'activité 

## Post Conditions
### Conditions de succès 
L'enseignant a pu voir l'avancée de ses élèves

### Minimal Guarantees
Les données visibles sont à jour au moment du chargement de la page

### Frequence
Accès régulier

### Performance  
Le chargement doit se faire rapidement (chaque activité doit retrouver rapidement l'avancée de chaque étudiant)
Une note doit être remontée aux activité parentes à chaque réponse d'un étudiant

##	Problèmes et étapes suivantes  
Quels sont les affichages graphiques proposés ?

En relation avec [completion etudiant](https://github.com/PremierLangage/platon-conception/issues/12) pour la vue d'un étudiant choisi
