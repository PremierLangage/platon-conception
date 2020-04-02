
# Cas d'utilisation N° 17 : connexion LTI

La connexion LTI de l'enseignant étend la [Connexion LTI](../Utilisateur/connection-lti.md) définit pour les utilisateurs de manière générale.

##	Description

La paticularité de l'enseignant dans un **serveur d'assets** est que les inforamtions LTI lors de sa connexion qualifiaient qu'il avait le rôle d'enseignant. L'enseignant a une vue de type enseignant sur les assets sur lesquels LTI le qualifie d'enseignant mais il peut avoir des vues élèves sur des assets pour lesquels LTI lui donnait le rôle d'étudiant (le role par cours déployés assets calque les rôles issus du LMS sur chaque cours de ce LMS...). 

On dit qu'un utilisateur est enseignant dans PLaTon losrqu'il existe au moins une matière (un cours ou un asset) pour lequel il est enseignant. De ce fait, il peut avoir accès (seulement s'il décide de cliquer pour s'y rendre...) au **serveur central** de ressources. Il aura alors au moins status de [membre](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Membre.md) et il concervera aussi les données relatives au **serveur d'assets** d'où il est originaire.

Voir le cas d'utilisation [creation-classe](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/create-classe.md) 
