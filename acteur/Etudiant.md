 
# Étudiant  

Objectifs des étudiants: apprendre et participer.

**Apprendre**: Accumuler des complétions d'AAV (**[aav](https://github.com/PremierLangage/plconception/tree/master/conception/concept/aav.md)**)

**Participer**: Être dans un cours organisé avec d'autres étudiants, suivre un planning, effectuer des devoirs, former des binomes ou autre groupes.

**Acteur Humain** qui normalement appartient à un ou plusieurs **cours** d'un **serveur d'assets**. La première connexion d'un utilisateur inconnu sur un **serveur d'assets** ayant le **status d'étudiant dans LTI** fabrique un utilisateur de type étudiant dans ce même **serveur d'assets**. Cette connexion se fait par un lien du type : "faire tel exercice" ou encore "accéder à tel cours" mis en place par un enseignant.

## description

> Besoin en formation: Non, il doit juste répondre à des exercices.

Les étudiants sont des utilisateurs ayant accédé à un **serveur d'assets** PLaTon par un lien LTI qui a été placé dans un cours LTI par un enseignant. Ils ne peuvent que rejoindre un cours depuis LTI. 

## Questions sur l'acteur étudiant

* **Comment a-t-il connu la plateforme ?** \
  Un enseignant a ajouté un lien vers une activité (tournant sur **serveur d'assets**) PLaTon sur son LMS. Tous les élèves du LMS pouvant cliquer sur le lien se verront créé automatiquement un compte **étudiant** sur ce **serveur d'assets** via LTI.
  
* **Comment a-t-il créer son compte ?** \
  Par une première connexion via LTI. CF use-case login. Il faudrait cependant lui fournir un mot de passe lors de sa premiere connexion s'il ne souhaite par fois pas passer par LTI. Cependant le seul moyen de rejoindre un cours est de cliquer sur un lien dans un LMS.

## Les use-cases identifiés des étudiants

[activite-recommandation.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Etudiant/activite-recommandation.md)   

* [afficher-completion.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Etudiant/afficher-completion.md) (l'étudiant souhaite visualiser son avancement sur les activités de ses cours)  

[auto-inscription-classe.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Etudiant/auto-inscription-classe.md)   
[donner-avis-asset.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Etudiant/donner-avis-asset.md)   
[exporter-cours-portfolio.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Etudiant/exporter-cours-portfolio.md)   
[interagir-exercice.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Etudiant/interagir-exercice.md)   
[lire-tabledebord-individuel.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Etudiant/lire-tabledebord-individuel.md)   
[login.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Etudiant/login.md)   
[réaliser-activité.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Etudiant/r%C3%A9aliser-activit%C3%A9.md)   
[travailler.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Etudiant/travailler.md)   
