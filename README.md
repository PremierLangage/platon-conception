# Analyse et conception fonctionnelle de PLaTon

Bienvenue sur l'analyse et la structuration fonctionnelle de PLaTon 
établie au printemps 2020 pour rigidifier la prochaine version majeure 
de PLaTon : la version 1.0

## Les différents acteurs dans PLaTon

* [Visiteur](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Visiteur.md) (Le statut par défault de l'acteur n'ayant pas de compte PLaTon)

### Acteurs ayant accès au serveur central de ressources

* [Administrateur](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Administrateur.md) (sorte de power-user du **serveur central** de ressources)
* [Membre](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Membre.md) (statut de base de l'utilisateur/contributeur du **serveur central** de ressources)
* [Enseignant](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Enseignant.md) (membre qui opérationnalise les resources vers un **serveur d'assets**...)
* [Président d'un cercle](https://github.com/PremierLangage/platon-conception/blob/master/acteur/President.md) (membre d'un **cercle** qui en assure l'animation et l'organisation (souvent son créateur))
* [Directeur Scientifique](https://github.com/PremierLangage/platon-conception/blob/master/acteur/DirecteurScientifique.md) (membre d'un **cercle** dont il porte la responsabilité scientifique)

### Acteurs dont l'activité reste sur serveur d'assets

* [Utilisateur](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Utilisateur.md) (status racine abstrait de l'utilisateur loggué ayant toujours un rôle plus précis)
* [Étudiants](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Etudiant.md) (acteur apprenant sur le **serveur d'assets** de son organisme formateur)
* [Enseignant](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Enseignant.md) (lorsqu'il décide de rester non-éditeur mais qu'il manage ses classes déployées...)

## Ressources du projet, concepts et lexique

### Concepts immatériels

* [AAV pour Acquis d'Apprentissage Visé](https://github.com/PremierLangage/platon-conception/blob/master/concept/aav.md) (objectif pédagogique clair et mesurable)
* [Notion de complétion d'un travail](https://github.com/PremierLangage/plconception/blob/master/conception/concept/completion.md) (relatif à l'avancement, la réussite voire la validation)
