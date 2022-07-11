<h1 style="text-align:center"> RFC Platon 001: diskdata</h1>

Creation: 4/05/2022 DOMINIQUE REVUZ

<h1 style="text-align:center"> ORGANISATION DES DONNÉES DANS LE DISQUE PARTAGÉ </h1>
</br></br>


Cette rfc à pour but d'expliciter l'organisation des fichiers sur le disque partagé entre le serveur et la sandbox.

# Qualités attendues du stockage

Trois éléments stratégiques:
 - observer (pull plutôt que push)
 - ondemande (lazy loading des données des tableaux de bord)
 - sans blocages 

Bien-sûr les problématiques de complexité:
 - l'objectif est d'être efficace en terme de nombre d'accès disque (éléments de complexité de base des entrées sorties sur disque)
 - réduire l'empreinte en terme de place disque. 

## Comment assurer ces qualités

Il faut que les accès aux fichiers soit protégés (un seul processus manipule le fichier à la fois), et ceci sans interblocages. Pour cela nous utilisons une stratégie hiérarchique ou les processus ne peuvent modifier en écriture que des fichier de leur niveau. Et accède en lecture qu'a des fichiers de niveau supérieur (plus profonds dans l'arborescence).

Les analytiques sont calculées à la demande (mais pas recalculées).


# Les données stockées

1) les données complémentaires d'asset: fichiers de code et autre 
2) les données par utilisateur de l'asset: les éléments de l'asset spécifique à un utilisateur 
3) les analytiques (données statistiques) de l'asset qui sont nécessaire a de nombreux services de platon.

## Les données complémentaires d'asset

Les assets peuvent être des supports (pdf, video, etc) il faut stocker sur le disque les fichier correspondant pouvoir les fournir au front ou au téléchargement. 

Ces données seront stockées dans le répertoire `/${ASSETPATH}/data` . 

Dans le cas d'un exo ou d'une activité le répertoire  `/${ASSETPATH}/context/` contiendra l'ensemble des fichiers a copier dans le repertoire d'exécution du builder de l'asset. 

## Les données par utilisateurs de l'asset 

Quand un utilisateur utilise un asset actif (activité, exo, etc) il faut créer un répertoire de travail pour l'instanciation de l'asset pour l'utilisateur.

Pour retrouver ce répertoire le chemin sera : `/${ASSETPATH}/${USERslug}/`  ou `${USERslug}` est un mot identifiant uniquement l'utilisateur (le mieux est d'utiliser une formule du genre nomprenom et d'ajouter un entier en cas d'homonymie). Ce Userslug est stocké dans l'utilisateur et est unique.

Par exemple pour une activité l'on exécutera en shell  sur le serveur : `cp -R /${settings.NFS_ASSETS/${ASSETPATH}/context /${ASSETPATH}/${USERslug}`
avant que la sandbox fasse un `cd /${settings.NFS_ASSETS}/${ASSETPATH}/${USERslug}` avant d'exécuter  `python3  /${settings.NFS_ASSETS}/${ASSETPATH}/${USERslug}/builder.py`.


### Localisation absolue sur disque des fichiers 

Tout les fichiers seront dans un répertoire racine nommé settings.NFS_ASSETS.
(voire la configuration des settings dans le framework django qui est utilisé en commun par le serveur et la sandbox).

Cette valeur peut être fixé différemment sur le serveur et la sandbox en fonction des besoins de l'équipe devops.

Par défaut cette valeur est 'ASSETS' et ce répertoire est a la racine du disk: '/Assets'.

## Construction d'un chemin d'asset  : Création du {ASSETPATH}

Un asset est contenu dans un autre asset, à la publication de l'asset,le ASSETPATH du parent est fournit: ParentPath et le ASSETPATH du nouvel asset devient ParentPath/${asset.slug}.

Dans le cas particulier des cours le ParentPath fournis est : '/'

(on fera attention a ne pas redoubler les '/').

## Slug 

Tout les  assets on un slug unique qui permet a un humain de parcourir les répertoires du disque sans trop de difficultés, c'est à dire pas de préfixe commun trop long pas, pas de code hexa numériques illisible, etc.

### COURS

Les cours sont les racines des arborescence de fichiers associés à une classe,
les cours contiennent des informations spécifiques. 

Les cours sont un model django qui contient un slug unique (les cours sont des assets). 
Ce slug permet de créer le COURSPATH de la façon suivante:
COURSPATH= `/${settings.NFS_ASSETS/${Course.slug}/`.

Toutes les informations qui ne sont pas dans le model django sont placé dans le répertoire `/${COURSPATH}/data/`.

Les COURSPATH sont tous uniques : `/${settings.NFS_ASSETS/${CourseSlug}/`.

Chaque cours de la plateforme possède un répertoire réservé : `/${COURSPATH}`

TOUTES  les données/fichiers liées a un cours doivent être dans un des sous répertoire, c'est ce que propose l'organisation suivante.


### ACTIVITÉS et EXO (assets actifs)

Les activités et les exos (il y aura peut être dans l'avenir d'autres types d'assets actifs), utilise un répertoire de travail à la mode d'unix pour stocker et rendre accessible l'ensemble des données utiles pour qu'un utilisateur puisse utiliser l'activité.

Nous proposons pour le moment une simple copie du contexte pour chaque utilisateur (dans un deuxième temps des liens symboliques pourrai être utilisé, ou des répertoires partagées pour faire des économie de place et de temps).

Ainsi au démarrage (build) d'une activité le première action est de créer par copie du répertoire `/${settings.NFS_ASSETS}/${ASSSETPATH}/context` le répertoire `/${settings.NFS_ASSETS}/{ASSETPATH}/{user.slug}/`.

En suite la sandbox reçoit le path: `/${ASSETPATH}/{user.slug}/` et se place sur le répertoire `/${sandbox_settings.NFS_ASSETS}/${ASSETPATH}/{user.slug}/`



### Les Exercices répétables 

Dans le cas des exercices répétables, il faut un répertoire de travail différent pour chaque répétition. 

Dans ce cas le chemin du répertoire de contexte sera : `/${settings.NFS_ASSETS}/{ASSETPATH}/{user.slug}/{tentative}/`
Avec le numéro de tentative comme nom de répertoire.
Il n'est interdit de faire plus de 99 fois un exercice. A partir de 100 le compteur est réinitialisé et le répertoire visé est remplacé à chaque fois.


### Le context d'un asset actif et compression

Une possibilité d'implémentation du contexte est de le stocker sous forme d'une archive compressée et ainsi au lieux de faire une copie une décompression est faite ce qui vas plus vite.


### Analytics construction des données

Les informations collectées sur les utilisateurs (voir plus bas) sont stockées soit dans des modèles django soit dans un fichier /ASSETS/{ASSETPATH}/{user.slug}.json

Comment les informations stockée dans les [cours](#cours), [activités](#activités) et [exercices](#exercice) sont elle produites. 

Il faut faire attention a ne pas avoir de conflit d'accès. 
Dans le cas des données propres a utilisateur elle peuvent être demandé soit par l'utilisateur lui même mais aussi par un autre utilisateur dans le cas d'un calcul de moyenne etc.

Pour ce faire nous allons construire les données par "pull", c'est à dire, un asset ne peut modifier les données d'un asset parent. Si l'asset modifie des données qui peuvent avoir un impact sur les données de l'asset au dessus il positionne un drapeau (dirty_flag) qui indique qu'il faut relire la donnée. Le dirty_flag doit être positionnée dans l'asset parent et dans l'asset courant. 


Ces répertoires contiennent des informations sur l'élève. Exemple : Pour chaque exercice l'élève aura un fichier contenant ses réponses à l'exercice. Il pourra aussi avoir des fichiers contenant des informations statique sur l'élève afin de savoir si il a essayer de faire chaque activités si il les a réussie ou non, les points qu'il maîtrises ou ceux ou il a des difficultés et autres.  

 `ASSETS/slug_cours/DATA/slug_activité/DATA/slug_exercice/slug_user`
 `ASSETS/slug_cours/DATA/slug_activité/slug_user`
 `ASSETS/slug_cours/slug_user`

### Construction des données

Afin de construire de nouvelles données, qui ne sont pas déjà prise en compte dans le modèle django ou dans les fichiers actuelles nous allons utiliser des visiteurs l'idée est de définir un comportement par type d'asset un exemple simple serait la note moyenne d'un cours.

Une classe AssetVisitor est implémentée qui peut nous servir de base pour le parcours des assets dans le disque partagé. Il suffi d'en hériter puis d'implémenter ses méthodes pour chaque type d'asset dont on souhaite un comportement particulier.

Pour le type `Cours` nous allons faire la moyenne des notes des activités. Pour le type `Activité` nous allons faire la moyenne des notes des exercices. Et dans les exercices nous allons parcourir la note de chaque élève à l'exercice et en faire la moyenne.

Pour rendre le comportement modifiable on pourra dans chaque méthode regarder si l'utilisateur à créé un fichier pour surcharger le comportement, dans ce cas l'utilisateur (créateur de cours, d'activité ou d'exercice) pourra remplacer ce comportement en plaçant un fichier "moyenne.py" dans son asset et nous utiliserons la fonction `moyenne(list[Asset])` fournie par le fichier.

Dans chaque `Asset` sera placé un fichier `data.json` permettant de stocker les résultats de ces données l'idée ici est de ne pas recalculer les données qui ont déjà été calculées. Dans ce fichier json on aura associé à chaque donnée la date à laquelle nous l'avons calculée pour la dernière fois.

### ACCESSIBILITÉ AUX ASSETS

#### Propriétés

`/asset/slug_cours/slug_activité` 

La méthode GET permet de récupérer les propriétés de l'activité

La méthode PATCH permet de mettre a jour ses propriétés et d'en ajouter au besoin 


EXEMPLE DE JSON PROPRIÉTÉS

```json
{
    "open_date":"12-01-2023",
    "close_date":"12-02-2023",
    "visible":"true",
    "notation":"active"
}
```

#### Jouer

 - Activité 

`/play/slug_cours/slug_activité`

La méthode GET permet de lancer le `Build` de l'activité

La méthode POST permet de lancer le `Grade` de l'activité il faudra renseigner l'évaluation faite par l'exercice

La méthode PATCH permet de lancer le `Repeat` de l'activité 


 - Exercice

`/play/slug_cours/slug_activité/slug_exercice`

La méthode GET permet de lancer le `Build` de l'activité

La méthode POST permet de lancer le `Grade` de l'activité il faudra renseigner la réponse de l'élève dans le corps de la requête

```JSON
{
    "answer":"42"
}
```

### EXEMPLE D'ARBORESCENCE

```c
/ASSETS/pythonL1/antoinedupont.json //fichier contenant les informations de monsieur DUPONT dans le cours de python de L1
/ASSETS/pythonL1/boucles66/ //Répertoire réservé de l'activité `boucles` du cours de python/
/ASSETS/pythonL1/boucles66/context.tgz //Répertoire de contexte de l'activité `boucles` du cours de python sous forme d'archive
/ASSETS/pythonL1/boucles66/while_IADUBA/ //Répertoire réservé de l'exercice `while`dans l'activité `boucles` 
/ASSETS/pythonL1/boucle66/while_IADUBA/context.tgz //Fichier contenant un environnement compressé avec toutes les données de l'exercice `while`
/ASSETS/pythonL1/boucle66/while_IADUBA/antoinedupont/01/ // Dossier content les réponses de `DUPONT` à l'exercice `boucles` qui est un exercice répétable.
```
