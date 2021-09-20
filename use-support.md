# Cas d'utilisation : Utiliser les supports en ligne 

## Description

Les étudiants doivent pouvoir utiliser les supports de cours ou d'exercices mis en ligne mais aussi les profs doivent pouvoir tester le déroulement des activités.

> **Déclencheur** : l'Administrateur clique sur le bouton play d'une activité 
> **Acteur Primaire** : Membres loggés de n'importe quel statut
> **Acteurs secondaires** : -   
> **Parties Prenantes concernées** : Membres loggés de n'importe quel statut

## Preconditions

- L'utilisateur est loggé sur la plateform web
- Un rôle lui a été automatiquement attribué
- Si le support en question est une activité, on suppose que la structure de cours dans laquelle on doit ajouter le support existe déjà
- Si le support en question est un exercice, on suppose que la structure d'activité dans laquelle on doit ajouter le support existe déjà

## Scenario Nominal

1. L'utilisateur va sur la page des cours pour afficher le cours auquel appartient l'activité à dérouler
2. L'utilisateur choisit l'activité à dérouler
3. L'utilisateur pourra donc interagir avec l'activité selon le mode de cette dernière : 
      - mode exam :
      - ...

## Post Conditions
### Conditions de succès 
Le déroulement de l'activité s'est bien passé et les résultats seront visibles ou pas selon le statut de l'utilisateur (cf **UC: stat-dashboard**)

### Conditions final en cas d'échec
La notification n'est pas détruite dans la liste de l'administrateur.

### Frequence
Autant de fois que possible pour les profs et selon le mode pour les étudiants. 
  - mode exam : 
  - ...
