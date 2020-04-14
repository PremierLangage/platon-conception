
# Cas d'utilisation N° 84 :  lire-tabledebord-individuel

Niveau 3

##	Description
Chaque étudiant (utilisateur du même niveau) lorsqu'il àccède à l'écran d'accueil de la plateforme se voit présenter un tableau de bord avec affichage individuel différent et paramétrable suivant ses préférences :

 - Visualisation de ces cours 
 - Visualisation de ces statistiques genérales
 - Visualisation de son Port-Folio (AAV ou Objectif Pédagogique)
 - Recherche d'exercices ouverts à tous (si existant)
 - ...

**[tableaudebord](https://github.com/PremierLangage/plconception/blob/master/conception/concept/tableaudebord.md)**  

> **Déclencheur** : Un étudiant se connecte sur la plateforme via l'écran login et MDP / A partir de Platon, il revient sur sa page d'accueil 
> **Acteur Primaire**: Etudiant
> **Acteurs secondaires**: Pour certainnes parties l'enseignant
> **Parties Prenantes concernées** : 
 
## Preconditions

Listez les conditions nécessaires pour que ce cas d'utilisation puisse avoir lieu

-1 Avoir un compte sur platon 
-2.1 Se connecter sur Platon en passant par la fenêtre Login et MDP 
-2.2 Être déjà dans Platon et revenir à la page d'accueil

## Scenario Nominal

Tout ce passe bien c'est le scénario parfait.

1.	L'étudiant se connecte à la plateforme (identifiant et mot de passe) / L'étudiant clique sur sa page d'accueil à partir de Platon
2.	L'étudiant a une vue d'ensemble sur son tableau de bord, ses cours, ses statistiques, ses dernières activités ...
3.	Il peut accéder à tout les activités représentées en cliquant directement dessus   

Lorsqu'un élève accède à son écran d'accueil il aura immédiatement accès à un tableau de bord qu'il aura lui même paramétré dans les préférences de son profil.
Ce tableau de bord comportera avec les cours auxquels il est inscrit, ses dernières activités en particulier les exercicies réussis, échoués et de quels cours il dépendaient.
ATTENTION : il s'agit de l'écran d'accueil après une connexion ou un retour à l'écran d'accueil, il ne s'agit pas de l'accès direct au cours suite à un lien sur un LMS (si ce lien existe)!!

###	Extensions
Si problème de connection avec le serveur un message d'erreur doit apparaître

## Post Conditions
FIXME

### Conditions de succès 
L'élève accède à son tableau de bord

### Minimal Guarantees
FIXME _[Describe the guarantee or assurance that this Use Case provides to all Actors and Stakeholders to protect their interest regardless of whether the Use Case ends with success or failure.]_

### Conditions final en cas d'échec
FIXME _[Describe the end condition that results if the Primary Actor fails to accomplish his goal.]_

FIXME _les variables suivantes sont optionnelles._

### Frequence

Le tableau de bord est confondu avec l'écran d'accueil de l'application, ce qui veut dire que les utilisateurs de type "étudiant" et autre vont revenir très régulièrement à cet écran pour accèder à d'autres "ressources". 
Le tableau de bord étant le "croisement" de l'ensemble des activités des utilisateurs, sa fréquence d'utilisation sera forte!

### Besoins Spéciaux (optionel)  
Le tableau de bord est paramétrable. Les préférences des utilisateurs doivent être stockées.

### Performance  

###	Security  
un login = un tableau de bord et des préférences utilisateur

###	Usability / Accessibility
FIXME
###	Other  
FIXME

##	Problèmes et étapes suivantes  
FIXME _[Note any issues related to the definition of this use case that will require clarification prior to development. Also list any follow-up work that needs to be done prior to sign-off on the use case.]_  

FIXME définir ce qui pose problème dans la description **actuelle** du cas d'utilisation.  
FIXME vous pouvez ajouter ici un lien vers une issue github ou un carte de projet github.

TBR
