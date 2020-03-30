
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


## Scenario Nominal

1.	Des étudiants ont répondu à des exercices dans une activité  
2.	L'enseignant accède au tableau de bord de l'activité
3.	Il clique sur "afficher l'avancée des étudiants"
4.	Il peut voir quels exercices les étudiants ont réussi et l'avancée globale de la classe

###	Extensions

3.	Il clique sur "afficher l'avancée des étudiants"
4. Il clique sur un étudiant
5. Il peut voir l'avancée d'un étudiant plus en détails sur une activité



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

En relation avec [completion etudiant](https://github.com/PremierLangage/platon-conception/issues/12)
