# Cas d'utilisation : Mettre au point une ressource
  
## Description

Un membre appartenant à un cercle doit pouvoir créer des ressources dans ce cercle ou éditer les ressources qui existent déjà. 

> **Déclencheur** :

  - Création de ressources : cliquer sur bouton + pour créer une nouvelle ressource
  - Edition d'une ressource : cliquer sur la ressource à éditer pour modifier les paramètres de la ressource 
  
**Acteur Primaire** : Membres d'un cercle

**Acteurs secondaires** : -   

**Parties Prenantes concernées** : -

## Preconditions

- L'utilisateur est authentifié sur la plateform web  -> cf **UC: connexion**
- L'utilisateur est un membre et appartient à un cercle


## Scenario Nominal

1. L'utlisateur choisit le cercle dans lequel il veut travailler -> cf **GUI: acceuil Cercles** 
2. IL choisit de créer ou éditer une ressource -> CF **GUI: affichage cercle** .Il ya un bouton créer ressource. Toutes les ressources visibles dans l'affichage cercle peuvent être éditées en cliquant sur le bouton édition à côté de chaque ressource (il y'a aussi un bouton preview pour playActivity).
3. L'utilisateur a choisi une ressource en cliquant sur le bouton édition . L'éditeur par formulaire est ouvert -> cf **UC: editeur formulaire exo/activité**
4. S'il veut afficher le previeuw de la ressource en question, on clique sur le bouton preview -> **GUI: (pre)view**
5. S'il s'agit d'une création de ressource on définit le type de procédé à adopter sachant que la création par l'éditeur de code VSC n'est disponible que pour les ressources de type modèle. -> cf **GUI:selection du type de la ressource**
    - Par un **formulaire** : on sélectionne le modèle (Ressource de type modèle) à utiliser et le formulaire correspondant s'ouvre -> cf **UC: editeur formulaire exo/activité**
  - Par l'**import** -> cf **GUI: importation
  - Par l'**Editeur** de code VSC (**Visual Studio Code**) s'il s'agit d'un modèle
6. On valide après par le bouton de validation et s'il s'agit d'une création, la ressource est répertoriée au niveau de la liste des ressources du cercle, si c'était une édition, la ressource en question est mise à jour. 
7. Pour voir la liste des sauvegardes, cliquer sur le bouton à côté du bouton de sauvegarde(en mode édition) et cliquer sur une sauvegarde en particulier pour la visionner. 

## Post Conditions
### Conditions de succès 
Le prof a pu créer sa ressource et elle figure sur la liste des ressources du cercle en question
  
                    OU

Le prof a modifié la ressource et celle-ci est mise à jour et l'ancienne version figure sur la liste des sauvegardes

                    OU
                    
Le prof a pu faire sa sauvegarde et la précédente version figure sur les listes sauvegardes


### Conditions final en cas d'échec

Un pop up est renvoyé affichant l'erreur rencontrée -> cf **gui: pop-up-edit**

## Frequence

Une fois pour chaque sauvegarde 

            OU

Une fois pour chaque création de ressource

            OU

Une fois pour chaque édition

## Work Breakdown Structure
