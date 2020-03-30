
# Cas d'utilisation N° 10 :  afficher-notifications

Niveau 1

##	Description

Lorsqu'une **[notification](https://github.com/PremierLangage/plconception/blob/master/conception/concept/notification.md)**  est envoyée, elle est affichée 

> **Niveau** :Haut niveau, Résumé, objectif utilisateur, sous fonction, Bas niveau , FIXME Remove unused 

> **Déclencheur** : Une notification est envoyée

> **Acteur Primaire**: Utilisateur   

> **Acteurs secondaires**: TODO   

> **Parties Prenantes concernées** : tout le monde  
 
 
## Preconditions

une notification est envoyée


## Scenario Nominal


1.	une notification est envoyée 
2.	un petit pop-up s'affiche pendant quelques secondes avec un bip 
3.	au niveau d'une barre de navigation, un chiffre en rouge indique les notifications 
4.	lorsqu'on clique sur le chiffre notifications une fenêtre s'ouvre sur la page des notifications (classées par thèmes ou par dates)

> **(Cf. voir schéma)**

![Schema](https://raw.githubusercontent.com/PremierLangage/platon-conception/master/UC/Utilisateur/Images/uc_notif_display.png)


###	Extensions

Après le 2. on peut directement cliquer sur le fenêtre pop-up et directement arriver à 4.

## Post Conditions

### Conditions de succès 
L'acteur principal à une alerte qu'une nouvelle notification est parvenue
Les barres incrémentent l'alerte 
La page des motifications reçoit la nouvelle notification

### Minimal Guarantees
FIXME _[Describe the guarantee or assurance that this Use Case provides to all Actors and Stakeholders to protect their interest regardless of whether the Use Case ends with success or failure.]_

### Conditions final en cas d'échec
FIXME _[Describe the end condition that results if the Primary Actor fails to accomplish his goal.]_


FIXME _les variables suivantes sont optionnelles._

### Frequence
FIXME _[Indicate how often the use case is expected to occur. This information aids designers and developers in understanding capacity requirements.]_   
### Besoins Spéciaux (optionel)  
FIXME _[Describe any additional factors that impact the execution of the use case. These could be environmental, regulatory, organizational or market-driven in nature.]_  
### Performance  
###	Security  
###	Usability / Accessibility  
###	Other  

##	Problèmes et étapes suivantes  
FIXME _[Note any issues related to the definition of this use case that will require clarification prior to development. Also list any follow-up work that needs to be done prior to sign-off on the use case.]_  

FIXME définir ce qui pose problème dans la description **actuelle** du cas d'utilisation.  
FIXME vous pouvez ajouter ici un lien vers une issue github ou un carte de projet github.

TBR
