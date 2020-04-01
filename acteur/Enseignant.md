 
# Enseignant  

L'enseignant est un **Acteur Humain** qui est à la fois un [membre](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Membre.md) sur le **serveur central** de ressources (s'il s'y connecte), mais d'abord un acteur enseignant sur un **serveur d'assets** (Il existe un LMS qui le désigne comme enseignant sur au moins un cours du même LMS). 

> Besoin en formation: Oui

L'enseignant non éditeur n'accède qu'aux **serveur d'assets** notament à son **éditeur d'assets** qui lui permet d'administrer les cours opérationnels qu'il déploye à ses élèves (À ce moment là, son travail reste local...).

Losrque l'enseignant se dirige sur le **serveur central** de ressources, il devient un [membre](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Membre.md) mais aussi garde avec lui l'information relative à son **serveur d'assets**. Ainsi, s'il utilise le Search & compose pour construire son cours, ce même cours aura vocation à devenir un asset du **serveur d'assets** dont il est originaire.

Les possibilités coeurs du travail de l'enseignant sous PLaTon sont :
- Il peut définir la liste des AAV de son cours.
- Il peut modifier les assets de son cours.
- Il peut regarder l'avancement de ces élèves sur les assets déployés.
- Il peut évaluer/corriger certaines activités (les assets qui permettent de le faire).
- Il peut exporter des notes.
- Faire de la gestion: inscrire des enseigants non éditeurs, des enseignants et des étudiants.
- Administration du cours: partage et archivage.

Sinon l'enseignant est membre d'un **cercle** (a minima celui des "noobs" sur le site) et donc peut utiliser le **serveur central** de ressource comme un [membre](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Membre.md).


## cas d'utilisation associés

[afficher-completion-group.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/afficher-completion-group.md)   

* [afficher-completion.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/afficher-completion.md) : L'enseignant visualise l'avancement de ses étudiants sur ces cours déployés

[affichercompletion.png](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/affichercompletion.png)   
[archiver-cours.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/archiver-cours.md)   
[asset-metadata-edition.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/asset-metadata-edition.md)   
[choisir-visibilité-completion.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/choisir-visibilité-completion.md)   

* [connexionLTI.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/connexionLTI.md) : Connexion de l'enseignant depuis un LMS vers un **serveur assets** PLaTon

[consulter-indicateur-individuel-collectif.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/consulter-indicateur-individuel-collectif.md)   
[creer-cours.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/creer-cours.md)   
[crud-asset.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/crud-asset.md)   
[crud-classe.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/crud-classe.md)   
[definir-regle-acquisition.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/definir-regle-acquisition.md)   
[Demande-de-cercle.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/Demande-de-cercle.md)   
[editer-cours.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/editer-cours.md)   
[editer-modalités-completion.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/editer-modalités-completion.md)   
[Enseigner.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/Enseigner.md)   
[Evaluer.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/Evaluer.md)   
[exporter-notes.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/exporter-notes.md)   
[exporter-stats.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/exporter-stats.md)   
[[img]afficher_completion.jpg](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/[img]afficher_completion.jpg)   
[inscription-etudiant-classe.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/inscription-etudiant-classe.md)   
[Integrer-moncours.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/Integrer-moncours.md)   
[lire-tabledebord-groupe.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/lire-tabledebord-groupe.md)   
[login.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/login.md)   
[modifier-completion.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/modifier-completion.md)   
[modifier-evaluation-metadata-asset.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/modifier-evaluation-metadata-asset.md)   
[partage-cours.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/partage-cours.md)   
[réaliser-activité.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/réaliser-activité.md)   
[recharger-cours.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/recharger-cours.md)   
[valider-aav-etudiant.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/valider-aav-etudiant.md)   
[valider-portfolio.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/valider-portfolio.md)   
