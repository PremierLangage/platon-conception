# Cas d'utilisation : Ajouter des supports en ligne à un cours
  
## Description

Le prof doit pouvoir insérer des supports de cours ou d'exercices pour que les élèves puissent y accéder.

> **Déclencheur** : le prof clique sur le bouton ajouter un support 
> **Acteur Primaire** : Membres de statut prof (Utilisateur connecté par LTI ayant le statut prof sur le LMS)
> **Acteurs secondaires** : -   
> **Parties Prenantes concernées** : Prof - Etudiants

## Preconditions

- L'utilisateur est authentifié sur la plateform web -> cf **UC: connexion**
- On suppose que la structure du cours à modifier existe -> cf **UC: create-course**
- On suppose que le prof est membre d'un cercle -> cf **UC: create-course**
- On suppose qu'il existe déjà au moins une activité dans le cercle de ce cours 

## Scenario Nominal

1. Le prof va sur la page des cours pour afficher la liste de ses cours -> cf **gui: courses-list**
2. Le prof choisit le cours qu'il veut modifier puis l'affiche. -> cf **gui: course**
3. Choisir le bouton add (**+**) sur la page sur laquelle on se trouve. -> cf **UC: create-activity et UC: create-exercise**
4. Choisir la ressource -> **gui: choose-ressource**. 
  - Compiler et vérifier la ressource sélectionnée puis la transférer sur la sandbox -> cf **gui: ressource-freeze-error**
  - Créer un asset
  S'il ne trouve pas la ressource voulue on repart en 2.
8. Editer les propriétés d'assets du support au fur et à mesure puis valider à chaque étape -> cf **gui: edit-asset**
6. Choisir le chapitre et la position dans le chapitre **qqcvd TODO**


## Post Conditions
### Conditions de succès 
Le prof a trouvé son cours.
Il a trouvé la ressource à ajouter. 
Il n'y a pas eu de problème avec la compilation
Il n'y a pas eu de problème avec la validation
Il n'y a pas eu de problème avec le transfert 
Le support est ajouté dans un cours et n'importe quel utilisateur peut l'afficher et le jouer (cf **UC:use-support**).

### Conditions final en cas d'échec
L'utilisateur est renvoyé vers la page **gui: course**

### Frequence
Une fois pour chaque support de cours ajouté. //Un cours contient environs 30 supports. 
