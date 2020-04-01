# Triggers



Les Triggers sont des déclencheurs, ils s'activent au cours de certains évènements, une fois activés ils produisent une notification.

Exemple : j'installe une trigger sur une ressource (un template) de façon a être prévenu quand celle ci est modifiée. je choisi de recevoir un mail en plus de ma notification interne. 

Deux familles d'évènements:
- suivi des ressources 
  création/modification/etc d'une ressource triggers au niveau de la base de ressources,
- suivi des élèves (assets): 
 - des notifications pour les profs,
 - des notifications pour les élèves


## FIXME des problème avec la description suivante des triggers

## Un exemple avec une ressource activité 
Les activités sont stockées en base de données de la manière qui suit :

#### Activity
+ name
+ open
+ type
+ activity_data
+ PL
+ teachers
+ students
+ parent

Si les champs **PL**, **open**, ou **users**  changent, on envoie une notification à tous les étudiants concernés (dans cet exemple)

## Implémentation

Pour la manière dont cela va être implémenté dans PL il y a deux possibilités :
+ Mettre des triggers de notifications un peu partout dans les apps
+ Tout centraliser dans l'app notifs et tout gérer depuis celle-ci

Dans tous les cas chaque user peut subscribe à une activité (par exemple). 

Pour chaque subscribe on ajoute dans une liste en python à quel évènement on a souscrit. Quand une création/modification est faite en base de données on envoie une notification à ceux concernés.

Pour faire ça on utilisera les signaux de Django (presave, postsave etc)
