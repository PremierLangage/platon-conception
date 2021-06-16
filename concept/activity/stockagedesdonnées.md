
# Stockage des données d'activités

Les activités sont stockées dans des fichiers et repertoires sur la sandbox.   

L'organisation en repertoire est la suivante:  

Chaque course est stocké dans un répertoire principal: 
 
```
/coursid
```

Le coursid est défini par le serveur et correspond au numéro d'asset sur le serveur. 
Les informations qui ne sont pas contenues dans la base de donnée des assets est contenue
dans des fichiers de ce repertoire.


Chaque activité dans le cours a un repertoire associé:
```
/coursid/activityid/
```
L'activityid correspond à l'identifiant de la frozenRessource associée dans la table des frozen
 ressource sur la sandbox.
Cet identifiant est connu du serveur d'assets.
Le repertoire contient les informations générales de l'activité en particulier toutes les informations 
qui sont partagées par les différents utilisateurs.



Pour chaque utilisateur il y a potentiellement une instance de l'activité l'instance a pour identifiant 
un hashage fait de l'activityid et du userid.

De tel façon qu'il soit possible de récupérer le bon environnement d'exécution de l'acitivité pour l'utilisateur courrant:   
```
/coursid/activityid/pla_env_id/
```
Ce répertoire contient les informations de l'activité dans un fichier YYYY.json. 


De la même façon chaque exercice apparaitra dans un répertoire correspondant au hashcode 'pl_env_id' du tuple (pl_id, param) ou param est le dictionnaire qui est passé en paramêtre du build de l'exercice. Ainsi des exercices avec une seed différente aurons des repertoires différents.

Le repertoire 
```
/coursid/acitvityid/pla_env_id/pl_env_id/ 
```
contient toutes les données et fichiers de l'exercice.


