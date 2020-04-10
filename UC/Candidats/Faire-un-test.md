
# Cas d'utilisation N° 72 :  Faire-un-test

Niveau 2

##	Description

Permet d’envoyer a un candidat une feuille d’exercice à usage unique pour laquelle on récupère l’évaluation.


> **Déclencheur** : Le candidat recois un test sous forme d'un liens sur la plateforme. 
> **Acteur Primaire**: Candidat. 
> **Acteurs secondaires**: Membre (responsable de formation) 
> **Parties Prenantes concernées** : Université
 
 
## Preconditions

Le cas d'utilisation [membre fairepassertest](../Membres/fairepassertest.md) est un prérequis.


## Scenario Nominal



- lien a usage unique, question d'entrée dans le test (date de naissance, numéro de téléphone), double identification (vérification avec sms).
- Validation d'un document fait sur l'honneur que le candidat répondra lui même et seul au test, et qu'il repassera un test du même niveau en arrivant dans la formation pour valider que c'est bien lui qui à passé le test.


1.	Le candidat click sur le lien/ le cole dans son navigateur. 
2.	Le système vérifie que le lien n'a pas été utilisé (test commencé dans une autre session). Si oui fin du cas d'utilisation. 
3. Sinon le système affiche la question de controle.
4.	Le candidat répond à la question de controle.  
5. le système vérifie la question de controle. Si fausse retour en 4 (max trois essais). 
 Sinon  le système affiche la page d'engagement sur l'honneur, 
 
 
 
###	Extensions
FIXME Moins bien _[Document alternate flows and exceptions to the main success scenario. Extensions are branches from the main scenario, and numbering should align with the step of the success scenario where the branch occurs.]_

FIXME Indiquez dans quel point du scenario nominal le chemin alternatif démarre et ou il reprend.


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


"""
aujourd'hui {{date}} 


Objet : déclaration sur l’honneur

Madame, Monsieur,

Je soussigné {{nom}} {{prenom}}, née le {{datenaissance}} à {{villedenaissance}}  atteste sur l’honneur 
**Que je passe le test suivant seul (sans aide), en personne (pas quelqu'un d'autre), et aujourd'hui {{date}}** 
J'ai connaissance qu'un test de niveau me sera exigé en présentiel si mon dossier est accepté.
Et qu'un échec à ce second test pourra invalider mon inscription si le résultat de celui ci est trop inférieur au présent test que je passe aujourd'hui.
Que toute tentative de passer plusieurs fois le test dans une même session de sélection est éliminatoire.
J’ai connaissance des sanctions pénales encourues par l’auteur en cas de fausse déclaration sur l’honneur.

Fait pour servir et valoir ce que de droit.

"""

