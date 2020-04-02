
# Cas d'utilisation N° 7 :  afficher-completion

Niveau 1

##	Description

Un étudiant souhaite savoir si il a terminé l'asset ? A-t-il suffisement travaillé ? A-t-il complètement achevé le travail ? Quelle note a-t-il eu ? Nous sommes ici sur un feedback synthétique, numérique ou graphique pour aider rapidement à l'étudiant à décider de ce qu'il fera ensuite. Ces vues peuvent aussi être vecteur de motivation...

voir aussi le concept : **[completion](https://github.com/PremierLangage/plconception/blob/master/conception/concept/completion.md)**  

> **Niveau** : objectif utilisateur   
> **Déclencheur** : L'étudiant accède au tableau de bord d'une activité   
> **Acteur Primaire**: Etudiant   
> **Acteurs secondaires**: Enseignant   
> **Parties Prenantes concernées** : Etudiant   
 
 
## Preconditions

* L'étudiant est inscrit dans un cours.
* Ce cours contient des exercices / activités.
* L'étudiant s'est déjà connecté au exercices pour en faire/tenter d'en faire quelques uns.

## Scenario Nominal

1.	L'étudiant accède au tableau de bord d'une activité.
2.	Il clique sur "voir mon avancement" ou "tableau de bord" ou ....
3.	Un tableau et des graphiques récapitulant son avancement sont affichés.
4.	L'étudiant est content car il a vu ce qu'il voulait voir.


## Post Conditions

### Conditions de succès 

L'étudiant a pu voir ce qu'il voulait voir. Cela lui permet de savoir s'il peut considérer son travail comme fini et passer à autre chose (ou pas).

### Garanties minimales

Les données visibles sont à jour au moment du chargement de la page.

### Fréquence

Accès assez fréquent

### Besoins Spéciaux (optionel)  

Le chargement doit se faire rapidement (chaque activité doit retrouver rapidement l'avancée de chaque étudiant). Une note doit être remontée aux activités parentes à chaque réponse d'un étudiant.
Cet affichage doit etre moins gourmand que pour l'affichage de la completion pour un enseignant (qui peut voir tous ses élèves lui...). Une des difficultés de ces visualisation vient de l'emboitement des activités.

##	Problèmes et étapes suivantes  

Choix des graphiques proposés en plus du tableau. (Boîte à moustaches pour se comparer aux autres, etc...)  

Cet affichage est le même que celui proposé à un enseignant lorsqu'il choisi d'afficher l'avancé d'un seul élève.
[afficher-completion-enseignant](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/afficher-completion.md)
