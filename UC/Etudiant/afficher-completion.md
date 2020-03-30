
# Cas d'utilisation N° 7 :  afficher-completion

Niveau 1

##	Description

Un étudiant veut savoir si il a terminé l'asset ? suffisement ? complètement ? Quel note il a eu
**[completion](https://github.com/PremierLangage/plconception/blob/master/conception/concept/completion.md)**  

> **Niveau** : objectif utilisateur
> **Déclencheur** : L'étudiant accède au tableau de bord d'une activité
> **Acteur Primaire**: Etudiant   
> **Acteurs secondaires**: Enseignant   
> **Parties Prenantes concernées** : Etudiant   
 
 
## Preconditions

L'étudiant est inscrit dans un cours.
Ce cours contient des exercices / activités.


## Scenario Nominal

1.	L'étudiant accède au tableau de bord d'une activité
2.	Il clique sur "voir mon avancée"  
3.	Un tableau et des graphiques récapitulant son avancée sont affichés
4.	L'étudiant est content il a vu ce qu'il voulait voir 


## Post Conditions
### Conditions de succès 
L'étudiant a pu voir ce qu'il voulait voir

### Minimal Guarantees
Les données visibles sont à jour au moment du chargement de la page

### Frequence
Accès assez fréquent
### Besoins Spéciaux (optionel)  
Le chargement doit se faire rapidement (chaque activité doit retrouver rapidement l'avancée de chaque étudiant) Une note doit être remontée aux activité parentes à chaque réponse d'un étudiant.
Cet affichage doit etre moins gourmand quand l'affichage de la completion pour un enseignant.

##	Problèmes et étapes suivantes  
Choix des graphiques proposés en plus du tableau. (Boîte à moustaches pour se comparer aux autres, etc...)  

Cet affichage est le même que celui proposé à un enseignant lorsqu'il choisi d'afficher l'avancé d'un seul élève.
[afficher-completion-enseignant](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/afficher-completion.md)
