
# Cas d'utilisation : validation-cercle

Niveau 1

##	Description

La création des cercles ce fait par une demande a un administrateur qui valide la création du **[cercle](https://github.com/PremierLangage/plconception/blob/master/conception/concept/cercle.md)** .

> **Déclencheur** : l'Administrateur recoit une notification  
> **Acteur Primaire**:  Administrateur   
> **Acteurs secondaires**: -   
> **Parties Prenantes concernées** : Les membres
 
 
## Preconditions

l'Administrateur est loggé. Il a reçu une notification.

## Scenario Nominal


1. l'administrateur suis le lien de la notification de creation de cercle.  
2.	Le système lui propose trois choix:  
- valider telquel la demande de création (si il ya bien trois personnes différentes qui sont enseignants).
- valider l'affectation du cours dans le cercle demandé.
- affecter le cours dans un cercle existant (pas celui demandé en création).le système propose une liste déroulante des cercles existant (ou mieux)
3. l'admistrateur fait le choix. 
4. le système créer le cercle si nécessaire avec les toutes les affectations de membres et notifie les trois membres initiaux de la création. Le cours est associé au cercle et devient visible dans la liste de cours du cercle. l'enseignant si il nétait pas membre du cercle le devient. 
5. l'enseignant recoit une notification lui dissant dans quel cercle est affecté sont cours.

## Post Conditions
### Conditions de succès 
Le cours est affecté à un cercle. la notification disparait.

### Conditions final en cas d'échec
La notification n'est pas détruite dans la liste de l'administrateur.

### Frequence
Une fois pour chaque création de cours.

