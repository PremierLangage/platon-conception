
# Cas d'utilisation N° 16 :  connection-lti

Niveau 1

## Description

L'utilisateur se connecte à la plateforme depuis un LMS en cliquant sur une activité [lti](https://github.com/PremierLangage/plconception/blob/master/conception/concept/lti.md).

La norme LTI permet de récupéré en, partculier les données suivantes depuis le LMS:

|                paramètre                |       status       |description|
|-----------------------------------------|--------------------|-----------|
|`user_id`                               |recommended         |ID unique référençant l'utilisateur.|
|`user_image`                            |optional            |Potentiel URL vers un avatar.       |
|`roles`                                 |recommended         |List de roles séparé par des virgules, voir le tableau ci-dessous pour la liste des rôles|
|`lis_person_name_full`                  |recommended         |Nom complet de l'utilisateur, ne sera pas envoyé si le LMS à été configuré pour lancer des requêtes de façon anonyme.|
|`lis_outcome_service_url`               |optional            |URL sur laquelle PLaTon peut renvoyer des notes, celle-ci est unique pour le double (`user_id`, `resource_link_id`). |
|`lis_person_name_given`                 |recommended         |Prénom de l'utilisateur.|
|`lis_person_name_family`                |recommended         |Nom de l'utilisateur.|
|`lis_person_contact_email_primary`      |recommended         |Email de l'utilisateur.|
|`resource_link_id`                      |required            |ID unique référençant l'activité sur le LMS.|
|`resource_link_title`                   |recommended         |Titre de l'activité sur le LMS.|
|`resource_link_description`             |optional            |Description de l'activité sur le LMS.|
|`context_id`                            |recommended         |ID unique de la classe sur le LMS.|
|`context_type`                          |optional            |Contexte du LMS depuis lequel l'utilisateur est arrivé sur PLaTon.|
|`context_title`                         |optional            |Titre de la classe sur le LMS.|
|`context_label`                         |recommended         |Label de la classe sur le LMS (Nom court / code...).|
|`launch_presentation_locale`            |recommended         |Locale à utiliser pour l'utilisateur (fr-FR...).|
|`launch_presentation_return_url`        |recommended         |URL avec laquelle renvoyer l'utilisateur sur le LMS si besoin. Possible de fournir les paramètres suivant: `lti_errormsg` - Message d'erreur à montrer à l'utilisateur, `lti_errorlog` - Message d'erreur que le LMS peut stocker sans le montrer à l'utilisateur, `lti_msg` - Message de réussite à montrer à l'utilisateur| `lti_log` - Message de réussite que le LMS peut stocker sans le montrer à l'utilisateur
|`tool_consumer_info_product_family_code`|recommended         |"Marque" du LMS : `moodle`, `blackboard`, `canvas`...|
|`tool_consumer_info_version`            |recommended         |Version du LMS.|
|`tool_consumer_instance_guid`           |strongly recommended|ID unique du LMS, il s'agit du plus souvent du DNS.|
|`tool_consumer_instance_name`           |recommended         |Nom du LMS.|
|`tool_consumer_instance_description`    |optional            |Description du LMS.|
|`tool_consumer_instance_url`            |optional            |URL du LMS.|
|`tool_consumer_instance_contact_email`  |recommended         |Adresse email sur laquelle contacter les gestionnaires du LMS.|
|`custom_*`                              |optional            |N'importe quelle paramètre custom. Chaque clé doit commencé par `custom` et être écris en *snake case*.|
---------------------------------------------------------------

|       Rôle       |
|------------------|
|Student           |
|Faculty           |
|Member            |
|Learner           |
|Instructor        |
|Mentor            |
|Staff             |
|Alumni            |
|ProspectiveStudent|
|Guest             |
|Other             |
|Administrator     |
|Observer          |
|None              |
--------------------

Dans les faits, la plupart des LMS n'utilisent que les rôles `Instructor` et `Learner`.

Il est intéressants de noter que les LMS ne sont pas tenus de fournir des informations concernants les groupes au sein des classes. Cela doit être fait par des paramètre `custom_*`.

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
