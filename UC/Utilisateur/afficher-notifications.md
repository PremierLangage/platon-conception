
# Cas d'utilisation N° 10 :  afficher-notifications

Niveau 1

##	Description

Lorsqu'une **[notification](https://github.com/PremierLangage/plconception/blob/master/conception/concept/notification.md)**  est envoyée par la plateforme, elle est affichée dans le [centre de notification](https://github.com/PremierLangage/platon-conception/edit/master/UC/Utilisateur/ouvrir-centrenotification.md) et son compteur est mis à jour.

> **Niveau** :Haut niveau, Résumé, objectif utilisateur, sous fonction, Bas niveau , FIXME Remove unused 

> **Déclencheur** : Une notification est envoyée

> **Acteur Primaire**: Utilisateur   

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
La page des notifications reçoit la nouvelle notification

### Minimal Guarantees
Idéalement on assure la mise à jour des notifications en asynchrone grâce aux web sockets.

### Conditions final en cas d'échec
> Failure is not an option. #Apollo11


FIXME _les variables suivantes sont optionnelles._

### Frequence
Très Souvent 
### Besoins Spéciaux (optionel)  
API Rest
Web Socket
Inner Link
### Performance  
###	Security  
###	Usability / Accessibility  
###	Other  

##	Problèmes et étapes suivantes  
L'utilisateur clique sur le lien de la notification, ou il clique le bouton "tout mettre comme lu".

FIXME définir ce qui pose problème dans la description **actuelle** du cas d'utilisation.  
FIXME vous pouvez ajouter ici un lien vers une issue github ou un carte de projet github.

TBR
