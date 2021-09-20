# Cas d'utilisation : Mettre les supports en ligne 

## Description

Le prof doit pouvoir insérer des supports de cours ou d'exercices pour que les élèves puissent y accéder.

> **Déclencheur** : l'Administrateur clique sur le bouton ajouter un support 
> **Acteur Primaire** : Membres de statut prof
> **Acteurs secondaires** : -   
> **Parties Prenantes concernées** : Membres loggés de n'importe quel statut

## Preconditions

- L'utilisateur est loggé sur la plateform web
- Un rôle lui a été automatiquement attribué

## Scenario Nominal

1. Le prof va sur la page des cours pour afficher la liste des cours qui sont disponibles
2. Le prof choisis le cours dans lequel il veut mettre son support et l'affiche. Si le cours en question n'existe pas, il le crée (cf **UC: create-course**) puis l'afficher.
3. Si le support à ajouter est une sous-activité ou un exercice, il faudra choisir l'activité dans laquelle on veut la mettre puis l'afficher. Si l'activité n'existe pas, il faut la créer (cf **UC: create-activity**) puis l'afficher.
4. Choisir le bouton add (**+**) sur la page sur laquelle on se trouve. (cf **UC: create-activity et UC: create-exercise**)
6. Editer les propriétés du support au fur et à mesure puis valider à chaque étape.

## Post Conditions
### Conditions de succès 
Le support est ajouté dans un cours et n'importe quel utilisateur peut l'afficher et le jouer (cf **UC: play_activity**).

### Conditions final en cas d'échec
La notification n'est pas détruite dans la liste de l'administrateur.

### Frequence
Une fois pour chaque support de cours ajouté.
