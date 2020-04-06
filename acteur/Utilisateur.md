 
# Utilisateur  

L'utilisateur est un **Acteur Humain** mais abstrait. Il regroupe tous les acteurs qui sont identifiés et autentifiés sur la plateforme (coté **serveur d'assets** ou bien sur le **serveur central**).

Lors de sa première connexion depuis un LMS vers un **serveur d'assets**, cet utilisateur abtrait va tout de suite se spécialiser vers l'acteur [étudiant](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Etudiant.md) s'il avait le status élève pour LTI. Si ce même utilisateur était enseignant pour LTI de la matière, alors le **serveur d'assets** en fera un [enseignant](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Enseignant.md). 

* le cas d'utilisation associé est login.

* Chaque utilisateur à un profil.

* L'objectif de l'utilisateur est d'utiliser les ressources de PLaTon.

## Cas d'utilisation de l'utilisateur loggué sur PLaTon

* [connexion via LTI](https://github.com/PremierLangage/platon-conception/blob/master/UC/Utilisateur/connection-lti.md) (Action de l'utilisateur abstrait qui clique sur un liens depuis son LMS vers PLaTon, il se spécialisera alors en étudiant ou en enseignant.)

* [première connexion](https://github.com/PremierLangage/platon-conception/blob/master/UC/Utilisateur/premiere-connexion.md) (Action de l'utilisateur abstrait qui clique pour la première fois sur un liens depuis son LMS vers PLaTon. Cette action transforme un visiteur en utilisateur en créant son compte avec les renseignement LTI issus du LMS.)
