
# Cas d'utilisation N° 51 :  programmer-ressource

Niveau 1

##	Description
 
 Un membre (d'un cercle quelconque) souhaite programmer une **[ressource](https://github.com/PremierLangage/plconception/blob/master  /conception/concept/ressource.md)**, qui peut-être **1)** une ressource entièrement nouvelle, ou **2)**une **[version](https://github.com/PremierLangage/plconception/blob/master/conception/concept/version.md)** d'une ressource existante, ou **3)** une ressource nouvelle, créée à partir d'une ressource existante.
 
Si l'utilisateur programme une ressource à partir d'une ressource existante (cas **2** et **3**), alors la méthode est celle de la ressource en question. S'il crée une ressource entièrement nouvelle, il peut choisir, si cela s'applique, une méthode pour la créer.
Dans le cas d'un exercice, par exemple, il peut choisir d'utiliser un **[exercice_prepare](https://github.com/PremierLangage/plconception/blob/master  /conception/concept/exercice_prepare.md)**


 **Déclencheur** : Plusieurs point de départs possibles. L'utilisateur
 
 a. consulte une ressource
 
 b. consulte une liste de ressources
 
 c. consulte une **[demande](https://github.com/PremierLangage/plconception/blob/master  /conception/concept/demande.md)**
 
 Il choisit alors de programmer une ressource. Par exemple
 
 A. il consulte un **[cours](https://github.com/PremierLangage/plconception/blob/master  /conception/concept/cours.md)**, il souhaite programmer un **[exercice](https://github.com/PremierLangage/plconception/blob/master  /conception/concept/exercice.md)** pour ce cours, ou programmer une **[activité](https://github.com/PremierLangage/plconception/blob/master  /conception/concept/activite.md)** pour ce cours 
 
 B. il consulte une activité, il souhaite ajouter un exercice à l'activité.
 
 C. il consulte un exercice, il souhaite créer une version de cet exercice, ou en programmer un nouveau à partir de celui-ci.
 
 D. il consulte une demande, il souhaite créer une ressource qui réponde à cette demande
  
 **Acteur Primaire**: Utilisateur   

**Parties Prenantes concernées** : Dans le cas D. le créateur de la demande, qui est notifié.  Dans le cas d'une version d'une ressource existante, le créateur de la version précédente, qui est notifié. Dans tous les cas, le superviseur concerné qui doit valider le résultat final.


## Preconditions

L'utilisateur doit avoir l'autorisation nécessaire.


## Scenario Nominal

1.	Déclenchement (voir ci-dessus).  

2.	Choix d'une méthode d'édition (si applicable, et si on est dans le cas **1)**, ressource entièrement nouvelle).

3.	Si la méthode choisie requiert des paramètres supplémentaires, lien vers un formulaire adéquat. Par exemple si le choix est de programmer un exercice via un exercice préparé, le formulaire permet de choisir le modèle.

4. Un certain nombre de cycles édition/test/sauvegarde dans l'éditeur correspondant au type de ressource et à la méthode choisie.

5. Validation de la ressource programmée par l'utilisateur.


###	Extensions
4. L'utilisateur abandonne le processus. 

## Post Conditions
### Conditions de succès 
La ressource est créée et validée par l'utilisateur. Elle est sauvegardée et disponible pour être validée par des membres d'autorisation plus élevées, et pour être renseignée en métadonnées. 

### Minimal Guarantees
Dans tous les cas, le processus aboutit soit à la création d'une nouvelle ressource, soit laisse la base des ressources inchangée.

### Conditions final en cas d'échec
La base des ressources est inchangée.

### Frequence
Pas très fréquent.

##	Problèmes et étapes suivantes

Les scenarios sont multiples du fait des types ressources variés. Il faudrait préciser chaque cas **A)**, **B)**, **C)**, **D)** , éventuellement en ajouter d'autres, et préciser les métadonnées de la ressource programmée héritées du contexte dans lequel on a démarré.

On peut souhaiter, partant d'un exercice préparé, vouloir programmer un exercice en partant d'une description plus bas niveau de l'exercice de départ, mais c'est un scénario pour un version ultérieure, peut-être.


TBR
