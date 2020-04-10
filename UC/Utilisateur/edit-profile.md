
# Cas d'utilisation N° 30 :  edit-profile

Niveau 1

##	Description

Permettre à un utilisateur de modifier ses informations de **[profile](https://github.com/PremierLangage/platon-conception/blob/master/concept/profile.md)** dans la base de données, ou de régler ses paramètres (mode daltonien, mode nuit, cercles etc..).
 
> **Déclencheur** : Lors d'un clique sur le bouton **Modifier** sur la page /profil.
> **Acteur Primaire**: membre   
> **Acteurs secondaires**: //   
> **Parties Prenantes concernées** :      
 
 
## Preconditions

1. L'utilisateur membre doit être connecté et sur la page /profil

## Scenario Nominal

1.	L'utilisateur clique sur le bouton **Modifier** de la page /profil
2.	Les champs deviennent modifiables (les modifications sont faites sur la même page pas de boîte de dialogue...)
3. Des boutons **Annuler** et **Enregistrer** apparaissent.
4. Les champs modifiables sont les suivants:
   FIXME indiquer les champs modifiables
5. Il clique sur le bouton Sauvegarder pour enregistrer les modifications dans la base.
6. Une notification apparaît indiquant si les modifications sont enregistrées ou pas.


### Cas d'Echec 

3. L'utilisateur clique sur le bouton annuler.
6. La notification indique que les modifications ne sont pas enregistrées.

## Post Conditions
### Conditions de succès 
Une notification indique que les informations sont enregistrées en base.

### Minimal Guarantees
Si les informations sont sauvegardés en base, ils le resteront et seront immédiatement appliquées.

### Conditions final en cas d'échec
Les informations saisies ne s'effacent pas si l'utilisateur n'a pas cliqué sur **Annuler** 

### Frequence
Rarement

### Besoins Spéciaux (optionel)  

##	Problèmes et étapes suivantes  
Définier la liste des champs modificables sur la page de profile. 

TBR
