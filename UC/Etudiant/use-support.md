# Cas d'utilisation : Utiliser les supports en ligne 

## Description

Les étudiants doivent pouvoir utiliser les supports de cours ou d'exercices mis en ligne.

> **Déclencheur** : l'étudiant clique sur le bouton play d'une activité 
> **Acteur Primaire** : Etudiants
> **Acteurs secondaires** : -   
> **Parties Prenantes concernées** : Etudiants - Professeurs - Responsable de formation 

## Preconditions

- L'étudiant est authentifié sur la plateform web et est inscrit au cours auquel appartient l'activité à dérouler

## Scenario Nominal

1. L'étudiant va sur la page des cours pour afficher le cours auquel appartient l'activité à dérouler
2. L'étudiant choisit l'activité à dérouler : 
      1. Récupérer l'identifiant de l'activité 
      2. Vérifier que l'activité existe dans l'arborescence. Si oui, l'utiliser et sinon la créer : créer un dossier au bon endroit spécifique à l'étudiant - appeler le script start.py // start.py fabrique les fichiers json des exercices qui vont avec
      3. Envoyer à **gui: play-activity** le fichier pla.json et le renvoyer
4. L'étudiant attérit sur **gui: play-activity** et démarre le **UC: play-activity**

## Post Conditions
### Conditions de succès 
Le déroulement de l'activité s'est bien passé et les résultats seront visibles ou pas selon le statut de l'utilisateur (cf **UC: stat-dashboard**)

### Conditions final en cas d'échec
La notification n'est pas détruite dans la liste de l'administrateur.

### Frequence
Autant de fois que possible pour les profs et selon le mode pour les étudiants. 
  - mode exam : 
  - ...

### Work Breakdown Structure 
