


## Les différents acteurs dans PLaTon

le 
[Diagramme Général](http:////www.plantuml.com/plantuml/png/NP11RiCW44NtSmeka0kmg5BLNLQg5BNxYHad8m5EOQWKgHVAENAn3jW9QRtYluU73ziicAG43_hPPnSuSfQ4GYLPWzbWHQe6TZWAZqonSQUvqaHZtRkhGdZYhqBD3pkmhp4J7o96QQX7LL8StqKB5RzHs2TgCBGbsFVZEVCSvw2z5dCwdXKdokpqp0Lf0liXx3dtxYLJ0h3gJdFCkFSqpIcWwBZcqmG0lPNP_3ojnvh_k8uoS2jgpAR3vOzEODXfk4q2RLjTprhd3u3sn8yJwzkQ3Y1DZmd0lc2iUvQxZsi0-ycPxvV_NWE0i7Wo0-CXOGXa3jTBl5uIUkEq2evrLzQrENcKESAMeYl1_m80)
des acteurs.

* [Visiteur](Visiteur.md) (Le statut par défault de l'acteur n'ayant pas de compte PLaTon)
* [Candidat](Candidats.md) (Le candidat est un utilisateur sans compte dans PLaTon mais possédant un secret pour accèder à une activité évaluatrice)

### Acteurs ayant accès au serveur central de ressources

* [Administrateur](Administrateur.md) (sorte de power-user du **serveur central** de ressources)
* [Membre](Membre.md) (statut de base de l'utilisateur/contributeur du **serveur central** de ressources)
* [Enseignant](Enseignant.md) (membre qui opérationnalise les resources vers un **serveur d'assets**...)
* [Didacticien](Didacticien.md) (membre dont le travail est focalisé sur les outils statistiques supports aux enseignements)
* [Président d'un cercle](President.md) (membre d'un **cercle** qui en assure l'animation et l'organisation (souvent son créateur))
* [Directeur Scientifique](DirecteurScientifique.md) (membre d'un **cercle** dont il porte la responsabilité scientifique)
* [Physionomiste d'un cercle](Physionomiste.md) (membre d'un **cercle** qui assure la médiation et la modération au seing du groupe)

### Acteurs dont l'activité reste sur serveur d'assets

* [Utilisateur](Utilisateur.md) (status racine abstrait de l'utilisateur loggué ayant toujours un rôle plus précis)
* [Étudiants](Etudiant.md) (acteur apprenant sur le **serveur d'assets** de son organisme formateur)
* [Enseignant](Enseignant.md) (lorsqu'il décide de rester non-éditeur mais qu'il manage ses classes déployées...)

