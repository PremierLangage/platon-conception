
# Cas d'utilisation N° 11 :  afficher-profile

Niveau 1

##	Description

Un membre de la plateforme veut pouvoir consulter ses informations en affichant son **[profil](https://github.com/PremierLangage/plconception/blob/master/conception/concept/profile.md)**

> **Déclencheur** : Lors d'un click sur l'icone profile.
> **Acteur Primaire**: Utilisateur   
> **Acteurs secondaires**: //   
> **Parties Prenantes concernées** : Tout le monde
 
 
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
   * Historique d'utilisation de la plate-forme, derniers cours consultés, derniers exos faits ou écrits, etc.
   * Les préférences applicatives 
       * préférences daltonniens 
       * préférences editeur 
       * préférences générales (page d'acceuil, etc)
4.	Il arrive sur une page où toutes ces informations sont détaillées. 
5. Il est arrivé à mettre à jour ses choix.
> (Cf. Schema)

![Schema](https://raw.githubusercontent.com/PremierLangage/platon-conception/master/UC/Utilisateur/Images/uc-display-profile.png)


###	Extensions

### Cas d'Echec 

4. On ne parvient pas à requêter en base, on ne peut obtenir les informations demandées.


## Post Conditions
### Conditions de succès 
Quand l'utilisateur a réussi à accéder à (un sous-menu de) son profil.

### Minimal Guarantees
Leurs informations restent sauvegardées en base.

### Conditions final en cas d'échec
Le profil est affiché mais aucune information n'est affichée

### Frequence
pas souvent.  


##	Problèmes et étapes suivantes  


