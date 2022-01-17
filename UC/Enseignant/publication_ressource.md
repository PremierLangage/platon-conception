
# Cas d'utilisation :  publication d'une ressource ie passage d'une ressource à un asset

##	Description

On doit pouvoir passer d'une ressource à un asset en la publiant. 

> **Déclencheur** : Clic sur bouton publier
> **Acteur Primaire**: Professeur   
> **Acteurs secondaires**:    
> **Parties Prenantes concernées** : Professeur - Etudiant   
 
 
## Preconditions

Il faudrait que la ressource en question soit créée. 
L'acteur doit être loggé en tant que prof sur le cours où on veut ajouter la ressource. 


## Scenario Nominal

1.	Cliquer sur le gadget **+** à côté de la ressource en question  
2.	Déterminer le chemin vers le cours où on veut la publier  
3.	Déterminer la date de publication (champ opening de l'asset) et de fermeture (champ closing de l'asset) 
4.	Valider l'action  

## Post Conditions
### Conditions de succès 
La ressource est maintenant un asset du cours choisit et est accessible(visible) par les étudiants à partir de la date d'ouverture. La visibilité sera en off après la date de fermeture. 

### Frequence
Une fois pour chaque ressource publiée (asset)
