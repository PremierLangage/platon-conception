
# Evaluation par les pairs 


Les évaluations par les pairs sont des exercices présent dans des activités dynamiques.
L'activité qui contient une evaluation par les pairs vas commencer par faire faire a chaque étudiant l'exercice de base **exobase** sur lequel est basé l'activité d'évaluation par les pairs.

Une fois qu'un étudiant à fait l'exercice **exobase** il peut participer à l'évalution de celui ci (il ne peut pas participer temps qu'il n'a pas fait l'exercice **exobase**).
L'exercice **exobase** peut avoir une évaluation automatique dans ce cas il faut que l'étudiant décide de "valider" pour évaluation (comme pour un exercice sans évaluation auto) une réponse (cela permet de valider un algorithme avec les tests puis de faire un peu de refactoring une fois que l'on a une version correcte pour améliorer sa note d'évaluation par les pairs). Ceci implique un bouton spécifique dans l'interface qui permet de valider pour évaluation collective et un bouton pour evaluation automatique. {si le bouton eval collective est pressé alors que l'évaluation automatique n'a pas été faite un dialogue apparait "are you sure" ? }. C'est un élément important car cela permet d'éviter des copies qui ne sont pas conforme aux consignes (par exemple trop peu de text ou trop, ou un code qui ne répond pas à la question), si l'étudiant décide de rendre une copie non conforme: il y a une option (correction sans copie : false) qui permet de spécifier si l'on authorise ou non cette option (pour un élève en difficulté c'est bien), par contre il ne pourra pas avoir de points pour l'exercice.

En suite l'activité propose des exercices classique de l'activité ou des évaluations par les pairs. L'algorithme de production de Jeux (games) ne fournis pas à tout moment des évaluations a faire pour tout le monde, deux solutions :

* une solution dynamique avec des websocket et une promise sur la présence d'un exo évaluable par l'étudiant (attente ou l'étudiant ne fait rien, peut être raisonnable dans le contexte d'un tp ou l'on souhaite synchroniser les étudiants).
* une solution ou les autres exercices de l'activité permettent de faire patienter l'étudiant.

Remarque sur les groupes d'exercices: 
Une fois que le groupe contenant l'**exobase** est fait par plus de la moitier des participant et qu'ils ont fait PSY(nombre de participant) évaluations ils peuvent passer un groupes d'exercice suivant (quand ils ont fait tout les exos standard du groupe et que l'algo ne leur fournis pas de Jeux). PSY dépend des options d'évaluation (voir plus bas).

## Les matchs 

Les matchs sont de deux types:

* des matchs feuilles qui contiennent qu'un winner et nbchallenges, qui sont utilisés pour les affichages (On est le gagnant d'un match ou l'on est seul :), ces matchs sont de niveau -1. 
* des  matchs chalenges qui représente une mise en comparaison des réponses de deux étudiants ces chalenges sont réalisés par des Jeux qui font gagner un point à l'un des deux étudiants.
* un match se clos quand le nombre de points d'un des deux students devient supérieur au niveau du match (niveau = level ou level//2 suivant les options ).
* les points se gagne par des Jeux (games) qui sont des exercices d'évaluation par les pairs qui sont fait par un troisième student différent de A et B par défaut (sauf si on autorise l'auto évaluation). 

    @dataclass  
    class Match:  
        studentA:int # MatchID  
        studentB:int # MatchID  
        pointsA:int = 0  
        pointsB:int = 0  
        nbchallenges:int = 0  
        winner:int = -1  
        level:int = 0  
        id:int = -1 # MatchID  


## Les jeux (games)

Les jeux (games) sont des _exercices PLaTon_ qui permet a un étudiant de juger deux réponses à l'exercice de base **exobase**. 


* des jeux (matchs chalenges) qui représente une mise en comparaison des réponses de deux étudiants (réponse "a" ou "b" qui est utilisé pour modifiée les points du match correspondant)


## l'algorithme de production des jeux 

Plusieurs organisation des corrections, **auto-test** chaque élèves compare sa copie par rapport à toutes les autres. **Random(X)** chaque élèves compare X paires de copies prisent aléatoirement dans les copies possibles. **Tournois** des comparaisons sont faites par les élèves pour "classer" les copies, les meilleurs copies étant départagées par plusieurs comparaisons, les copies étant toutes comparées au moins deux fois (compromis entre le nombre de comparaison et l'intéret des comparaisons).


### Auto test (dans une première phase)

Tout les matchs possibles sont produit (n*n-1), tous les élèves évaluent leur propre copie contre celle des autres. Cela fait RAPIDEMENT beaucoup de matchs donc a reservé a de TRES petits groupes. Sinon on définie un nombre m de copies a comparer qui sont choisies par randomisation de façon dynamique. On créer un match avec une copie qui a le moins de matchs terminéss.

Les règles de matchs et de jeux sont différentes:
- a chaque nouvelle réponse d'un élève X. Tout les matchs de la forme 
(X,Y) soit (Y,X) où Y est un des élève ayant déja répondu sont créer et mis dans la liste des matchs encours.
- les jeux sont créer une fois pour chaque match avec comme correcteur le premier élève de la pair.

#### auto test retour prof

Les copies ayant gagnées le plus de matchs sont considérées comme bonnes.
Les copies ayant perdu le plus de matchs sont considérées comme mauvaises.
Les resultats des matchs (X,Y) et (Y,X) sont regardés si il sont en opposition pas de points gagnés pour la correction. Si il sont en accord les deux élèves gagnes 1 pts de correction, la copie gagnante gagne un point suplémentaire d'évaluation.
La note finale de chaque élève est la somme des points d'évaluation plus la note de correction.
Le tableau de bord de l'activité donne la liste de notes des élèves.

### Random (X)

Créer X matchs pour chaque copie sans répétitions.
A partir du moment ou il y a plus de X copies, on commence a créer des matchs sur demande. 
Un utilisateur C demande un match si il n'en a pas déjà eu X on tire au hazard A et B tant que que C n'a pas corrigé le match(A,B) 
et que le match(A,B) n'a pas été fait plus de X fois (attention a ne pas produire une boucle infini si ce n'est pas possible). 

### Le tournois 

Les matchs sont organisé par Gagnants et Perdants, et par niveau.  

* les matchs feuilles sont de niveau -1:
* les matchs de niveau zéro doivent être perdu au moins 2 fois avant élimination.
(ainsi si un etudiant perd son premier match contre le meilleur il a une deuxième chance)
* les matchs de niveaux x sont créer par deux gagnants des match de niveau x-1. 


## Production d'un match

La production d'un mathce est la transformation d'une pair de match terminés (gagnant ou perdant) pour produire une match actif.

Un match est créer pour chaque élève qui réussise l'exercice **exodebase**.
Quand on appel la production de match chaque pair de match terminé de niveau x est retiré et remplacé par un nouveau match de niveau x+1.

Dans le cas ou il n'y a plus de match en cours, qu'il n'y a plus de paire de gagnants de même niveau, mais qu'il y a des gagnants de niveau < niveau max. (On a pas toujours un nombre de copie puissance de 2).  ALORS on vas essayer de faire monter les gagnants des niveau inférieurs soit X le plus petit niveau de ces gagnants: Pour cela on cherche des perdant de ce niveau et l'on fait un match de COMPENSATION (avec le gagnant du niveau et un perdant du niveau), si le gagnant bas le perdant du niveau il monte d'un niveau sinon il devient un perdant de ce niveau, pour le perdant rien ne change. 
[il faut regarder que l'on ne fait pas cela trop vite, si l'on a une idée du nombre d'élèves NBE qui peut participer (sans les fantomes par exemple), alors on ne déclanche cela que quand levelMax atteint est égal à log(NBE+1)-1 soit grosso modo quand la moitier des élèves sont dans un arbre complet et qu'il sera difficile ou impossible d'avoir un arbre complet pour tout le monde].



## Production d'un Jeux 

Le système garde une liste de matchs en cours. 
Si un etudiant demande un jeux, on cherche dans cette liste de matchs un match qu'il n'a pas déja évalué et dans lequel il n'est pas un des deux protagonistes (sauf si il y a l'option : autoévaluation).
Si il n'y en a pas ou lance la création de matchs. 



## Résolution d'un Jeux

le jeux est un exercice platon permettant de comparer deux copies, les données du jeux sont :

- l'identité des deux étudiants A et B
- leur réponse respectives à l'**exobase** 
- l'ID du match correspondant pour la résolution 
l'étudiant a choisi soit A soit B. 
La réponse est utilisée immédiatement pour mettre à jour le match en modifiant le nombre de points coorespondant.

Si le match est terminé le match devient un winner. Les matchs sous jacents sont classés en loser ou terminés.
[Attention a cela, 4 états pour un match, terminé+gagnant, terminé+perdant, encours, terminé+classé] 
Les terminés classé sont des matchs qui ont pour winner quelqu'un qui a gagné le match suivant. 

# PSY
Le nombre PSY donne une limite inférieur pour débloquer les élèves entre deux groupes d'exercices d'évaluation. Ceci dépand de l'algorithme de production des matchs.

