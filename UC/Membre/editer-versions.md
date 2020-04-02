
# Cas d'utilisation N° 1 :  editer-versions

##	Description
Objectif: modifier la version d'une ressource utilisé dans une ressource multiple (cours, activité, feuille, section, ...).
Permet de comparer les versions, choisir une version ou de créer une version suplémentaire.

Un membre d'un cercle consulte une **[ressource](https://github.com/PremierLangage/plconception/blob/master/conception/concept/ressource.mdressource)**, ou consulte une liste de ressources. Il peut alors accéder à la liste des **[versions](https://github.com/PremierLangage/plconception/blob/master/conception/concept/version.md)**  
 actuelles de la ressource, ou d'une des ressources de la liste.
 A partir des la liste des versions, il peut en modifier une, pour l'améliorer, ou en créer une autre, s'il souhaite l'adapter à une situation particulière. Il peut aussi en sélectionner une pour ajout à une **[activité][https://github.com/PremierLangage/plconception/blob/master/conception/concept/activity.md)**.
 
 Cela suppose que les versions soient organisées en arbre. _FIXME en liste cela suffirait. Comme dans wikipedia._
 Par contre il faut que les liens de ressources (entre elles dans une activité par exemple) comporte le numero de version.
 La liste des versions consultées est l'ensemble des feuilles de l'arbre.
 Le membre peut dans une ressource multiple (activité) **modifier une version**, c'est à dire, choisir dans la liste des versions de la ressource visé choisir une autre version,soit passer en edition (nouvelle page de la ressource visé pour créer une version suplémentaire), soit créer un fork de la ressource visée pour s'affranchir de celle-ci (mais c'est découragé car cela réduit le partage de curation sur la ressource en question). Dans le cas du fork la ressource copié doit être positionnée dans l'établi du membre (et pas dans ces fichiers personels) ce qui exige une demande au près du DirecteurScientifique d'un cercle englobant l'etabli courrant de la ressource multiple.

 
> **Déclencheur** : Un membre d'un cercle consulte une liste de ressources. Dans le premier cas, un bouton permet d'accéder aux versions. Dans le second cas, un menu contextuel attaché à chaque ressource de la liste permet d'accéder aux versions de cette ressource. 
> **Acteur Primaire**: membre
> **Acteurs secondaires**: Néant  
> **Parties Prenantes concernées** : Néant  
 
 
## Preconditions

1. La ressource doit être versionnable.
2. Pour la modification d'une version, le membre doit avoir l'autorisation nécessaire.
3. Pour la création d'une nouvelle version, le membre doit avoir l'autorisation nécessaire.


## Scenario Nominal

1.	Le membre choisit d'accéder aux versions d'une ressource, soit en consultant cette ressource, soit en consultant une liste de ressources où elle figure.
2.	S'affiche une liste de versions, et une prévisualisation de la version sélectionnée dans la liste. La liste est ordonnée par date décroissante, ou par popularité décroissante des versions. A partir de cette liste, il est possible de revenir à l'endroit à partir duquel on y a accédé. 
3.	Pour chacune des versions de la liste, un menu contextuel propose d'éditer cette version, ou de la tester, ou de l'ajouter à une activité.
4.	Dans l'éditeur, il est proposé de sauvegarder la modification comme une nouvelle version,  ou comme une modification de la version éditée. Dans le cas d'une nouvelle version, un descriptif doit être fourni. Dans le cas d'une modification d'une version, la description de ce qui a été corrigé doit être fourni, et en quoi la modification constitue une amélioration.


###	Extensions

1. La ressource n'a qu'une version. Le menu contextuel propose directement d'éditer cette ressource ou de l'ajouter à une activité sans passer par la liste des versions.

3. L'utilisateur n'a pas les autorisations nécessaires pour modifier/créer une versions. Les choix non autorisés ne sont pas proposés.



## Post Conditions
### Conditions de succès 
L'utilisateur revient de là où il était en 1). Si une version a été modifiée/créée, l'arbre des versions est modifié en conséquence.

### Minimal Guarantees
Si l'utilisateur a modifié/créé une version, mais que celle-ci n'a pas pu être intégrée dans l'arbre des versions, l'utilisateur est informé par un message d'erreur, et revient là où il était en 1). 

### Conditions final en cas d'échec
L'utilisateur est informé par un message d'erreur, et revient là où il était en 1). L'arbre des versions de la ressources est inchangé.

### Frequence

Cas simple d'utilisation. Occurence dès qu'une ressource avec versions doit-être intégrée dans une activité.


##	Problèmes et étapes suivantes  
1. Il faut clarifier les autorisations nécessaires pour valider une modification/création de version. 

2. Si une version est modifiée, elle ne doit pas immédiatement remplacer la précédente dans les choix proposés, mais être d'abord proposée en plus. Si elle s'avère plus populaire, elle est proposée à la place de la précédente. Un remplacement direct est possible par un utilisateur à autorisation élevée.

3. Il faudrait autoriser la création de versions **privées**, uniquement liées à une activité particulière, mais n'ayant pas vocation à être proposées aux autres utilisateurs.



