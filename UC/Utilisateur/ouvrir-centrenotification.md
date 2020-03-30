
# Cas d'utilisation N° 97 :  ouvrir-centrenotification

Niveau 4

##	Description

L'utilisateur membre souhaite ouvrir le centre de notification afin de les consulter.
Le centre de **[notification](https://github.com/PremierLangage/plconception/blob/master/conception/concept/notification.md)** s'affiche comme un sous-menu de l'icone notification

  
> **Déclencheur** : Click sur l'icone de notification (cloche)  
> **Acteur Primaire**: Membre  
> **Parties Prenantes concernées** : All
 
 
## Preconditions

1. Il faut être connecté
2. Cliquer sur l'icone de notification (cloche)

## Scenario Nominal

1.	Click sur l'icone de notification (cloche)  
2.	Un sous-menu s'ouvre  
3.	La liste des notifications les plus récentes surlignées et non suivi (càd on a pas suivi le lien de la notif) et celles déjà lues sont toutes affichées de façon asynchrone.
4. On peut suivre les notifications pour qu'elles soientt mise en "lue"
5. Le compteur de notifications est mis à jour et l'affichage lu/non lu également du centre de notifications.

> On peut également avoir un bouton "Tout mettre en lue" sans avoir à cliquer sur chaque notification, mais il n'y aura pas de redirection vers les ressources par ce biais. Un bouton "Afficher plus" affichera les notifications plus anciennes à l'aide d'un scrollbar.

> **(Cf. voir schéma)**

![Schema](https://raw.githubusercontent.com/PremierLangage/platon-conception/master/UC/Utilisateur/Images/uc_notif_center.png)


###	Extensions
3. Problème de requête en base, on ne parvient pas à obtenir les notifications.
3. bis. Problème d'inner link, le lien suivi de la notification ne mène nul part.


## Post Conditions
### Conditions de succès 
Le menu s'est bien ouvert avec les notifications les plus récentes.

### Minimal Guarantees
Les notifications restent stockées en base X temps. (Ad vitam aeternam pour le moment)
Elles sont mises à jour de manière asynchrone et s'affichent dynamiquement (via JS et web socket).

### Conditions final en cas d'échec
Le centre de notification est vide à cause d'un problème de requête en base.
OU
L'inner link suivi mène sur une page error html 404

### Frequence
souvent  
### Besoins Spéciaux (optionel)  
Web socket, inner links, front JS
### Performance  
###	Security  
###	Usability / Accessibility  
###	Other  

##	Problèmes et étapes suivantes  
* Liens internes
* Websocket
* API Rest 

FIXME définir ce qui pose problème dans la description **actuelle** du cas d'utilisation.  
FIXME vous pouvez ajouter ici un lien vers une issue github ou un carte de projet github.

TBR
