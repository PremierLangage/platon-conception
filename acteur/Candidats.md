 
# Candidats  

Un candidat est un **Acteur Humain** non loggué, sans compte PLaTon, mais possédant un secret (typiquement une URL qu'il a reçu par mail). C'est un [visiteur](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Visiteur.md) qui grace à son secret, peut accéder à une ressource évaluante qui laissera une trace à l'utilisateur qui a créé le secret.

Dans l'idée, l'enseignant en charge du recrutement dans une formation peut créer des secrets (avec pour argument une activité PL, un temps limite, un nom et un prénom). Le secret est ensuite envoyé à un visiteur par mail par exemple. Lorsque la cible utilise le secret, il devient candidat. Il devra alors faire l'activité PL dans le temps imparti. Une fois l'examen terminé, un résumé est envoyé par mail au créateur du secret.

Objectif: être accepté dans une formation  

> Besoin en formation: Non, toutes les instructions doivent être incluses avec la transmission du secret.

## Cas d'utilisations identifiés du candidat :

* Créer un test d'entrée
* [Passer un test d'entrée](https://github.com/PremierLangage/platon-conception/blob/master/UC/Candidats/Faire-un-test.md)
* Produire les "resultats" du test (pour les inscriptions par exemple)
* associer les comptes candidats au compte etudiant correspondant pour archivage
