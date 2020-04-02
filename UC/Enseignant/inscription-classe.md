
# Cas d'utilisation N° 96 :  inscription-etudiant-classe

Niveau 4

## Description

L'enseignant doit pouvoir ajouté des étudiants et enseignant à une **[classe](https://github.com/PremierLangage/plconception/blob/master/conception/concept/classe.md)** de deux façon :

1. Depuis le panneau de gestion de sa classe sur PLaTon
2. En créant une activité LTI sur un LMS.

> **Niveau** : Haut niveau
> **Déclencheur** : L'enseignant sélectionne le paneau de gestion 
> **Acteur Primaire**: Utilisateur
 
 
## Preconditions

L'enseignant doit avoir accès à une classe sur PLaTon et les droits sur celle-ci.

## Scenario Interne Nominal
1. Depuis le panneau de gestion de sa classe sur PLaTon
    1. L'enseignant clique sur le bouton d'ajout d'étudiant dans son cours
    2. Un popup s'ouvre avec la liste des étudiants inscrit sur PLaTon.
    2. Il choisit le/les étudiant dans un menu déroulement, une barre de recherche et des filtres sont disponibles. On peut aussi imaginé la possibilité d'ajouer plusieurs étudiant d'un coup en important un csv où en copiant une liste d'étudiant.
    3. Il valide le/les étudiant séléctionnés

## Scenario LTI nominal
1. En créant une activité LTI sur un LMS.
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
Inscription simultanés de plusieurs centaines d'étudiant à prévoir.


