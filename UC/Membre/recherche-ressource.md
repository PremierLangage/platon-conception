
# Cas d'utilisation N° 56 :  recherche-ressource

Objectif d'un utilisateur :  Trouver une ressource.
Pour trouver une ressource deux possibilités:
- Par aav en utilisant le q&a et la recherche d'aav. Voir le Q&A.
- Par une recherche full text et tags (comme pour une recherche immobilière/ le bon coin )


> **Niveau** :Haut niveau, Résumé, objectif utilisateur, sous fonction, Bas niveau , FIXME Remove unused   
> **Déclencheur** : Le membre cherche une ressource pour la placer dans un cours ou une ressource agrégeante
> **Acteur Primaire** : Membre   
> **Acteurs secondaires** : Acteurs modifiant les métadonnées 
> **Parties Prenantes concernées** : utilisateurs   
 
 
## Preconditions
 
Pour que ce cas d'utilisation puisse avoir lieux il faut des ressources étiquetées (tags)

Types de Tags:
- Disciplinaire (informatique, histoire, etc),
- Niveau scolaire (CP,CE1,...., D, N),
- Difficulté (Introductif,applicatif,calculatoire,reflexion,difficile),
- Etat de développement (None,testé,Validé,opérationnel, inconnu, Erreur,...),


## Scenario Nominal

Le scénario débute avec la page de recherche d'exercice du site des ressources:

1.	L'utilisateur rempli les différents champs des critères de recherche,
- full text (grep dans le fichier ou un locate ou un elastique search)
- choix disciplinaire (saisie controlée)
- Niveau (Click + selected/notselected)
- etat (liste déroulante)

2. Le système fait un filtre selon les critères sélectionnés 
- Si aucune ressource n'a été trouvé il renvoie à l'utilisateur ou page vide avec un message pour dire qu'aucune ressource ne correspond à la recherche -> fin du cas d'utilisation
- Sinon il envoie la liste des liens vers les ressources par ordre de correspondance selon les critères

3. L'utilisateur peut cliquer sur n'importe quel lien qui mène vers une ressource parmi celles qui sont apparus à la recherche -> fin du cas d'utilisation


###	Extensions
FIXME Moins bien _[Document alternate flows and exceptions to the main success scenario. Extensions are branches from the main scenario, and numbering should align with the step of the success scenario where the branch occurs.]_

FIXME Indiquez dans quel point du scenario nominal le chemin alternatif démarre et ou il reprend.


## Post Conditions
### Conditions de succès 

Une fois que les ressources correspondant à la recherche sont listés, la recherche est terminé et l'utilisateur peut naviguer dans les ressources trouvées.

### Minimal Guarantees
FIXME _[Describe the guarantee or assurance that this Use Case provides to all Actors and Stakeholders to protect their interest regardless of whether the Use Case ends with success or failure.]_

### Conditions final en cas d'échec
FIXME _[Describe the end condition that results if the Primary Actor fails to accomplish his goal.]_

S'il existe une ressource qui pourrait correspondre à la recherche mais qui n'est pas tagué -> elle n'apparaîtra pas dans les résultats alors qu'elle devrait

FIXME _les variables suivantes sont optionnelles._

### Frequence
FIXME _[Indicate how often the use case is expected to occur. This information aids designers and developers in understanding capacity requirements.]_   
### Besoins Spéciaux (optionel)  
FIXME _[Describe any additional factors that impact the execution of the use case. These could be environmental, regulatory, organizational or market-driven in nature.]_  
### Performance  
###	Security  
###	Usability / Accessibility  
###	Other  

##	Problèmes et étapes suivantes  
FIXME _[Note any issues related to the definition of this use case that will require clarification prior to development. Also list any follow-up work that needs to be done prior to sign-off on the use case.]_  

Problème dans la description **actuelle** du cas d'utilisation : Des problèmes à comprendre le principe de la rubrique **extension**  

## Cas d'utilisation associé

- [Discipline](https://github.com/PremierLangage/plconception/blob/master/conception/concept/discipline.md) 
- [Ressource](https://github.com/PremierLangage/plconception/blob/master/conception/concept/ressource.md)
- [Aav](https://github.com/PremierLangage/plconception/blob/master/conception/concept/aav.md) 
- [Tag](https://github.com/PremierLangage/plconception/blob/master/conception/concept/tag.md)
