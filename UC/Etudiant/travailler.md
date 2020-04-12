
# Cas d'utilisation N° 57 :  travailler

Niveau 1

##	Description

 Travailler pour un étudiant doit couvrir l'ensemble de l'interface utilisateur de l'étudiant.
 
 Objectifs de l'étudiants:
 - apprendre = acquerir des AAV, réaliser des activité avec succès
 - atteindre des objectifs pour obtenir des validations (diplomes)
 - participer à un enseignement (Forum, notification, dates limites, dates d'ouverture)
 - communiquer avec les enseignants et les autres élèves: notifications
 - travailler en groupes (plugapps, 2.0), communication orale visio, documents partagés,  
 - construire son portfolio (2.0) 
 - Fournir des travaux au système
 - améliorer sa métacognistion et learn how to learn.
 
 
 **[actions,activity,data-activity,classe,aav,assets](https://github.com/PremierLangage/plconception/blob/master/conception/concept/actions,activity,data-activity,classe,aav,assets.md)**  

> **Déclencheur** : connexion à la plateforme avec un compte étudiant (lti, login)
> **Acteur Primaire**: Etudiant 
> **Acteurs secondaires**:   Enseignant
> **Parties Prenantes concernées** : Responsable de formation   
 
 
## Preconditions

L'étudiant a été préalablement inscrit dans un LMS qui est connecté à la plateforme.
L'étudiant est inscrit dans un cours dans lequel, l'enseignant a mis un liens LTI dans les activités du LMS. 

## Scenario Nominal

1.	le système affiche la page d'acceuil des etudiants, avec les informations personnel de l'étudiant, nom de login en haut a droite, les notifications. Les liens des différents cours auquel l'etudiant participe sur la plateforme.  
2.	L'etudiant choisi un cours.
3.	le système passe sur la page d'acceuil du cours pour les étudiants.
4.	L'etudiant choisi une des activités du cours.
5. Le système affiche l'activité et interagi avec l'etudiant voir le cas d'utilisation: [réaliser-activité](réaliser-activité.md)
6. l'étudiant se déloge et a fait ce qu'il souhaitai.

###	Extensions

- Notifications 
2. l'etudiant choisi de regarder ses notifications. [afficher-notifications](../Utilisateur/afficher-notifications.md)

- Réseau social 
3.l'etudiant choisi de rejoindre le réseau social du cours. A faire. 

- Notes 
4. l'etudiant choisi de voir l'avancement dans le cours et son positionnement par rapport à la promotion dans laquelle il est. [afficher-completion](afficher-completion.md)




## Post Conditions

l'etudiant est connecté et est arrivé à réaliser un de ses objectifs


### Frequence
Utilisation a haute fréquence, le logiciel doit être agréable et réactif.

### Besoins Spéciaux (optionel)  

L'interface doit fonctionner sur un smartphone de façon parfaite, exigence moins forte pour les exercices car pas toujours possible.


TBR
