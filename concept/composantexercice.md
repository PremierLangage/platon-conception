
## Composant angular d'exercice 


Dans premier langage nous avons mis en place des composants angular pour structurer les inputs et interaction des exercices.

Dans platon nous organisont deux niveau de composants:
les composants exercices et les composants inputs.

Les composants exercice ont pour responsabilité d'adapter le comportement de l'exercice à la situation ou il est utilisé.

Ce document s'inspire du document suivant:  https://docs.google.com/presentation/d/1M3qN693xb-Xn04Y2UjLrFtTXEoBVi7UvyRA-hTI3D3Q/edit?usp=sharing


## Les composant angular d'exercice et les modes 

Le mode d'utilisation de l'exercice indique dans quel contexte il est utilisé.

### Mode : Edition 

Mode accessible uniquement dans les ressources, le mode edition utilise un model d'exercice pour produire un exercice. 
IL permet de faire des exercices préparés à la mode WIMS.


### Mode Test (Preview)

Mode accessible uniquement dans les ressources, le mode test permet de valider un exercice.
Le mode test permet d'afficher toutes les informations sur l'exercice, 
un onglet permet d'avoir un pretty print du JSON actuel de l'exercice,
un onglet permet de tester le grader avec une réponse exact ou une fausse 
un onglet permet de lancer ou d'enregistrer un test (remplir la réponse vérifier que le grader retourne la bonne réponse).

L'idée du test c'est que l'on enregistre un ou plusieurs comportement (grade,feedback,etc. en fonction d'une entrée et que cela nous donne un test de nom regression).
Le fichier test.pl dans la ressource enregistre les tests sous forme de json.


### Mode Démo 

Le mode démo est un mode run avec une personne non identifié. Donc pas de mode spécifique. 

### Mode Play

Mode d'Utilisation standard l'exercice est présenté avec  la possibilité de répondre.

C'est le mode 'actif' de PL quand l'utilisateur intéragit avec l'exercice.

Le mode Play utilise des composants Platons (inputs, graphics, hints, etc). 



### Mode Answer 

Mode ou l'énoncé est affiché et la réponse d'un utilisateur est affichée.
Le mode answer doit être associé a des composants de correction:
1) champ text libre 
2) Note 
3) Grille 

Les informations de correction sont sauvé avec la réponse de l'utilisateur.

### 



