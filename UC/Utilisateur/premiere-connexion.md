
# Cas d'utilisation N° 48 :  premiere-connexion

Niveau 1

## Description

Grâce à [lti](https://github.com/PremierLangage/plconception/blob/master/conception/concept/lti.md, la plateforme peut récupérer les principales informations concernant l'utilisateur, à savoir :

* Nom / Prénom
* Mail
* Langage

Voir [connection-lti](https://github.com/PremierLangage/platon-conception/edit/master/UC/Utilisateur/connection-lti.md) pour plus d'informations.

La première connexion d'un utilisateur permet donc de créer un compte associé sur PLaTon.

> **Niveau** : Haut niveau
> **Déclencheur** : L'utilisateur clique sur une activité LTI depuis un LMS
> **Acteur Primaire**: Utilisateur
 
 
## Preconditions

Avoir créée une activité LTI correspondant à sur un LMS PLaTon.


## Scenario Nominal
1.	L'utilisteur clique sur l'activité LTI depuis un LMS.
2.	Le LMS redirige l'utilisateur sur PLaTon.
3.	PLaTon crée l'utilisateur avec les informations de la requête.  
4.	L'utilisateur est authentifié sur PLaTon.  

### Extensions
2. Le LMS redirige l'utilisateur sur PLaTon.
3. Les identifiants LTI ne sont pas valide, PLaTon refuse la connexion.



## Post Conditions
### Conditions de succès 
Un compte est créé correspondant à l'utilisateur du LMS, et l'utilisateur est identifié sur celui-ci.

### Minimal Guarantees
Le respect de la norme LTI par PLaTon.

### Conditions final en cas d'échec
Rien n'est crée sur PLaTon, et l'utilisateur est redirigé sur le LMS avec un message d'erreur.
bles suivantes sont optionnelles._

### Frequence
Pic en début d'année scolaire, peu souvent le reste du temps.
