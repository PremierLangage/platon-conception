
# Cas d'utilisation N° 24 :  crud-metadonnes-ressource

Niveau 1

##	Description

 Ici le cas d'utilisation explicite les informations que l'on peut modifier et comment 

1) Label du cercle (ajouter retirer un label du cercle)
2) status de publication 
3) tags scientifiques
4) Certains éléments techniques peuvent être stocké dans les méta-données 

Automatiques 
5) Information d'usage compilées une fois par an.



FIXME _[One to two sentences that briefly describe the use case, including the primary actor’s goal]_   
FIXME N'oubliez pas de mensioner le concept **[metadonnees](https://github.com/PremierLangage/plconception/blob/master/conception/concept/metadonnees.md)**  

> **Niveau** :Haut niveau, Résumé, objectif utilisateur, sous fonction, Bas niveau , FIXME Remove unused   
> **Déclencheur** : _[Describe the event that initiates the use case.]_ TODO  
> **Acteur Primaire**: Utilisateur   
> **Acteurs secondaires**: TODO   
> **Parties Prenantes concernées** : TODO   
 
 
## Preconditions

FIXME Listez les conditions nécessaire pour que ce cas d'utilisation puisse avoir lieux


## Scenario Nominal

1.	L'editeur de ressource propose un bouton "editer les méta données".
SI le membre click dessus. 
le système demande si c'est pour une version pariculière ou pour la dernière.
Le membre sélectionne la version de la ressouce pour laquel on souhaite editer les métadonnées.
le système lui affiche l'éditeur de métadonnées de la ressource.
2.	Cet editeur permet de modifier sans erreurs (les clefs sont prédéfinie), et le système n'accepte que des valeurs d'un type adapté et convertible en JSON.
3.	Une fois quel l'utilisateur sauvegarde ces données. Le système met a jour les métadonnées.
4.	le membre a modifier les métadonnées de la version de la ressource qu'il voulait modifier.

###	Extensions

Pouvoir choisir plusieurs ressources.
Par défaut si l'on édite pas les métadonnées elle sont les mémes que la version précédente de la ressource (récursivement, jusqu'a la valeur par défaut de la version zéro).



## Post Conditions
### Conditions de succès 
FIXME _[Describe the end condition of the Use Case where the Primary Actor’s goal is satisfied]_

### Minimal Guarantees
FIXME _[Describe the guarantee or assurance that this Use Case provides to all Actors and Stakeholders to protect their interest regardless of whether the Use Case ends with success or failure.]_

### Conditions final en cas d'échec
FIXME _[Describe the end condition that results if the Primary Actor fails to accomplish his goal.]_


FIXME _les variables suivantes sont optionnelles._

### Frequence
FIXME _[Indicate how often the use case is expected to occur. This information aids designers and developers in understanding capacity requirements.]_   
### Besoins Spéciaux (optionel)  
FIXME _[Describe any additional factors that impact the execution of the use case. These could be environmental, regulatory, organizational or market-driven in nature.]_  
### Performance  
###	Security  
###	Usability / Accessibility  
###	Other  

##	Problèmes et étapes suivantes  
FIXME _[Note any issues related to the definition of this use case that will require clarification prior to development. Also list any follow-up work that needs to be done prior to sign-off on the use case.]_  

FIXME définir ce qui pose problème dans la description **actuelle** du cas d'utilisation.  
FIXME vous pouvez ajouter ici un lien vers une issue github ou un carte de projet github.

TBR
