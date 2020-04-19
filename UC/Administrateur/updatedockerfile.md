
# Cas d'utilisation N° 26 :  updatedockerfile

Niveau 1

##	Description
Objectif de l'Administrateur mise à jour de la [dockerfile générale](https://github.com/PremierLangage/plconception/edit/master/conception/concept/stddockerfile.md)
ou ajout d'une dockerfile spécifique [dockerfile](https://github.com/PremierLangage/plconception/edit/master/conception/concept/dockerfile.md).

La mise à jour peut avoir lieux pour une sandbox ou toutes les sandbox.



> **Déclencheur** : Dans la view d'adlminsitration l'admisitrateur choisi un des deux liens 
> **Acteur Primaire**: Administrateur   
> **Acteurs secondaires**:    
> **Parties Prenantes concernées** : tout le monde (c'est dangereux comme truc).

 
## Preconditions
Avoir un fichier dockerfile testé sur une machine qui se met bien à jour. 



## Scenario Nominal

### Mise à jour docker file 

1.	Sur le serveur de ressource l'adminsitrateur ouvre la view mise à jour sanbdox. 
Le système propose de télécharger le fichier dockeractuel.
Ou d'uploader un nouveau fichier docker. 
2.	En cas d'upload. Le système demande si c'est une mise à jour si elle est local ou globale. Le serveur de ressource peut être en avance sur les dockerfile qu'il propose dans son serveur d'asset par rapport aux serveurs d'assets en production.
En cas de mise à jour le dockerfile devient le docker par défaut.
Sinon le dockerfile est juste ajouté à la liste des dockers disponibles.
Dans tout les cas le dockerfile est envoyé à la sandbox associé au serveur d'asset. Qui vas vérifier le bon déroulement de l'installation de celle-ci. L'admiistrateur recevra un mail quand la commande sera fini sur la(les) sandbox.

3.	Quand l'administrateur est satisfait que toutes les sandbox sous sa responsabilité ont recu et installé la nouvelle dockerfile. IL peut déclancher la mise en service de la dockerfile. Pour cela il a une interface qui permet d'envoyer l'instruction de changement de dockerfile par défaut (sans perte de la précédente), ou l'instruction permettant à) un exercice d'utiliser cette nouvelle dockerfile pour le docker qui execute les build/grade d'un exercice.
4.	l'administrateur peut vérifier les dockerfile isntallés sur une sandbox. 



###	Extensions


FIXME     oulllallalalala 

## Post Conditions
### Conditions de succès 
Le dockerfile c'est bien téléchargé, l'image docker à bien été créer sur chaque sandbox, les sandbox l'ont ajoutée aux images disponibles,et l'admisitrateur a reçu tout les mail de confirmation. L'admisitrateur a put ajouter l'image aux images autorisées, ou a changé l'image par défaut. 



### Minimal Guarantees
Pas de changement possible si la création d'image à un problème. 


### Conditions final en cas d'échec



### Frequence
Pas trop souvant la gestion des lib devant passer devant. Pour les modifications.
L'exemple type pour une vraie image suplementaire c'est Ebop.

### Besoins Spéciaux (optionel)  
Il faut eventuellement penser à pouvoir uploader des fichiers sur un serveur visible de toutes les sandbox pour pouvoir fournir les fichier utilisés par les images (le serveur de ressource peut aussi servire a cela, ou aux moins de proxy pour un serveur de fichier du cloud).

### Performance  
###	Security  
IL faut que seul un administrateur dument certifié puisse faire cela (pas l'operateur d'un serveur d'asset dans un coin paumé). 

##	Problèmes et étapes suivantes  

Y a encore des trucs à écrire. 


TBR
