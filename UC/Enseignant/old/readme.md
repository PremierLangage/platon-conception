
# Les cas d'utilisations pour l'enseignant

le responsable de formation créer un cours et affecte un enseignant responsable. (par le truchement d'un LMS).

## La mission d'enseignement 

1) Ecrire le descriptif du cours.
2) Ecrire les objectifs de formation du cours. 
3) Organiser le cours (contenus, ordonancement, dates, heures, rendus, livrables, etc).
4) Ajouter des assets au cours.
5) Suivre une activité.
6) Exporter des notes.
7) Evaluer une activité un asset.
8) Faire un amphi dynamique.
9) Suivre les étudiants.
10) Faire le bilan du cours.

## Les enseignants comme membre. 

Les enseignants sont membre d'au moins un cercle ce qui leur permet d'ajouter des assets dans leur cours. Voire la discription des membres. 
1) importer des ressources. Ce role est spécifique aux membres qui sont enseignants.



## Plantuml

@startuml
actor Enseignant as ens


usecase "travailler" as trav
ens --> trav

usecase "Evaluer" as eval #red
usecase "coacher" as coach
usecase "enseigner" as teach
usecase "archiver-cours" as archi

usecase "editer-cours" as editcourse
usecase "exporter-notes" as exnote
usecase "exporter-stats" as exstat



trav --> eval
trav --> teach
trav --> coach
trav --> archi
archi --> exnote 
archi --> exstat

usecase "Utiliser une activité" as usepla #red

usecase "motiver recadrer" as foueter
usecase "consulter-indicateur-individuel-collectif" as con
usecase "afficher-completion" as affcomp

coach <-- foueter
usepla --> con :<uses>
usepla --> affcomp :<uses>

usecase "choisir-visibilité-completion" as chviscom
usecase "asset-metadata-edition" as asseme
teach --> asseme :<uses>
asseme --> chviscom :<uses>

coach --> usepla : <uses>
teach --> usepla : <uses>
teach --> editcourse : <uses>
eval --> usepla

usecase "editer-modalités-completion" as emc
usecase "modifier-completion" as mc
asseme --> emc : <uses>
asseme --> mc : <uses>

@enduml
