
# Cas d'utilisation N° 4 :  aav-add-ressource

Niveau 1

##	Description

Un membre (d'un cercle quelconque) est en train de consulter une **[demande](https://github.com/PremierLangage/plconception/blob/master/conception/concept/demande.md)** (un aav). 
Il propose un lien vers une ressource pouvant répondre à l'aav.
 

> **Déclencheur** : le membre est en train de consulter une demande

> **Acteur Primaire**: membre  
> **Acteurs secondaires**: le demandeur   
> **Parties Prenantes concernées** : les membres surveillants la demande en question (notification?)
 
 
## Preconditions

- une demande (crud-aav) a été faite


## Scenario Nominal


1.	le système affiche la demande
2.	l'utilisateur clic sur le bouton (ajouter une réponse)
3.	cela conduit à une view dans laquelle il y a le champ de réponse et moteur de recherche
4.	l'utilisateur fait sa recherche, sélectionne une ressource et crée un lien vers la ressource en faisant un commentaire
5. il valide;
6. Le système lui affiche le lien interne de la ressource et le commentaire
7. Une notification est envoyée au demandeur et aux personnes qui suivent la demande. 

###	Extensions
6. l'utilsateur n'est pas satisfait et il peut retourner en 4. (un bouton)


## Post Conditions
### Conditions de succès 
Le lien sur la ressource et le commentaire sont enregistés dans la base de données;
Les notifications ont été envoyées; 


### Frequence
Un cas simple d'utilisation. 



## Besoins du cas d'utilisation 

FIXME 
