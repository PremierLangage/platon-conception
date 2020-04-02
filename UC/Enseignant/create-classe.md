
# Cas d'utilisation N° 23 :  crud-classe

Niveau 1

##	Description

 Une classe permet d'organiser un cours (cours-moodle= classe-platon, contient des élèves et un cours composé d'assets).

 **[classe](https://github.com/PremierLangage/plconception/blob/master/conception/concept/classe.md)**  

> **Déclencheur** : Création par un accès LTI par une nouvelle classe du LMS client 
> **Acteur Primaire**: L'utilisateur de type enseignant du LMS qui se connect en premier.  
> **Acteurs secondaires**: -   
> **Parties Prenantes concernées** : Les participant de la classe  
 
 
## Preconditions

Être connecté au LMS client.

## Scenario Nominal

1.	Le système vérifie que l'utilisateur se connectant est un enseignant.
2. le système crée une classe dans la base de donnée avec les données LTI.
3. le système ouvre la page de création de classe avec les données préremplie disponibles.
3.	l'enseignant remplie les champs de création de classe.
FIXME quel champs n'y a t'il pas un UC sur ce sujet ?
4. Un cours est associé à la classe (eventuellement le cours vide).
5.	la classe est créée, l'enseignant et les étudiants peuvent si connecter et elle apparait dans leur page d'acceuil à la prochaine connexion. 

###	Extensions

1. Dans le cas contraire (premier connexion par un étudiant) une page d'erreur indiquant que l'enseignant n'a pas encore créer la classe dans platon.
l'utisateur n'est pas connecté à Platon (sauf si il a déjà un compte à cause d'une autre classe ?).
Fin du cas d'utilisation. 



## Post Conditions
### Conditions de succès 
la classe est créée avec un cours.

### Minimal Guarantees

### Conditions final en cas d'échec

? si l'enseignant abandonne la procédure (reduire le temps de session pour l'opération), la classe n'est pas créée. 

### Frequence
Quelques fois en début de période scolaire. 



##	Problèmes et étapes suivantes  

FIXME Il faut fixer les parametre de définition d'une classe  

TBR
