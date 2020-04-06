
# Cas d'utilisation N° 6 : visualiser le travail du groupe et de l'élève (afficher-completion)

Niveau 1

##	Description

L'[enseignant](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Enseignant.md) souhaite visualiser la progression d'un [étudiant](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Etudiant.md) ou de plusieurs étudiants sur une activité déployée (un asset), et sur chacune des sous-activités. Cette visualisation s'opère systématiquement dans un **serveur d'assets**.

Il doit obtenir une vue d'ensemble de tous les étudiants inscrits dans l'asset dans un premier temps et une vue pour chaque étudiant s'il le demande. cf. **[completion](https://github.com/PremierLangage/plconception/blob/master/conception/concept/completion.md)**  

> **Déclencheur** : L'utilisateur enseignant accède à un tableau de bord d'activité pour laquelle il a le status d'enseignant. \
> **Acteur Primaire**: Enseignant \
> **Parties Prenantes concernées** : Etudiants et enseignants rattachés par un asset \
 
 
## Preconditions

* Des activités ont été ajoutées à un cours et ce cours a été déployé dans un **serveur d'assets**.
* Il y a des étudiants inscrits dans le cours déployé.
* Des étudiants ont répondu à des exercices dans une des activités du cours déployé (sinon il y a rien à voir).
* Les groupes de classe sont créés (par défaut tous les etudiants de classe, pour la visualisation groupée).

## Scenario Nominal

1.	L'enseignant accède au tableau de bord de l'activité.
2.	Il clique sur "afficher l'avancée des étudiants" ou "tableau de bord" ou ...
3. Le tableau récapitulatif de l'avancement est affiché : 
3.1 Voir schéma ![schema](https://raw.githubusercontent.com/PremierLangage/platon-conception/master/UC/Enseignant/%5Bimg%5Dafficher_completion.jpg)
ou ![schema2](https://raw.githubusercontent.com/PremierLangage/platon-conception/master/UC/Enseignant/affichercompletion.png)
4. le prof est content car il a vu ce qu'il voulait voir. 

**Extensions possibles :** 

5. Il est possible de cliquer sur un élève pour avoir la vue avancement élève (la même que l'élève). 
6. Il est possible de cliquer sur une activité composite pour avoir une synthèse des sous-activités contenues dans l'activité composite.

## Post Conditions

### Conditions de succès 

L'enseignant a pu voir l'avancée de ses élèves en temps raisonnable. La visualisation est agréable voire web-responsive.

### Minimal Guarantees

Les données visibles sont à jour au moment du chargement de la page. Si des précalculs doivent être opérer (mise en cache des highest grade par exemple...), cela a été fait...

### Frequence

Accès régulier

### Performance  

Le chargement doit se faire rapidement (chaque activité doit retrouver rapidement l'avancée de chaque étudiant). Les notes doivent aussi remonter aux activités parentes à chaque réponse d'un étudiant le cas échéant.

##	Problèmes et étapes suivantes  

Quels sont les affichages graphiques proposés ?

En relation avec [completion etudiant](https://github.com/PremierLangage/platon-conception/issues/12) pour la vue d'un étudiant choisi
