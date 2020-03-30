
# Cas d'utilisation N° 16 :  connection-lti

Niveau 1

## Description

L'utilisateur se connecte à la plateforme depuis un LMS en cliquant sur une activité [lti](https://github.com/PremierLangage/plconception/blob/master/conception/concept/lti.md).

> **Niveau** :Haut niveau
> **Déclencheur** : Cliquer sur une activité LTI depuis un LMS.  
> **Acteur Primaire**: Utilisateur  
 
 
## Preconditions

Avoir créée une activité LTI correspondant à PLaTon.

## Scenario Nominal

1.	L'utilisteur clique sur l'activité LTI depuis un LMS.
2.	Le LMS redirige l'utilisateur sur PLaTon.
3.	Si besoin, PLaTon crée l'utilisateur avec les informations de la requête.  
4.	L'utilisateur est authentifié sur PLaTon.  

### Extensions

2.	Le LMS redirige l'utilisateur sur PLaTon.
3. Les identifiants LTI ne sont pas valide, PLaTon refuse la connexion.

*Remarque :* Si un même utilisateur se connecte à un même serveur depuis plusieurs LMS différents, un compte différents sera créer sur PLaTon pour chaque LMS.


## Post Conditions
### Conditions de succès 
L'utilisateur est correctement authentifié sur PLaTon.

### Minimal Guarantees
Création d'un compte associé à l'utilisateur du LMS.

### Frequence

Une fois pour chaque nouvelle session utilisateur.

### Besoins Spéciaux
Disponibilité d'un LMS.
