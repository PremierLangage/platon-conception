
# Cas d'utilisation N° 11 :  afficher-profile

Niveau 1

##	Description

Un membre de la plateforme veut pouvoir consulter ses informations en affichant son profil.

> **Déclencheur** : Lors d'un click sur l'icone profile.
> **Acteur Primaire**: membre   
> **Acteurs secondaires**: //   
> **Parties Prenantes concernées** :    
 
 
## Preconditions

1. L'utilisateur membre doit être connecté
2. Cliquer sur l'icône profile.


## Scenario Nominal


1.	L'utilisateur clique sur l'icône profile
2.	Un onglet s'ouvre (avec possiblement des sous-menus stats, infos perso)
3.	Il choisit ce qu'il souhaite consulter (stats, informations perso...)  
   * Informations persos
       * E-mail
       * Nom
       * Prenom
       * Etablissement
   * La liste des cercles auxquels il appartient.
   * les préférences applicatives 
       * préférences daltonniens 
       * préférences editeur 
       * préférences générales (page d'acceuil, etc)
4.	Il arrive sur une page où toutes ces informations sont détaillées. 
5. IL est arrivé à mettre à jour ses choix.



###	Extensions

### Cas d'Echec 

4. On ne parvient pas à requêter en base, on ne peut obtenir les informations demandées.


## Post Conditions
### Conditions de succès 
Quand l'utilisateur a réussi à accéder à (un sous-menu de) son profil.

### Minimal Guarantees
Leurs informations restent sauvegardées en base.

### Conditions final en cas d'échec
Le profil n'est pas affiché et page erreur html ?

### Frequence
pas souvent.  


##	Problèmes et étapes suivantes  
Définir si nécessaire la possible existence de sous-menu ? 

Dans ce genre là :
* Profil :
   * Vos infos perso
   * Vos stats
   * Vos qqcdv
...

FIXME JL et si j'était pas la ??  Propose moi des trucs soit force de proposition tu a de l'imagination.

