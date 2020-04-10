
# Cas d'utilisation N° 53 :  publier-ressource

Niveau 1

##	Description

Objectif rendre plus visible une ressource. 
Les ressources d'un utilisateur ne sont visible que dans son établi.
Mais elles peuvent être trouvées par une recherche.
Publier une ressource ce fait de deux façons soit dans un cours par ajout a un cours ou reload dans un cours.
Soit dans le cercle sous la supervision du directeur scientifique qui vas attribuer le label à la ressource.

 
> **Déclencheur** :   Ajout, reload, copie de la ressource dans le répertoire publique du membre. 
> **Acteur Primaire**: Membre   
> **Acteurs secondaires**: DirSci
> **Parties Prenantes concernées** : autres membres   
 
 
## Preconditions
Être membre et dans un établi. 

## Scenario Nominal

1. Quand une ressource est chargée pour la première fois dans sur un serveur d'asset et qu'elle est private (dans le repertoire personnel privé du membre). 
2.	Le système vérifie que le membre est propriétaire de la ressource. Sinon un message d'erreur signale le problème et propose plusieurs solutions:
- une notification au propriétaire pour qu'il publie sa ressource. Fin du cas d'utilisation annulation de la mise a jour ou de l'ajout de la ressource.
- une notification au propriétaire et une copie dans la partie privé du membre. 
3.	La ressource est déplacée (avec la même structure de répertoire) dans la partie publique de l'établi du membre. 
4.	La ressource est visible dans les ressources du cercle. 
5. l'opération de modification de l'asset se termine.



###	Scénario alternatif

1. Le membre déplace du repertoire privé au repertoire public de l'atelier une ressource (c'est à dire tout les fichiers privé nécessaires au bon fonctionnement de la ressource, bien entendu pas ceux qui sont déjà publiques). 
1.1 Une autre interface est possible avec un bouton ou autre qui permet de rendre le fichier publique. @mc de voire.
2. Le système vérifie que l'on écrase pas un fichier dans la partie publique et fait un popup de warning. 
2.1 si l'utilisateur dit écraser!  il fautt qu'il soit propriétaire du fichier écrasé.
3. Le dirsci est notifié. La liste des ressources du cercle est mise à jour.
4. La ressource est publié.



## Post Conditions
### Conditions de succès 
La ressource est publique (les anciens liens sur la version privé sont toujours vallables, cela implique que le chemin prié/publique n'est pas important (recherche suscécivement dans publique puis privé)).


### Minimal Guarantees
Dans le cas d'un écrasement (ce qui ne devrai pas avoir lieu car aprori l'utilisateur peut éditer la version publique quand il).
L'opération de publication est complète ou ne l'est pas du tout, si une seule sous ressource pose problème echec de la procédure en entier.

### Conditions final en cas d'échec
En cas d'échec pas de changement de la visibilité de la ressource.


### Frequence
Souvent.

### Besoins Spéciaux (optionel)  
Problème de syncronisation quand on publie en même temps des ressource de même nom dans le même cercle.

