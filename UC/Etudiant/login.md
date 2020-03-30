
# Cas d'utilisation N° 43 :  login

Niveau 1

##	Description

Idem utilisateur. L'utilisateur membre étudiant souhaite se connecter sur la plateforme.

> **Niveau** :Haut niveau, Résumé, objectif utilisateur, sous fonction, Bas niveau , FIXME Remove unused   
> **Déclencheur** : _[Describe the event that initiates the use case.]_ TODO  
> **Acteur Primaire**: Utilisateur membre de rôle étudiant   

 
## Preconditions

1. Avoir un compte PL


## Scenario Nominal

1.	Click sur l'icone de connexion "Sign in / Se connecter"  
2. Il arrive sur la page de connexion
3.	Il rentre son login / id utilisateur  
4.	Il rentre son password / mdp  
5. Il est authentifié
6.	Il accède à la page d'accueil de PL  

###	Extensions
3. Il a oublié son login, un lien "login oublié" est disponible
4. Il a oublié son mdp, un lien "mdp oublié" est disponible
5. Son id utilisateur ou mdp est erroné, il n'est pas authentifié. Il retourne sur la page de connexion


## Post Conditions
### Conditions de succès 
Il est authentifié et accède à la page d'accueil de PL

### Minimal Guarantees
Il peut retrouver son login/mdp grâce à son adresse mail du compte

### Conditions final en cas d'échec
Il ne peut pas se connecter si il a oublié son adresse mail, il doit passer par un autre moyen. (LTI ?) FIXME DR

### Frequence
souvent 
### Besoins Spéciaux (optionel)  
FIXME _[Describe any additional factors that impact the execution of the use case. These could be environmental, regulatory, organizational or market-driven in nature.]_  
### Performance  
###	Security  
###	Usability / Accessibility  
###	Other  

##	Problèmes et étapes suivantes  

FIXME définir ce qui pose problème dans la description **actuelle** du cas d'utilisation.  
FIXME vous pouvez ajouter ici un lien vers une issue github ou un carte de projet github.

TBR
