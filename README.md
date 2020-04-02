# Analyse et conception fonctionnelle de PLaTon

Bienvenue sur l'analyse et la structuration fonctionnelle de PLaTon 
établie au printemps 2020 pour rigidifier la prochaine version majeure 
de PLaTon : la version 1.0

## Les différents acteurs dans PLaTon

* [Utilisateur](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Utilisateur.md) (status racine abstrait avant attribution d'un rôle plus précis post-login)

### Acteurs ayant accès au serveur central de ressources

* [Administrateur](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Administrateur.md) (sorte de power-user du **serveur central** de ressources)
* [Membre](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Membre.md) (status de base de l'utilisateur/contributeur du **serveur central** de ressources)
* [Enseignant](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Enseignant.md) (membre qui opérationnalise les resources vers un **serveur d'assets**...)

### Acteurs dont l'activité reste sur serveur d'assets

* [Étudiants](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Etudiant.md) (acteur apprenant sur le **serveur d'assets** de son organisme formateur)
* [Enseignant](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Enseignant.md) (lorsqu'il décide de rester non-éditeur mais qu'il manage ses classes déployées...)

## Ressources du projet, concepts et lexique

### Concepts immatériels

* [AAV pour Acquis d'Apprentissage Visé](https://github.com/PremierLangage/platon-conception/blob/master/concept/aav.md) (objectif pédagogique clair et mesurable)
* [Notion de complétion d'un travail](https://github.com/PremierLangage/plconception/blob/master/conception/concept/completion.md) (relatif à l'avancement, la réussite voire la validation)
