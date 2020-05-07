
# Cas d'utilisation N° 58 :  Utiliser-demo

Niveau 1

##	Description

Permet de voir des exercices de démo.
**[demo](https://github.com/PremierLangage/plconception/blob/master/conception/concept/demo.md)**  

> **Déclencheur** : Une URL de démo est parcourrue par un navigateur. 
> **Acteur Primaire**: Visiteur   
> **Acteurs secondaires**:    -
> **Parties Prenantes concernées** :    
 
 
## Preconditions

Une ressource doit avoir été publiée comme démo.
Tous les utilisateurs connectés ou non peuvent avoir accès aux exercices de démo.

## Scenario Nominal

1. Le navigateur accède à la plateforme 
2. le système regarde si l'utilisateur est connecté grace aux cookies 
3.	Si non il créer un utilisateur fictif pour créer une session, l'utilisateur sera "connecté" avec cet identifiant de session tant qu'il utilise ce navigateur et qu'il ne se déconnect pas. La session n'est vallable que quelque jours (5). 
4. La ressource est lancé (build). 
5. l'utilisateur interagit avec la ressource. 
Le système répondant (grader).
6. l'utilisateur a utilisé une ressource en mode démo. 
