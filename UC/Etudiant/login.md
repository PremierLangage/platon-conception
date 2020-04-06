
# Cas d'utilisation N° 43 :  login

Niveau 1

##	Description

Idem utilisateur. L'utilisateur étudiant souhaite se connecter sur la plateforme.
 
> **Déclencheur** : 
 * Click sur l'icone de connexion "Sign in / Se connecter" 
 * Via LTI
 * Par URL
> **Acteur Primaire**: Etudiant , idem qu'utilisateur.

 
## Preconditions

1. Avoir un compte PL créer préalablement via la plateforme ou un compte via LTI


## Scenario Nominal

1.	Click sur l'icone de connexion "Sign in / Se connecter"  
2. Il arrive sur la page de connexion
3.	Il rentre son login / id utilisateur  
4.	Il rentre son password / mdp  
5. Il est authentifié
6.	Il est renvoyé sur la page d'accueil de PL

> **(Cf. voir schéma)**

![Schema](https://raw.githubusercontent.com/PremierLangage/platon-conception/master/UC/Utilisateur/Images/uc-student-login.png)

###	Extensions
3. Il a oublié son login, un lien "login oublié" est disponible
4. Il a oublié son mdp, un lien "mdp oublié" est disponible
5. Son id utilisateur ou mdp est erroné, il n'est pas authentifié. Il retourne sur la page de connexion 2.

1. arrive directement par url
1. arrive par LTI -> arrive dans quelle étape 


## Post Conditions
### Conditions de succès 
Il est authentifié et accède à la page d'accueil de PL

### Minimal Guarantees
Il peut retrouver son login/mdp grâce à son adresse mail du compte

### Conditions final en cas d'échec
Il ne peut pas se connecter si il a oublié son adresse mail, il doit passer par le LTI, et si il a plus accès au LMS de départ il voit avec les adminsitrateur du LMS.

### Frequence
normale

##	Problèmes et étapes suivantes  

En fonction du rôle la page générale est variable 

## Concepts 

page générale 

