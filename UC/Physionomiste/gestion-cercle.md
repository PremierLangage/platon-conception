
# Cas d'utilisation N° 39 :  gestion-cercle

Niveau 1

##	Description

 Possibilité de jetter/banir/rendre muet retirer les droits etc bien entendu changer les droits 

> **Déclencheur** : Les physionomistes d'un cercle on accès a une view de gestion. 
> **Acteur Primaire**: physionomistes   
> **Acteurs secondaires**: Membre   
> **Parties Prenantes concernées** : Membre   
 
 
## Preconditions

être le physionomiste d'un cercle


## Scenario Nominal

1.	Le système affiche la liste des cercle pour lesquels l'acteur est physionomiste. 
le physionomiste choisi le cercle dans lequel il souhaite effectuer une opération.
2 Le système affiche une liste des listes d'utilisateurs:
- demandeurs (suf si le cercle accepte automatiquement les utilisateur non bannis).
- membres actuels
- membres bannis 
Devant chaque nom d'utilisateur il y a des boutons:
accepter rejetter demande.  
renvoyer bannir membre 
blanchir banni
3.	Le physionomiste choisi toutes les modifications qu'il souhaite faire. Puis valide / cancel.
4. Si c'est une validation le système met à jour toutes les listes et envois des notifications aux personnes concernées.


## Post Conditions
