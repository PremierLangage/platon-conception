
# Cas d'utilisation N° 91 :  auto-inscription-classe

Niveau 4

##	Description

 v1.0 passage par moodle 

**Déclencheur**: Quand un utilisateur click sur un liens vers platon a partir d'un LMS
**Acteur Primaire**: Utilisateur   

 
 
## Preconditions

Le LMS doit être identifié dans platon. La pair identifiant mot de passe doit être mis dans la table des LMS autorisés.



## Scenario Nominal

1.	l'administrateur a mis le LMS dans la table.
2.	L'enseignant a placé un lien LTI dans son cours qur le lms.  
3.	l'utilisateur le clic.
4. Test d'existance de l'utilisateur si non création du compte
5. Test d'existance du cours -> si cours inexistant et utilisateur "teacher-lti" -> création du cours.
6. Test d'inscription de l'utilisateur au cours si non inscription au cours.
7. Si c'est la première connection lancer le tutoriel et faite remplir le profile.
8. pour finir l'utiulisateur est connecté avec le bon droit (prof,élève) au cours sur platon.

###	Extensions

Au point 4 on doit demander si l'on a pas déjà une connection a platon par un autre biais. Autre académie /université etc. Pour ne pas créer plusieurs foit le meme utilisateur.

Le tutoriel est une activité ouverte a tous en mode démo.

## Post Conditions
### Conditions de succès 

Le crous et l'utilsateur existent sur platon et l'utilisateur est connecté.


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
