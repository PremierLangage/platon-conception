# Syntaxe pla

Syntaxe de définition des activités.

Deux niveaux:
- niveau code : un système de gestion de workflow qui permet de préciser quelles actions doit prendre l'activité 
- niveau pla : une activité est un dictionnaire qui permet de définir une partie des comportements de l'activité.

## Format syntaxique des fichiers pla

Conservation du format pl:   
```
	name = jsonvalue  
	name==  
	textual value 
	==  
```

## Déclaration des exercices 

Pour que l'activité puisse choisir et proposer des exercices il faut que l'on ai vérifié les exercices et il faut les placer dans le serveur d'asset.

Deux syntaxes, celle des pltp 

@ chemindelexercice [alias]
Le chemin est soit relative au fichier pla soit absolu. 
Le nom de l'exercice est par défaut celui du nom de base dans le chemin sans l'extension, mais peut être modifié par l'alias.
Exemple:

@ ../tp3/exo5.pl [fractions4]
Par défaut le nom de l'exercice est "exo5" mais remplacé par "fractions4", attention les alias doivent être des identifiants légaux pour des variables python.

La deuxième syntaxe permet de donner un nom a une liste d'exercices:

name@@
exo.pl 
../tp3/exo5.pl
../tp2/exo7.pl
cours.md
fusé.pla
@@


## Rappel des Missions de l'activité

Les rôles de l'activité (! obligatoire, ? optionel):
* ! gérer des données
* ! choisir les exercices
* ? proposer une navigation entre les exercices
* ! fournir un cadre d'affichage au exercice 
* ? fournir un thème css pour les exos
* ! paramètrer le comportement de l'exercice 
* ? parametrer l'exercice (données, aléa, difficulté, etc)
* ? ce comporter comme un exercice 
* ! Fournir des informations au cours

## Gérer des données

Les activités doivent gérer un certains nombre données pour fonctionner.
Les exercices fait (terminés) par l'utilisateur sont dans la variables **done** qui est une liste de dictionnaires (peut être une optimisation a faire pour un chargement fainéant l'information étant dans la base de donnée). 
**last** soit **done[-1]** contient le dernier exercice fait. 

[bof bof]:L'utilisateur, le groupe, la classe sont des variables d'environnement éventuellement accessibles (je suis pas convincu de l'interet sauf peut être pour les exercices direct affectés ??).

Les activités ont une structure json dans la variable **udata** qui est spécifique à l'utilisateur courrant si option **userdata** est positioné.. 
Et une struvture json dans la variable **cdata** qui est commune a tout les utilisateurs d'une même classe et que l'option **classdata** est positioné.
de même pour le **gdata** spécifique au groupe (si il y a des groupe et que l'option **groupesdata** est positioné).

Les activités sont libre de lire et modifier le contenu des variables **?data**. 

La limitation a des json est pour le moment maintenue (dans un avenir proche des classes pourrait être sauvegardée).

Certaines donnée sont stocké directement dans l'asset de l'activité (cf.).

## Choisir les exercices 

*Role principal de l'activité.* 
L'activité contient (car il faut charger les exos dans un asset pour que l'activité puisse y accèder) les références de toute les exercices qu'elle peut utiliser. Bien sur certains exercices sont répétables et l'activité peut décider de les lancer/proposer plusieurs fois.
Le dictionnaire dynamique de l'activité contient une variable _*_current*_ qui contient l'ID de l'asset correspondant à l'exo actif (ou la sous activité).

Le choix peut être fait de différentes façon non exclusives.
- Manuel : l'utilisateur choisi l'exercice qu'il souhaite faire, ceci implique une navigation et une mise à jour de la navigation entre chaque exercice (ou pas comme dans le cas des pltp). Le calcul de la navigation est programmable. 
- Automatique: un algorithme utilise une base de donné d'exercice et choisi l'exercice suivant. 
- Dirigé : l'enseignant peut proposer des exercices, cet action de l'enseignant est asynchrone, il peut ajouter des exercices dans une activité qui seront prioritairement affichés à l'élève.

Ce rôle est réalisé par la méthode **action.next** ou par le **workflow** associé à l'activité qui doit mêtre à jour la variable _current.

Pour le calcul du premier exercice et donc de la mise en place de l'activité l' **action.init** sera exécutée par la plateforme. 

A la fin de chaque exercice avant l'appel à **action.next** l'activité récupèrera l'exécution dans l'exercice dans la variable **done** et exécutera l'**action.collect** pour mettre à jour les données (**Xdata**).


## proposer une navigation entre les exercices (optionel)

La navigation est recalculée, pour mettre à jour les informations de réussite, et pour rendre accessible ou disabled des exercices. 

Ce role est réalisé par la méthode **action.nav** qui met à jour la variable json **navigation** dont la structure est définie par dans le rôle suivant (cadre d'affichage).


## ! fournir un cadre d'affichage aux exercices 

Le cadre d'affichage est un élément angular qui organise l'affichage des exercices et de la navigation. 
Un certain nombre de thèmes sont proposé les modalités de programmation de ces cadre n'est pas encore figé.

## ? fournir un thème css pour les exos (optionel)

Les exercices utilise un certain nombre de classes css qui peuvent être paramêtrées par un thème css.
C'est l'activité qui porte ce thème css dans son dictionnaire: **theme** 

## ! paramètrer le comportement de l'exercice 

Les exercices sont traités en F&F **fire and forget** c'est à dire qu'une fois que l'activité les a lancés ils se déroulent en autonomie, mais les exercices sont paramêtrables et leurs settings doivent être définis préalablement. C'est le rôle de l'activité de fournir ces settings. Pour gérer la dynamique du site il est **néccessaire** de savoir si un exercice est terminé ou pas et donc savoir si il faut le relancer ou pas. 

Les balises **setting**, **parameters** quand un exercice est lancé il reçoit deux dictionnaires qui modifie le dictionnaire de départ de l'exercice. Dans les deux cas les valeurs des clefs des deux dictionnaires remplace les valeurs par défaut de l'exercice.

### Settings des exercices 

setting.nbtry = nbr d'essai par tentative 0 (default) = infinity, 1  
setting.reroll = True(default)|False en cas d'echec autorisation de relancer l'exercice (pour les exercices caculatoire répétables)  
setting.syntactic = True(default)|False  # l'exercice peut si il y a une erreur de syntaxe dans la réponse autoriser une tentative non décomptée, sinon cela consome un essai, dans les deux cas si il y a encore un essai, le feedback d'erreur de saisie ou de syntaxe est fournis à l'utilisateur.  
setting.feedback = True(default)|False # Affichage du feedback proposé par l'exercice, sinon pas de feedback.  
setting.evaluation = True(default)|False # affichage de l'évaluation (numérique) de l'exercice, ou pas.  
setting.validation = True(default)|False # le bouton de validation est géré par l'exercice, sinon il est géré par l'activité. Dangereux si l'on oublie de le proposer dans l'activité.   

DEFAULTSETTINGS = { 'nbtry':0, 'reroll':True, 'syntactic':True, 'feedback':False, 'evaluation':False, 'validation'=True }

STEPSSETTINGS = { 'nbtry':1, 'reroll':False, 'syntactic':True, 'feedback':True, 'evaluation':True, 'validation':True }
STANDARDSETTINGS = { 'nbtry':1, 'reroll':True, 'syntactic':True, 'feedback':True, 'evaluation':True, 'validation':True }
EXAMSETTINGS =  {  'reroll':False, 'syntactic':True, 'feedback':False, 'evaluation':False, }

### Paramêtrage
Certains exercice proposent des paramêtrages cf. leurs documentations. 
L'activité peut modifier ces parametrages en fournissant un dictionnaire **parameters**. 


## ? ce comporter comme un exercice 

une activité peut être utilisé comme un exercice par une autre activité.  
Il est donc nécessaire que l'activité puisse fournir un grade et un feedback. 


## ! Fournir des informations au cours

De la même façon l'activité doit remonter des indicateurs au cours, à minima un grade, un % d'avancement , un % de réussite, un feedback ("encore un peu", "presque fini",), une liste d'aav et leur évaluation. 



# Conception générale

Comme pour les exercices pl l'objectif est de fournir au power user la possibilité de construire leur propres activités.

C'est un peu plus délicat que pour les exercices comme plusieurs notions doivent être maitrisés pour profiter pleinement du langage d'activités.

Pour rendre les choses plus simple nous utiliserons le même principe d'héritage que pour les exercice avec le même mots clef **extends** (il est possible que l'on travail avec des observateurs et de l'injection de dépendance mais pas tout de suite).

Les activités apporte un nouveau type de balise les **lambda**  pour rendre l'ecriture de certains script plus facile. 
(syntaxe à définir).

Enfin il est possible de travailler sur des exercices composé i.e. plusieurs exercices proposé en même temps (le carroussel), avec le choix sur l'affichage des feedback et des resultats laissés à l'activité par le parametrage.


# Les exercies composé 

Il sera possible dans platon d'afficher plusieurs exercices à la fois dans la même page web grace a la transformations des exercices en composant angular ce qui permet de mieux les intégrer dans la page.
Chaque exercice restant autonome quand a sa communication vers 



# Le  cas des acivités scénarisés (ou à étapes)

Une des activité que l'on peut programmer est un exercice de maths à étapes.


Quels sont les éléments clefs:

- les étapes doivent être des exercices pré-écrits. 
- grace aux balise **done** et **last** l'activité peut extraire des valeurs de l'étape précédente. 
- il faut écrire une activité générique pour simplifier l'ecriture des exercices à étapes.
- 



## Paramètres/balises des exercices à étapes

>>> doit utiliser le setting.validation = False. la validation devant être faite par l'activité. 



* `liste_exos  = [ exo1, exo2, ...]`
* `coeffs = [c1, c2,...]`
Le coefficient $c_i$ de l'exercice ex$o_i$  de chaque étape dans le score final. 
* `one_way = true/false `
  * Si `True`, l'utilisateur doit valider l'étape i pour accéder à l'étape i+1.
  * Si `False`, la validation se fait à la fin, pour toutes les étapes en même temps. Entre temps, l'utilisateur peut naviguer librement d'une étape à l'autre. _Ceci implique que les étapes sont indépendantes._

* `affichage_score_partiel = true/false`
  * Si `True`, à chaque validation d'étape, un score est calculé à chaque validation d'étape, et affiché.
  * Si `False` le score n'est calculé et affiché qu'après validation de toute les étapes. 
* `affichage_solution = true/false`
  * Si `True`, à chaque validation d'étape, la solution est affichée.
* `affichage_correction = true/false`
  * Si `True`, à chaque validation d'étape, la correction de l'étape est affichée.
* `autoriser_corriger = true/false`
  * Si `True`, après validation l'utilisateur a le droit de corriger sa réponse et revalider.


## Balise Before (optionnel)
Comme d'habitude, du code qui initialise des variables

## Balise Pipeline (optionnel)
Décrit le passage d'informations de l'étape _n_ à l'étape _n+1_. L'étape 0 est le before, l'étape _N+1_ est l'evaluator. Les exos sont numérotés de _1_ à _N_. 

Pour _i = 0..N_, 
* si `pipeline[i]` est un dictionnaire, où les clés sont des noms de clés du dictionnaire généré par l'étape _i_, et les valeurs sont des noms de clés du dictionnaire fourni en entrée à l'étape _i+1_.

Un couple `{a:b}` dans `Pipeline[i]` signifie que la variable `a` générée par l'étape _i_ est injectée dans la variable `b` fournie à l'étape _i+1_. 
* Si `pipeline[i]` est une liste, alors c'est une liste de noms de variables qu'il faut transferer d'une étape à l'autre. 


Note: Par défaut, chaque étape _1,..N_  fournit un score et un feedback qui sont accessibles à Evaluator. 

Une autre prossiblité est d'avoir une variable `commons` qui contient une liste de variables qui sont transmisses d'une étape à l'autre. Dans le cas ou la variable n'existe pas dans l'étape i elle est ignoré (pour ne pas écraser avec un undefined celle de la nouvelle étape). Pendant la préview les variables non définie produirons un message dans la console.



## Balise Introduction

La balise de texte de la page de garde de l'activité.

## Balise Page

Une balise qui permet de mettre en page l'activité. 
Une page Html, avec des conteneurs pour les exos _1, 2, .., N_

## Balise Evaluator
Calcule Le score final et le feedback à partir des données fournies par les étapes _1..N_.


Il nous faudrait une classe `Exo` pour représenter un exercice (un peu comme la classe `Component`). On pourrait construire un exercice dans le `before` de l'activité en utilisant cette classe. Les paramètres du constructeur `Exo` seraient l'adresse du fichier source pl et (optionnel) un dictionnaire de surcharge.

A la fin du `before`, il faudrait avoir construit une liste `liste_exos` d'objets `Exo`.

Cette approche est compatible avec le pipeline (on update l'objet `Exo` avec le dictionnaire du pipeline en temps voulu).



# Exemples de  Codes

Le code d'une activité doit choisir l'exercice que doit lancer le module PlayExo. 

Ceci doit être fait dans la balise next de l'activité.
Pour cela il doit appeller une fonction Launch(exo,settings,param) qui retourne imédiatement (appel asynchrone) et l'activité s'arrète (yield?).
Cette fonction launch a pour effet de charger l'exercice "exo" (identifié par sont id dans les assets), puis de modifier ses settings, et d'y ajouter les parametres. 
Une fois ces modification réalisées on lance un build sur la sandbox, une fois le build réalisé, il faut lancer sur le front de l'utilisateur courrant un composant angular d'exercice avec en paramêtre cet exercice post build.
L'exercice terminé l'activité est rechargé les données d'exécution placées dans la variable done. (done.append(exo.executiondata)).

Puis la fonction next de l'activité est appelée.



## Une activité qui choisit 3 exercices parmi 5.

```
title= Activité de démo
tags=demo

introduction==
Page d'introduction de l'activité.
==

@ exo1.pl
@ exo2.pl
@ exo3.pl
@ exo4.pl
@ exo5.pl [truc]
#Balise de lancement de l'activité 
before ==
# Choix aléatoires de 3 parmis 5 
lst_exos = random.sample([exo1, exo2, exo3, exo4, truc], k=3)
==
state=0
next==
if state>len(lst_exos):
	end()
Launch(lst_exos[state++],settings=STANDARDSETTINGS, {"title":" bande de moules "})
==

end==
# l'objectif du script "end" est de préparer les données de fin d'activité et de calculer le grade pour l'activité.
feedback=vous avez fini. // TBD 
score=sum([exo.score for exo in done])/len(done)
==
```







## Une activité qui choisit 3 exercices parmi 5 dans différentes listes

```
# Création de la liste L1 de 5 exercices 
L1@@
exo1.pl
exo2.pl
exo3.pl
exo4.pl
exo5.pl
@@ 
L2@@
compile/linter.pl
compile/identifiers.pla
compile/linker.md
compile/gesinfo.pl
translation/exo4.pl
@@


before ==
state=0
lstate=0
LL=@[random.sample(L1, k=3),random.sample(L1, k=3)]
==

next==
while lstate < len(LL):
	if state>len(LL[lstate]):
		lstate+=1
		continue
	Launch(LL[lstate][state++],settings=STANDARDSETTINGS, {"author":" Nous !! "})
end()
==

end==
# l'objectif du script "end" est de préparer les données de fin d'activité et de calculer le grade pour l'activité.
feedback=vous avez fini. // TBD 
score=sum([exo.score for exo in done])/len(done)
==
```



## Une activité à étapes.

```
extends=/model/steps.pla

mesetapes@@ 
@ step1.pl
@ step2.pl
@ step3.pl
@@

before ==
params = {'param1': randint(1,10), 'param2': randint(1,10)}
basepipe={'param1','param2'}
# Variable utilisée oar le model steps
steps = mesetapes
==
```

Le models steps.pla si il y a échec sur une étape rédémarrage au début.


```
state=0
next==
if state <len(steps):
	param = updatedic(params,basepipe)
	if done[-1].results != OK :
		state=0 # echec au cours d'une des étapes rédémarage
		dobefore()
		Launch(FEEDBACK, settings={}, param={'feedback':" Vous avez échouez vous devez reprendre au début"})
	Launch(steps[state++],settings=STEPSSETTINGS,param)	
else:
	end()
==

```




## Une activité qui génère plusieurs exercices à partir d'un même modèle d'exercice et d'un jeu de données. 

Ce serait utile pour les exercices de vocabulaire.

```
@ exomodel.pl

before ==
from random import sample
data = sample(range(1, 10), k=5)
for value in data:
	lst_exos.append(Exo('exomodel.pl', {'param': value}))
==
```
