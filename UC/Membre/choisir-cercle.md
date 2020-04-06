
# Cas d'utilisation N° 13 :  choisir-cercle

Niveau 1

##	Description

Un utilisateur [membre](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Membre.md) du **serveur central** de ressources souhaite entrer dans un **cercle**. 

> **Déclencheur**: Dans le profile de l'utilisateur, il clique sur entrer dans un cercle.  
> **Acteur Primaire**: Le membre utilisateur souhaitant intégrer le **cercle**.   
> **Acteurs secondaires**: Le physionomiste du **cercle** en surveillant.   
> **Parties Prenantes concernées** : Les autres membres du cercle.      
 
 
## Preconditions

Être [membre](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Membre.md) du **serveur central** de ressources. Les ressources publiques étant placés dans des **cercles**, il vous faudra intégrer ces **cercles** pour éditer les ressources communes rattachées.

## Scenario Nominal

1.	Le système propose la liste des **cercles** (même truc que dans la crétion **cercle** de Adminsitrateur).
2.	L'utilisateur choisi un **cercle** dont les intérêts sont communs aux siens.
3.	La demande est envoyée comme une notification aux [physionomistes](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Physionomiste.md) du **cercle** (si l'intégration est soumise à approbation).
4. Le [physionomiste](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Physionomiste.md) valide l'entrée, l'utilisateur est inscrit dans le **cercle**.


###	Extensions

4. le cercle est a inscrition automatique (le **cercle** est ouvert à quiconque...).
