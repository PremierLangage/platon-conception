#  Exercice

Sur la plateforme PLaTon, un exercice est un dispositif pédagogique élémentaire. Il prescrit une tâche dans un énoncé et offre une interface de réponse. Il est capable d'évaluer la réponse entrée par l'élève et, éventuellement, de fournir une rétroaction corrective.

Dans certains exercices, les données de l'énoncé peuvent être aléatoires. Une version d'un exercice associée à un jeu de données particulier est appelée une instance.

La plateforme peut exécuter un exercice selon diverses configurations pédagogiques : nombre de tentatives, limite de temps, possibilité de demander une nouvelle instance de l'exercice, etc. C'est ce que l'on appel les `settings` de l'exercice. 

Les exercices sont généralement insérés dans des dispositifs pédagogiques plus complexes appelés activités. Dans ce cadre, ils peuvent tout aussi bien servir à de l'apprentissage, de l'entraînement ou de l'évaluation. 
Les settings sont fixés au lancement de l'exercice, l'exercice peut les modifier mais c'est contraire aux principes qui confie le choix des settings à l'`activité` qui utilise l'exercice (Examen, Tp, exploration, mémorisation etc).  


* * *

Un exercice permet à un utilisateur de s'entraîner de manière autonome.

Il est créé par un enseignant ayant un [karma](karma.md) suffisant ou peut être proposer par un étudiant (l'exercice doit donc être validé par un enseignant ayant aussi un karma suffisant dans la discipline de l'exercice).

Il est corrigé de manière automatique. La correction est un couple (score,feedback).
Le score variant de -n à 100. Zéro indiquant l'échec total et 100 le success total.  
Le score -1 indiquant que la réponse de l'élève ne peut être évalué car elle n'est pas dans un format correct (exemple: ne compile pas, mal parenthèsé, etc). 
  Note: les valeurs négatives sont réservé pour un usage ultérieur.

Le feedback est du markdown qui affiché entre la text et le form. Ce feedback est construit par l'évaluateur de l'exercice.

## Règles 

Il doit contenir un ou plusieurs [tag](tag.md) pour apporter un étiquetage sémentique à l'exercice à la fois pour aider l'enseignant qui cherche des exercices et pour permettre des traitement de type analyse des prérequis.


Un exercice doit être placer dans une [activité](activity.md) comme la [feuille d'exercice](feuille.md) par un enseignant pour que les étudiants puissent l'tuilisé.

Un exercice peut être fournis en mode 'démo' dans ce cas il est accessible sans identification.

## Status editorial d'un exercice

Les exercices sont écrit par des collègues a tout moment et accessible au partage dès qu'ils sont publiés (c-a-d proposés à des étudiants), les exercices de démo ne sont pas publiés.

Un  exercice passe par les étapes suivantes:  
privé: seul le propriétaire le vois et peut en faire une préview.  
publié: l'exercice apparait dans les ressources du cercle  
utilisé: Des élèves ont fait l'exercice  

En suite l'exercice peut avoir des étiquettes 
validé: l'exercice à été validé par un responsable de cercle 
buggé:  Une bug à été détecté dans l'exercice -> une demande de motification à été faite.
CKC: l'exercice est casé (charge pas, erreur du grader, retour grade=-2). Affectation automatiqe du tag et notificaiton au cercle.
Cercle<tag>: le cercle peut donner des tags a un exercices (différents de ceux qui sont dans l'éxercice). A utiliser avec modération.


# Spécification de l'exercice

voire la documentation readthedoc.github.io/PremierLangage







## Cas d'utilisation associé

[créer une exercice](../casutilisation/createur/createexercice.md)

[éditer un exercice](../casutilisation/createur/editerexercice.md)

[donner un exercice à un ou plusieurs étudiants](../casutilisation/enseignant/donnerexercices.md)

[donner un défi](../casutilisation/etudiant/donnerexercice.md)

[Valider un exercice](../casutilisation/enseignant/validation.md)

[faire un exercice](../casutilisation/etudiant/faireexercice.md)

[étudier](../casutilisation/etudiant/etudier.md)

[réviser](../casutilisation/etudiant/reviser.md)

<!---
Author : Hugo
Validator : Jordan
-->
