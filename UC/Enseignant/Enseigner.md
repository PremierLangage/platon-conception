
# Cas d'utilisation N° 36 :  Enseigner

Niveau 1

##	Description

Activité principal de l'enseignant. 
L'enseignant choisi la classe dans la quelle il souhaite travailler.
La classe s'ouvre et l'interface de classe est affiché par le système.
l'enseignant peut travailler.


> **Déclencheur** : Soit une arrivé par lti (choix dans le profile d'avoir la page des cours comme page d'acceuil).  
> **Acteur Primaire**: Enseignant   
> **Acteurs secondaires**: -
> **Parties Prenantes concernées** : Etudiants    
 
 
## Preconditions

L'enseignant est loggé et il a au moins une classe de créée. 

## Scenario Nominal



1.	La page d'acceuil "Classes" du serveur d'asset de l'esneignant est affichée.
Cette page d'acceuil propose un bouton (text ou icone ou image) pour chaque classe. Et une information est affiché sur chaque cours voir scéma [ Notification et avancement ](https://github.com/PremierLangage/plconception/blob/master/conception/casutilisation/enseignant/ihm/starting-teacher.pdf). 
2.	L'enseignant choisi en clickant sur le bouton du Classe. Celui dans lequel il souhaite travailler.
3.	le système affiche la page de la Classe.

###	Extensions
1. Un bouton permet la création de classe dans platon (mais pas pour la version 1.0 ???)
Ce qui permet le lancement de la création d'une classe. 

## Post Conditions
### Conditions de succès 
L'enseigant est sur la bonne page du site. 

### Frequence
A chaque fois que l'enseignant exige de se connecter a une de ses classes. 
### Besoins Spéciaux (optionel)

le type classe doit contenir des variables: text ou icon ou image pour l'affichage dans la page d'acceuil. 
les notification spécifiques à une classe sont identifiables. 
la classe peut fournir un indicateur d'avancement numérique simple. 

### Performance 
Il ne faut pas que le calcul de l'indicateur d'avancement soit couteux en temps de calcul.


FIXME **le cas d'usage d'enseigner dans une classe n'est pas défini**  


