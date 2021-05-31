
# Cas d'utilisation N° 72 :  Faire-un-test

Niveau 2

##	Description

Permet d’envoyer a un candidat une feuille d’exercice à usage unique pour laquelle on récupère l’évaluation.


**Déclencheur** : Le candidat recois un test sous forme d'un liens sur la plateforme.  
**Acteur Primaire**: Candidat. 
**Acteurs secondaires**: Membre (responsable de formation) 
**Parties Prenantes concernées** : Université
 
 
## Preconditions

Le cas d'utilisation [membre fairepassertest](../Membre/fairepassertest.md) est un prérequis.


## Scenario Nominal

le prof créer un cours FORMATION_X
le prof créer une activité de type CANDIDATURE remplie le formulaire fournis les exercices.


- lien a usage unique, question d'entrée dans le test (date de naissance, numéro de téléphone), double identification (vérification avec sms).
- Validation d'un document fait sur l'honneur que le candidat répondra lui même et seul au test, et qu'il repassera un test du même niveau en arrivant dans la formation pour valider que c'est bien lui qui à passé le test.


1.	Le candidat click sur le lien/ le cole dans son navigateur. 
2.	Le système vérifie que le lien n'a pas été utilisé (test commencé dans une autre session au dela de la question de controle de démarage et une fois que le cronomètre est lancé). Si oui fin du cas d'utilisation (avec un message au candidat qui peut envoyer un mail si il pense être lésé). 
3. Sinon le système affiche la question de controle.
4.	Le candidat répond à la question de controle (secret partagé).  
5. le système vérifie la question de controle. Si fausse retour en 4 (max trois essais). 
 Sinon  le système affiche la page d'engagement sur l'honneur, voire plus bas.
6. le système lance un cronomètre et l'activité associé au test avec la clef d'accès.
7. Interaction du candidat avec l'activité. Compteur de temps visible.
Tout les résultats intermédiaires sont enregistrés (answers ou playexo). 
8. a la fin du temps, l'activité se termine automatiquement avec validation automatique des derniers éléments.

 
 
 
###	Extensions
Controle durci  
Le pltp qui correspond ne doit afficher les exercices dans la navigation que 5 par 5 (i.e. 5/10/15/20 exos dans la navigation). si au moins un exercice du paquet précédent est correct. sinon c'est la fin. 

Changement de page du navigateur, pour ne pas perdre les données si l'on fait un retour arrière. on doit protéger la sortie de l'activité.





## Post Conditions
### Conditions de succès 
Une fois le temps imparti terminé le test se termine automatiquement et les données de réussite sont sauvegardées 


### Minimal Guarantees

Si deux exemplaires de la feuille avec la même clef sur des machines (ip) différentes -> fin de la session.


### Conditions final en cas d'échec
Quels sont les echecs ??? FIXME 


### Frequence
Pour 1000 candidats pour le même diplome ...

### Besoins Spéciaux (optionel)  

Attention aux problèmatiques de cryptage. 


### Performance 
La Fiabilité du test est très important pour le candidat ...

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

