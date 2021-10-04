# Cas d'utilisation : Mettre au point un support
  
## Description

Le prof doit pouvoir choisir l'endroit où créer la ressource, la créer, être en mesure de l'éditer, tester et visualiser, faire une sauvegarde et consulter l'historique des sauvegardes.

> **Déclencheur** :

  - Création de ressources : cliquer sur bouton pour créer une nouvelle ressource
  - Modification d'une ressource : cliquer sur bouton editer pour modifier les paramètres de la ressources 
  - Sauvegarder après modification ou création : cliquer sur bouton de sauvegarde 
  - Consulter l'historique des sauvegardes : cliquer sur la petite icone à côté du bouton de sauvegarder pour afficher les différentes sauvegardes puis appuyer sur celle qu'on veut voir
  - Tester et visualiser le déroulement de la ressource : cliquer sur bouton play pour commencer le test 
  
> **Acteur Primaire** : Membres de statut prof (Utilisateur connecté par LTI ayant le statut prof sur le LMS)
> **Acteurs secondaires** : -   
> **Parties Prenantes concernées** : Prof

## Preconditions

- L'utilisateur est authentifié sur la plateform web -> cf **UC: connexion**
- On suppose que la structure du cours à modifier existe -> cf **UC: create-course**
- On suppose que le prof est membre d'un cercle -> cf **UC: create-course**
- On suppose qu'il existe déjà au moins une activité dans le cercle de ce cours 
- On suppose que le prof arrive sur son cours et/ou activité en mode édition

## Scenario Nominal

1. On navigue jusqu'à la page de cours où se trouve le support à mettre au point
2. Puisque le professeur arrive en mode édition, pour modifier une ressource il suffit de cliquer sur la ressource en question : les champs modifiables par écriture seront éditables; s'il faut uploader un fichier, cliquer sur l'icône et choisir le fichier en question, il remplacera celui qui y était
3. S'il s'agit d'une création de ressources, cf --> ** UC: add-support **
4. Sinon cliquer sur le support en question 
5. En bas de page, cliquer sur sauvegarder, play ou télécharger (pour télécharger le json de l'activité).
  - Sauvegarder pour enrégistrer dans la liste des sauvegardes et garder en vue la dernière. Lorsque la souris passe sur l'icône de sauvegarde, la liste des sauvegarde s'affiche en volet ouvrant et si on veut accéder à une en particulier il faut cliquer sur son lien.
  - Télécharger pour télécharger le json de la dernière sauvegarde de l'activité
  - Play pour visualiser PlayActivity -> cf **UC: play-activity



## Post Conditions
### Conditions de succès 
Le prof a pu créer sa ressource et elle figure sur la page de cours
  
                    OU

Le prof a modifier la ressource 

                    OU
                    
Le prof a pu faire sa sauvegarde et la précédente version figure sur les listes sauvegardes

                    OU
                    
PlayActivity a été un succès

### Conditions final en cas d'échec

Un pop up esst renvoyé affichant l'erreur rencontré -> cf **gui: pop-up-edit**

## Frequence

Une fois pour chaque sauvegarde 

            OU

Une fois pour chaque création de ressource

            OU

Une fois pour chaque édition

            OU

Une fois pour chaque test de PlayActivity

## Work Breakdown Structure
