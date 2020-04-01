
# Cas d'utilisation N° 86 :  optenir-bagde

Niveau 3

## Description

Les **[badges](https://github.com/PremierLangage/plconception/blob/master/conception/concept/badge.md)**   sont des récompense obtenues de diverses façons :
* Après avoir effectué une action
* Après avoir effectué une action un certain nombre de fois
* Remis manuellement par une personne autorisé à le faire

La remise manuelle peut être utile pour des actions ne pouvant être traitées par la plateforme, ou même des actions relatives à la plateforme, mais faites à l'extérieur de celle-ci (par exemple la participation à une convention IRL).

Certains badges peuvent avoir plusieurs niveaux. On peut imaginer des "points" associé aux badges / niveaux qui permettent de calculer un score pour l'utilisateur.

> **Niveau** : Haut niveau
> **Déclencheur** : Automatiquement après une action / Manuelle par une personne autorisé
> **Acteur Primaire**: Utilisateur  
 
 
## Preconditions
L'utilisateur est inscrit sur PLaTon.


## Scenario Nominal
1. Automatique
 1. L'utilisateur effectue une action.
 2. La plateforme enregistre cette action, celle-ci corresponds à un badge.
 3. Le badge est attribué à l'utilisateur
2. Manuelle
 1. Une personne autorisée décide que les actions d'un utilisateur mérite un badge.
 2. Cette personne remet le badge à l'utilisateur concerné
 
 FIXME : Décrire l'interface / le processus de remise manuelle de badge



## Post Conditions
### Conditions de succès 
L'utilisateur obtiens un nouveau badge.

### Minimal Guarantees
L'enregistrement de toutes les actions remarquable d'un utilisateur.

### Frequence
Tout le temps, la vérification étant faites à chaque action de l'utilisateur.

### Besoins Spéciaux
Il est nécessaire d'enregistrer chaque action faites par chaque utilisateur.
