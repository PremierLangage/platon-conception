
# Cas d'utilisation N° 80 :  crud-badge-createur

Niveau 3

## Description

L'administrateur doit avoir la possibilité de créer des badges. Il doit pour cela lui être possible de choisir une ou plusieurs actions, de les associé a des conditions et de lié plusieurs action ensemble avec des connecteurs logiques.

Des exemples :

|          actions           |      conditions      | connecteurs logiques |
|----------------------------|----------------------|----------------------|
|Créer une ressource         |`X` fois              | OU                   |
|Suivre un cours             | Pour la première fois| ET                   |
|Se connecter à la plateforme| `X` fois à la suite  | ...                  |
|Réussir un exercice         | ...                  |                      |
|...                         |                      |                      |

Des examples de badges seraient :
* Se connecter à la plateforme **10** jours.
* Réussir **100** exercice `OU` réussir un exercice **10 à la suite**.
* Se connecter à la plateforme **pour la première fois** `ET` réussir un exercice  **pour la première fois**.

Toutefois, comme détaillés dans [obtenir-badge](https://github.com/PremierLangage/platon-conception/blob/master/UC/Utilisateur/obtenir-badge.md), il faut permettre la création de badge *ad-hoc* à remettre manuellement pour permettre par exemple la remise de badge pour action extérieur à la plateforme.

Il est possible que certain grade ait des niveaux (faire 10 fois X, 100 fois X...).

Enfin, il peut être intéressant de fournir une valeur en points aux badges, afin de mettre à valeur les badges les plus rares. La somme total des points des badge pourrait servir à débloquer des features, ou tout simplement de *bragging rights*.


> **Acteur Primaire**: Administrateur 
> **Acteurs secondaires**: Utilisateurs 
 
 
## Preconditions
Toutes les actions faites par les utilisateurs doivent être enregistrées.

## Scenario Nominal

* L'administrateur clique sur le bouton de création de badge.
* Il choisie entre un badge à action ou un badge *ad-hoc* grâce à deux bouton radio
    * Si un badge *ad-hoc* est choisi, il rentre un titre, une description, une image ainsi que le nombre de points que vaut le badge.
    * Pour un badge à action, l'administrateur doit choisir au moins une action, et avoir la possibilité d'en ajouter d'autres en les liants par des connecteurs logiques. Chaque action doit avoir une conditions associées. Il rentre ensuite un titre, une description, une image ainsi que le nombre de points que vaut le badge.
* L'administrateur valide la création du badge à l'aide d'un bouton correspondant.
* Le badge est crée.
* La plateforme (ou un serveur de stats associé, et possiblement différé) vérifie que certains utilisateur ne vérifie pas déjà les conditions afin de possiblement leur remettre le badge.

### Extensions

* L'administrateur clique sur le bouton de création de badge.
* L'administrateur annule la création du badge à l'aide d'un bouton associé.

## Post Conditions
Le badge est créé et les utilisateurs remplissant les conditions reçoivent le badge.

### Frequence
Quelques fois par ans.
