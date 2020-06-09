
# Cas d'utilisation N° 41 :  login

Niveau 1

##	Description

 Explications de l'accès général à la plateforme avec l'interface générale IHM et les notifications profile etc qui peuvent être déclanchés 

**[centredenotification](https://github.com/PremierLangage/plconception/blob/master/conception/concept/centredenotification.md)**  

> **Niveau** :  Résumé, 
> **Déclencheur** : Connection par LTI ou connection directe 
> **Acteur Primaire**: Utilisateur   
> **Acteurs secondaires**: pas d'acteurs secondaires (a terme LDAP)
> **Parties Prenantes concernées** : tous   
 
 
## Preconditions

Les préconditions sont que l'utilisateur à un compte soit sur le LTI consomateur, soit directement sur platon.


## Scenario Nominal

1.	L'utilisateur connecté sur son LMS  
2.	Le système créé l'utilisateur sur PLATON et le cours si celui si n'existait pas.
3. le système connect l'utilisateur sur la page d'acceuil.

###	Extensions
3. Si l'option revenir ou l'on en était dans platon et possitionnée dans le profil de l'utilisateur, l'utilisateur est connecté à la dernière activité sur laquelle il était connecté.

