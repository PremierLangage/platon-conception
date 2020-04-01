
# Cas d'utilisation N° 96 :  inscription-etudiant-classe

Niveau 4

## Description

L'enseignant doit pouvoir ajouté des étudiants à une **[classe](https://github.com/PremierLangage/plconception/blob/master/conception/concept/classe.md)** de deux façon :

1. Depuis le panneau de gestion de sa classe sur PLaTon
2. En créant une activité LTI sur un LMS.

> **Niveau** : Haut niveau
> **Déclencheur** : /
> **Acteur Primaire**: Utilisateur
 
 
## Preconditions

L'enseignant doit avoir accès à une classe sur PLaTon et les droits sur celle-ci.

FIXME Quelques questions
FIXME Ou est le bouton ajout d'étudiant ? C'est une view spéciale 
FIXME dans quoi sont trouvé les etudiants qui remplissent la liste du menu déroulant

## Scenario Nominal
* A
    1. L'enseignant clique sur le bouton d'ajout d'étudiant dans son cours
    2. Il choisit le/les étudiant dans un menu déroulement, une barre de recherche est disponible
    3. Il valide le/les étudiant séléctionnés
* B
    1. L'enseignant copie le lien vers sa classe PLaTon
    2. L'enseignant créer une activité LTI sur LMS à l'aide du lien copier
    3. Un élève clique sur l'activité LTI sur le LMS


## Post Conditions
### Conditions de succès 
Le/les étudiants sont ajoutés au cours.

### Minimal Guarantees
/

### Conditions final en cas d'échec
L'étudiant n'est pas ajouté à la classe.

### Frequence
Souvent. 
Peut devenir fastidieux si il y a plusieurs centaines d'étudiants à inscrire.
FIXME peut on proposer une version avec un upload de la liste ??


