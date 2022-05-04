<h1 style="text-align:center"> RFC </h1>

<h1 style="text-align:center"> ORGANISATION DES ASSETS DANS LE DISQUE NFS </h1>
</br></br>

Cette rfc à pour but d'expliciter l'organisation du disque NFS (Network File System) qui va servir à stocker les [assets](https://github.com/PremierLangage/platon-conception/blob/V2/concept/assets.md) de platon.

Nous avons besoin de spécifier de façon explicte la modalité de stockage les actifs afin de pouvoir les retrouver facilement.
Le server et la sandbox auront accès à ce disque NFS alors cette organisation doit être la plus claire possible.

### BASE

Tout les fichiers seront dans un répertoire racine nommé `/ASSETS`

### COURS

Chaque cours de la platforme possède un répertoire réservé : `/ASSETS/slug_cours`

`slug_cours` étant un identifiant unique attribué au cours et stocké en base de donnée dans la table associée au cours afin de pouvoir le récupérer facilement.

Chaque cours peut posséder ou non des activitées qui seront stockées dans un dossier 
`/ASSETS/slug_cours/DATA`.

### ACTIVITÉS

Chaque activité d'un cours a un répertoire réservé dans le cours : `ASSETS/slug_cours/DATA/slug_activité`

`slug_activité` étant un identifiant unique attribué à l'activité et stocké en base de donnée dans la table associée à l'activité.

Une activité possède un ou plusieurs exercices qui seront stockées dans le dossier `ASSETS/slug_cours/DATA/slug_activité/DATA`.

### EXERCICE

Chaque exercice contenu dans une activité à un répertoire réservé dans l'activité : `ASSETS/slug_cours/DATA/slug_activité/DATA/slug_exercice`

`slug_exercice` étant un identifiant unique attribué à l'exercice et stocké en base de donnée dans la table associée à l'exercice. 
 
Chaque utilisateur ayant joué l'exercice au moin une fois aura un répertoire réservé dans l'exercice : 
`ASSETS/slug_cours/DATA/slug_activité/DATA/slug_exercice/slug_user`
Ce répertoire contiendra des sous répertoires pour chaque session de l'utilisateur où seront stockées c'est réponses à l'exercice pour chaque session.
`ASSETS/slug_cours/DATA/slug_activité/DATA/slug_exercice/slug_user/session_id`

### INFOS

Les cours, activités et exercices ont des fichiers dédiés aux informations divers par exemple un cours peut avoir un fichier qui contient les informations de la disposition des activitées, des eleves inscrits, des profs inscrits, etc. 

Les exercices ont besoin d'un fichier content.tgz qui contient tout l'environnement de l'exercice prêt à être "buildé".

Chaque élève peut avoir a plusieurs répertoire qui lui sont associé repectivement des les dossiers associés aux [cours](#cours), [activités](#activités) et [exercices](#exercice). Ces répertoires contiennent des informations sur l'élève. Exemple : Pour chaque exercice l'élève aura un fichier contenant ses réponses à l'exercice. Il pourra aussi avoir des fichiers contenant des informations statisque sur l'élève afin de savoir si il a essayer de faire chaque activités si il les a réussie ou non, les points qu'il maîtrises ou ceux ou il a des difficultées et autres.  

 `ASSETS/slug_cours/DATA/slug_activité/DATA/slug_exercice/slug_user`
 `ASSETS/slug_cours/DATA/slug_activité/slug_user`
 `ASSETS/slug_cours/slug_user`



### EXEMPLE D'ARBORESENCE

```c
ASSETS/pythonL1_16Z2FS/DUPONT_19U2BSI // Répertoire contenant les informations de monsieur DUPONT dans le cours de python de L1
ASSETS/pythonL1_16Z2FS/DATA/boucles_KJSSD/ //Répertoire réservé de l'activité `boucles` du cours de python
ASSETS/pythonL1_16Z2FS/DATA/boucles_KJSSD/DATA/while_IADUBA/ //Répertoire réservé de l'exercice `while`dans l'activité `boucles` 
ASSETS/pythonL1_16Z2FS/DATA/boucles_KJSSD/DATA/while_IADUBA/DATA/content.tgz //Fichier contenant un environnement compressé avec toutes les données de l'exercice `while`
ASSETS/pythonL1_16Z2FS/DATA/boucles_KJSSD/DATA/while_IADUBA/DATA/DUPONT_19U2BSI // Dossier content les réponses de `DUPONT` à l'exercice `boucles`.
```
