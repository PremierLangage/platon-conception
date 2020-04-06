
# Cas d'utilisation N° 2 :  interagir-exercice

Niveau 0

##	Description

 ce cas est le plus important

> **Déclencheur** : l'étudiant loggé cick sur une activité 
> **Acteur Primaire**: Etudiant   
> **Acteurs secondaires**: Pour certaines activités l'enseignant peut intervenir 
> **Parties Prenantes concernées** : - 
 
 
## Preconditions

1) l'étudiant est un utilisateur identifié de la plateforme, login. 
2) l'étudiant a commencer le cas d'utilisation Apprendre/travailler 
3) l'étudiant a choisi l'activité 



## Scenario Nominal

1. le système affiche la page d'acceuil de l'activité :
- la navigation
- la page d'acceuil (par exemple information dans un pltp).
2. L'etudiant démarre l'activité. 
3.	Le système enregistre la date de démmarage, dans la session activité.
  Et propose la première ressource de l'activité (qui peut êttre une activité).
  La ressource est affiché (prend éventuellement toute la page).
  le système enregistre la date de présentation de l'exercice, dans la session exercice.
4. l'etudiant interagis avec l'activité.
 Le système enregistre Les interactions dans la session exercice:
 les réponces, le grade, la seed etc. le temps. 
 Le système enregistre les statistiques modifiées de l'activité dans la session activité.

###	Extensions

1. Ce n'est pas la première fois que l'étudiant se connect à l'activité il est donc directement, placé sur le sous élément sur lequel il travaillais la dernière fois.

### Problèmatiques 

il faut faire attention aux modalité d'enregitrement des statistiques d'utilisation. 

