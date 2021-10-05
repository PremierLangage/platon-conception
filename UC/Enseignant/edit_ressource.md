# Cas d'utilisation : Mettre au point une ressource
  
## Description

Un membre appartenant à un cercle doit pouvoir créer des ressources dans ce cercle ou éditer les ressources qui existent déjà. 

> **Déclencheur** :

  - Création de ressources : cliquer sur bouton + pour créer une nouvelle ressource
  - Edition d'une ressource : cliquer sur la ressource à éditer pour modifier les paramètres de la ressource 
  
> **Acteur Primaire** : Membres d'un cercle
> **Acteurs secondaires** : -   
> **Parties Prenantes concernées** : -

## Preconditions

- L'utilisateur est authentifié sur la plateform web  -> cf **UC: connexion**
- L'utilisateur est un membre et appartient à un cercle

## Scenario Nominal

1. L'utlisateur choisit le cercle dans lequel il veut créer ou éditer sa ressource
2. S'il s'agit d'une édition de ressource l'utilisateur clique sur la ressource en question. Les champs éditables à l'écrit pourront être modifié à la main (nom, etc)
3. L'édition peut se faire par un formulaire ou directement par VSC (Visual Studio Code) s'il s'agit d'une ressource de type modele . On choisit le procédé voulu
  -  Si par formulaire, on remplit les champs au fur et à mesure 
  -  Si par VSC, on est directement renvoyé vers l'éditeur de code VSC 
4. S'il s'agit d'une création de ressource on définit le type de procédé à adopter sachant que la création par l'éditeur de code VSC n'est disponible que pour les ressources de type modèle.
  - Par un formulaire : on remplit les champs au fur et à mesure  
  - Par l'import d'une ressource template déjà fait et remplir un mini formulaire pour adapter le template
  - Par VSC
5. On valide après par le bouton de validation et s'il s'agit d'une création, la ressource est répertoriée au niveau de la liste des ressources du cercle, si c'était une édition, la ressource en question est mise à jour. 
6. Pour voir la liste des sauvegardes, cliquer sur le bouton à côté du bouton de sauvegarde(en mode édition) et cliquer sur une sauvegarder en particulière pour la visionner. 

## Post Conditions
### Conditions de succès 
Le prof a pu créer sa ressource et elle figure sur la liste des ressources du cercle en question
  
                    OU

Le prof a modifié la ressource et celle-ci est mise à jour et l'ancienne version figure sur la liste des sauvegardes

                    OU
                    
Le prof a pu faire sa sauvegarde et la précédente version figure sur les listes sauvegardes


### Conditions final en cas d'échec

Un pop up esst renvoyé affichant l'erreur rencontrée -> cf **gui: pop-up-edit**

## Frequence

Une fois pour chaque sauvegarde 

            OU

Une fois pour chaque création de ressource

            OU

Une fois pour chaque édition

## Work Breakdown Structure
