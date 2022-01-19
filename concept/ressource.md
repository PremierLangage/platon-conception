
# Ressources 

Structure d'informations pouvant être transformée en asset et gérant le fait qu'un élément de la plateforme doit avoir un certain nombre de propriétés pour être partageable.

Les ressources sont à priori **éditables**, **partagées**, **versionnées**. 
Deux grand types :

- binaires, non éditables mais modifiables dans un editeur externe, il faut téléverser le document pour le remplacer. 
- textuelles, éditables directement sur le site il est bien sur aussi possible de téléverser un document pour le remplacer.


Les ressources peuvent être transformées en [assets](assets.md) par une [publication](publication.md) dans un [cours](cours.md). 

Les [assets](assets.md) sont directement utilisables par les apprenants s'ils sont dans le contexte d'un cours.

Rem: il est possible de produire des assets de démonstration qui sont accessibles sur le site principal [demo](demo.md)


## Propriétées des ressources 

l'implémentation doit choisir comment sont stocker les différentes propriétées. 

Une ressource, existe dans l'aroborescence des cercles sous forme d'un répertoire contenant:
- un fichier json type.json qui décrit le contenu technique de la ressource.
- un fichier content

Les ressources éditables ont:

- une structure de stockage (apriori un **repertoire** avec un **main.pl** et des fichiers de données + fichier de meta data)
- des dépendances: information sur les versions des ressources liées.
- des utilisateurs/propriétaire/observateurs/editeurs/
- un historique de modification (utilisateur, timestamp, modification)
- un classement dans Yggdrasil (ensemble d'étiquetages obligatoires)
- des aav auquels la ressource participe
- une discution (eventuellement une page loomio)



## Propriétés pédagogiques 

- usages possible de la ressource, présentiel, online
- répétabilité, longueur de la répétabilité
- type: acquisition, discution, collaboration, entrainement, production
- utilisable ou non pour une évaluation


## Les ressources PL 

Les ressources PL sont stockées dans une arborescence versionnée. 

Chaque ressource est un répertoire git, chaque sauvegarde est taggée et il est possible d'ajouter des étiquettes.

https://www.ubuntupit.com/best-cloud-storage-for-linux-15-reviewed-and-compared-for-linux-nerds/

Les ressources sont des objets de la base de donnée :

1. Une référence sur la dernière version de la ressource et la possibilité de remonter dans les versions … (diff, voir la version , voir le patch) … avoir la date et l’utilisateur … blâme/praise 
2. Meta Data
    1. Statut d’usage (ne pas utiliser, exam, jamais servi, une classe, classes multiples)
    2. Héritage, dépendances, bundle 
    3. Statistiques json complexe voir module de stats 
        1. Nombre de classe utilisant 
        2. Nombre d’utilisation 
        3. Exercices 
            1. Nombre d’essai moyen pour réussir
            2. Taux de réussite 
    4. Labels: (open ended)
        1. Label Rouge
        2. Label Upem
        3. Label Euler
 

## types des ressources PL 
- exercices INFORMATIONS : Fichiers text / pdf / video/ podcast /autres formats non modifiable sur la plateforme 
- Liens vers des documents externes (i.e. pas stockés sur la plateforme (la question du cache ? pour assurer l'existance ? ))
- Tout les types Exercices: avec les codes et données (func.py, valeurs.csv) 
- Tout les types Activités en particulier : Sections/chapitres/cours/listes_de_ressources 
- Protocoles de validations (i.e. activités couplés présentiel / plateforme)




