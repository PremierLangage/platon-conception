<h1 style="text-align:center"> RFC Platon 001: diskdata</h1>

Creation: 4/05/2022 DOMINIQUE REVUZ

<h1 style="text-align:center"> ORGANISATION DES DONNÉE DANS LE DISQUE PARTAGÉ </h1>
</br></br>





Cette rfc à pour but d'expliciter l'organisation des fichiers sur le disque partagé entre le serveur et la sandbox.

# Qualités attendues du stockage

Trois éléments stratégiques:
 - observer (pull plutot que push)
 - ondemande (lazy loading des données des tableaux de bord)
 - sans blocages 

Biensur les problèmatiques de complexité:
 - l'objectif d'être efficace en terme de nombre d'accès disque (élement de complexité de base des entrées sorties sur disque)
 - réduire l'empreinte en terme de place disk. 

## Comment assurer ces qualités

Il faut que les accès aux fichiers soit protégés (un seul processus manipule le fichier à la fois), et ceci sans interblocages. Pour cela nous utilisons une stratégie hiérarchique ou les processus ne peuvent modifier en écriture que des fichier de leur niveau. Et accède en lecture qu'a des fichiers de niveau supérieur (plus profonds dans l'arborecence).

Les analytics sont calculées à la demande (mais pas recalculées).


# Les données stockées

1) les données complémentaires d'asset: fichiers de code et autre 
2) les données par utilisateur de l'asset: les élements de l'asset spécifique à un utilisateur 
3) les analytics (données statistiques) de l'asset qui sont nécessaire a de nombreux services de platon.

## Les données complémentaires d'asset

Les assets peuvent être des supports (pdf, video, etc) il faut stocker sur le disque les fichier correspondant pouvoir les fournir au front ou au téléchargement. 

Ces données seront stockées dans le repertoire /${ASSETPATH}/data . 

Dans le cas d'un exo ou d'une activité le repertoire  /${ASSETPATH}/context/ contiendra l'ensemblde des fichiers a copier dans le repertoire d'exécution du builder de l'asset. 

## Les données par utilisateurs de l'asset 

Quand un utilisateur utilise un asset actif (activité, exo, etc) il faut créer un répertoire de travail pour l'instanciation de l'asset pour l'utilisateur.

Pour retrouver ce repertoire le chemin sera : /${ASSETPATH}/${USERslug}/  ou ${USERslug} est un mot identifiant uniquement l'utilisateur (le mieux est d'utiliser une formule du genre nomprenom et d'ajouter un entier en cas d'homonymie). Ce Userslug est stocké dans l'utilisateur et est unique.

Par exemple pour une activité l'on executera en shell  sur le serveur : cp -R /${settings.ASSETS/${ASSETPATH}/context /${ASSETPATH}/${USERslug}
avant que la sandbox fasse un cd /${settings.ASSETS}/${ASSETPATH}/${USERslug} avant d'executer  python3  /${settings.ASSETS}/${ASSETPATH}/${USERslug}/builder.py.


### Localisation absolue sur disque des fichiers 

Tout les fichiers seront dans un répertoire racine nommé settings.ASSETS.
(voire la configuration des settings dans le framework django qui est utilisé en commun par le serveur et la sandbox).

Cette valeur peut être fixé différement sur le serveur et la sandbox en fonction des besoins de l'équipe devops.

Par défault cette valeur est 'ASSETS' et ce répertoire est a la racine du disk: '/ASSETS'.

## Construction d'un chemin d'asset  : Création du {ASSETPATH}

Un asset est contenu dans un autre asset, à la publication de l'asset,le ASSETPATH du parent est fournit: ParentPath et le ASSETPATH du nouvel asset devient ParentPath/${asset.slug}.

Dans le cas particulier des cours le ParentPath fournis est : '/'

(on fera attention a ne pas redoubler les '/').

## Slug 

tout les  assets on un slug unique qui permet a un humain de parcourri les repertoires du disk sans trop de difficultés, c'est a dire pas de préfixe commun trop long pas, pas de code hexa numériques illisible, etc.

### COURS

Les cours sont les racines des arborescence de fichiers associés à une classe,
les cours contiennent des informations spécifiques. 

Les cours sont un model django qui contient un slug unique (les cours sont des assets). 
Ce slug permet de créer le COURSPATH de la façon suivante:
COURSPATH= /${settings.ASSETS/${Course.slug}/.

Toutes les informations qui ne sont pas dans le model django sont placé dans le répertoire /${COURSPATH}/data/.

Les COURSPATH sont tous uniques : /${settings.ASSETS/${CourseSlug}/.

Chaque cours de la platforme possède un répertoire réservé : /${COURSPATH}

TOUTES  les données/fichiers liées a un cours doivent être dans un des sous répertoire, c'est ce que propose l'organisation suivante.



### ACTIVITÉS et EXO (assets actifs)

Les activités et les exos (il y aura peut être dans l'avenir d'autres types d'assets actifs), utilise un repertoire de travail à la mode d'unix pour stocker et rendre accessible l'ensemble des données utiles pour qu'un utilisateur puisse utiliser l'activité.

Nous proposons pour le moment une simple copie du context pour chaque utilisateur (dans un deuxième temps des liens symboliques pourrai être utilisé, ou des repertoire partagées pour faire des économie de place et de temps).

Ainsi au démarrage (build) d'une activité le première action est de créer par copie du repertoire /${settings.ASSETS}/${ASSSETPATH}/context le repertoire /${settings.ASSETS}/{ASSETPATH}/{user.slug}/.

En suite la sandbox recoit le path: /${ASSETPATH}/{user.slug}/ et se place sur le repertoire /${sandbox_settings.ASSETS}/${ASSETPATH}/{user.slug}/



### Les Exercices répétables 

Dans le cas des exercices répétables, il faut un repertoire de travail différent pour chaque répétition. 

Dans ce cas le chemin du repertoire de context sera : /${settings.ASSETS}/{ASSETPATH}/{user.slug}/{tentative}/
Avec le numéro de tentative comme nom de repertoire.
Il n'est interdit de faire plus de 99 fois un exercice. A partir de 100 le compteur est réinitialisé et le repertoire visé est remplacé à chaque fois.


### Le context d'un asset actif et compression

Une possibilité d'implémentation du context est de le stocker sous forme d'une archive compréssée et ainsi au lieux de faire une copie une décompression est faite ce qui vas plus vite.


### Analytics construction des données

Les informations collectées sur les utilisateurs (voir plus bas) sont stockées soit dans des modèles django soit dans un fichier /ASSETS/{ASSETPATH}/{user.slug}.json

Comment les informations stockée dans les [cours](#cours), [activités](#activités) et [exercices](#exercice) sont elle produites. 

Il faut faire attention a ne pas avoir de conflit d'accès. 
Dans le cas des données propres a utilisateur elle peuvent êter demandé soit par l'utilisateur lui même mais aussi par un autre utilisateur dans le cas d'un calcul de moyenne etc.

Pour ce faire nous allons construire les données par "pull", c'est à dire, un asset ne peut modifier les données d'un asset parent. Si l'asset modifie des données qui peuvent avoir un impact sur les données de l'asset au dessus il positionne un drapeau (dirty_flag) qui indique qu'il faut relire la donnée. Le dirty_flag doit être positionnée dans l'asset parent et dans l'asset courrant. 



Ces répertoires contiennent des informations sur l'élève. Exemple : Pour chaque exercice l'élève aura un fichier contenant ses réponses à l'exercice. Il pourra aussi avoir des fichiers contenant des informations statisque sur l'élève afin de savoir si il a essayer de faire chaque activités si il les a réussie ou non, les points qu'il maîtrises ou ceux ou il a des difficultées et autres.  

 `ASSETS/slug_cours/DATA/slug_activité/DATA/slug_exercice/slug_user`
 `ASSETS/slug_cours/DATA/slug_activité/slug_user`
 `ASSETS/slug_cours/slug_user`



### EXEMPLE D'ARBORESENCE

```c
/ASSETS/pythonL1/antoinedupont.json fichier contenant les informations de monsieur DUPONT dans le cours de python de L1
/ASSETS/pythonL1/boucles66/ //Répertoire réservé de l'activité `boucles` du cours de python/
/ASSETS/pythonL1/boucles66/context.tgz Répertoire de contexte de l'activité `boucles` du cours de python sous forme d'archive
ASSETS/pythonL1/boucles66/while_IADUBA/ //Répertoire réservé de l'exercice `while`dans l'activité `boucles` 
/ASSETS/pythonL1/boucle66/while_IADUBA/context.tgz //Fichier contenant un environnement compressé avec toutes les données de l'exercice `while`
/ASSETS/pythonL1/boucle66/while_IADUBA/antoinedupont/01/ // Dossier content les réponses de `DUPONT` à l'exercice `boucles` qui est un exercice répétable.
```
