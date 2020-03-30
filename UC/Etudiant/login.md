
# Cas d'utilisation N° 43 :  login

Niveau 1

##	Description

Idem utilisateur. L'utilisateur étudiant souhaite se connecter sur la plateforme.
 
> **Déclencheur** : Click sur l'icone de connexion "Sign in / Se connecter" FIXME bof u tape l'url dans le davigateur
> **Acteur Primaire**: Utilisateur membre de rôle étudiant , idem qu'utilisateur   FIXME un acteur c'est le rôle donc il faut choisir le role c'est lequel 


 FIXME un membre c'est PAS un etudiant
 
## Preconditions

1. Avoir un compte PL FIXME oui élaborre ??? 


## Scenario Nominal

1.	Click sur l'icone de connexion "Sign in / Se connecter"  
2. Il arrive sur la page de connexion
3.	Il rentre son login / id utilisateur  
4.	Il rentre son password / mdp  
5. Il est authentifié FIXME que fait le système ??? 
6.	Il accède à la page générale de PL  

###	Extensions
3. Il a oublié son login, un lien "login oublié" est disponible
4. Il a oublié son mdp, un lien "mdp oublié" est disponible
5. Son id utilisateur ou mdp est erroné, il n'est pas authentifié. Il retourne sur la page de connexion

1. arrive directement par url
1. arrive par LTI -> arrive dans quelle étape 


## Post Conditions
### Conditions de succès 
Il est authentifié et accède à la page d'accueil de PL FIXME je voudrais revenir dans l'état ou j'était la dernière fois (ou pouvoir choisir ma page d'acceuil , et que je configure dans le profile -> il faut changer le use case profile.

### Minimal Guarantees
Il peut retrouver son login/mdp grâce à son adresse mail du compte

### Conditions final en cas d'échec
Il ne peut pas se connecter si il a oublié son adresse mail, il doit passer par le LTI, et si il a plus accès au LMS de départ il vois avec les adminsitrateur du LMS.

### Frequence
souvent (comment cela marche les sessions).

##	Problèmes et étapes suivantes  

En fonction du rôle la page générale est variable 

## Concepts 

page générale 

