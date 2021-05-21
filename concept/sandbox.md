#  Sandbox

## Introduction

Une sandbox est un mécanisme qui permet d'éxecuter du code avec moins de risque pour le serveur. Son rôle dans PL est d'éxecuter le code écrit par les étudiants dans les exercices.
Il existe plusieurs sandbox associé à une priorité (pour éviter les pannes...). La sandbox ayant la priorité la plus petite est prioritaire et sera choisit pour recevoir les données du serveur, c'est à dire :
* Le code que les utilisateurs ont écrit pour résoudre les exercices
* Le docker file
* Le langage (C, python ...)

La sandbox doit renvoyer au serveur qui lui a envoyé les programmes à tester :
* le temps d'éxecution du programme
* la valeur de retour du programme
* les warnings s'il existe

## Sandbox 3.1

### Le serveur lui enverra des settings d'Asset associé à des FrozenResource. il recevra le (ID, settings, params) 
- ID : id du Frozenresource
- settings : Settings de l'asset
- param : modifie le contenu de l'exercice

### Envoi d'un cours
- ID : Id du cours / video / static
- settings : null
- param : null

La sandbox le récupère et renvoie le Json correspondant

### Envoi d'une activité
- ID : Id de la FronzenResource correspondant à l'activité
- settings :  Settings de l'asset
- param : modifie le contenu de l'exercice

Execute (ID, settings, param) : 
- Récupération de l'activité (FrozenRessource) grace à son id
- execute commande ***next***, qui renvoie (pl_id, settings, param) du premier pl trouvé.
- Load récursif de l'exercice correspondant dans la base de donnée ainsi que ses sous-exercices
- Build le pl et applique les settings et params
- sauvegarde l'environnement resultant du build.
- renvoi (json, jsonactivity) au client

Grade(ID : int, answer : Json) : 
- vérifie que l'environnement existe, le build s'il n'existe pas.
- execute l'environnement dans un container
- execute la commande ***next***  si l'exercice est fini afin de passer au prochain exercice
- Si l'éxercice est fini il renvoie la note. Sinon il faut refaire les mêmes étapes à partir du ***next***




<!---
Author : Hugo
Validator :
-->
