# Liste des clés soumises à contrôle de playexo/playactivity

* title 
* text
* form
* bouton valider et contrôle (recommencer/abandonner/voire la solution/faire autre chose)
* builder 
* grader
* vrai/faux (juste vrai ou faux, sans la réponse)
* réponse (juste la réponse brute)
* solution (solution complète et expliquée)
* grade (note de la dernière tentative sans tenir compte du nombre de tentatives, l'activité controle la pondération!)
* hint (conseil du moment)
* max_apptempt (None ou un entier)
* nb_apptempt
* feedback (retour personnalisé différable : tout de suite ou en fin d'exo)
* warning (consigne jetable utilisé pour le grade de -1)

Ordre d'affichage standard

    TITLE 
    TEXT 
    HINT 
    FEEDBACK 
    SOLUTION 
    WARNING 
    FORM 
    BOUTON VALIDER ET CONTROLE 

### title 
Toujours visible, c'est le titre courant de l'exercice.

### text
Toujours visible, c'est l'énoncé de l’exercice. Le contenu de la balise ne sera jamais désactivé. Pour l’effacer, la seule solution est que le créateur de l'exercice écrase son contenu avec la chaîne vide dans un builder/grader, le créateur/enseignant éditeur est responsable.

Dans les histoires dont vous êtes le héro, écraser le champs text est une feature, c'est important de pouvoir le faire

### form
Le formulaire de réponse de l'exercice. Ce dernier est proposé à l'élève si max_apptempt vaut None ou si nb_apptempt est strictement plus petit que max_apptempt. Des conditions extérieures (limites de temps ou autorisation d'accès : TODO) peuvent désactiver l'affichage du formulaire.

### bouton valider et contrôle (recommencer/abandonner/voire la solution/faire autre chose)

* bouton valider : Même visibilité que le formulaire
* option, proposer trois ou quatre boutons à la place de valider qui indique le niveau de confiance type "je le sais" (vert) "je le pense" (vert clair) "je ne suis pas très sûr" (orange) "je n'en ai aucune idée" (rouge). La valeur choisie doit être collectée.
* bouton ré-initialiser : Même visibilité que le formulaire, ré-initialise l'exo avec la **même seed de génération aléatoire**
* bouton voir la solution : Visible si solution existante et autorisation par l'activité
* bouton retenter l'exercice : Visible si autorisation par l'activité, relance l'exo avec une **nouvelle seed de génération aléatoire**

**--> abandonner/faire autre chose doit être gérer par l'activité mais pas par l'exo et son formulaire/controle**

### solution (solution complète et expliquée)
Disponible seulement à la demande de l'apprenant si existant et si autorisé. Lorsque l'apprenant veut voir la solution, on lui présente alors le contenu suivant : 

    TITLE 
    TEXT 
    SOLUTION 
    BOUTON VALIDER ET CONTROLE (en fait seulement possiblement relancer avec nouvelle seed ici !!!!)

TODO : IL Y A-T-IL UN APPEL SANDBOX OU PAS ?

TODO : IL FAUT ABSOLUMENT UNE TRACE POUR SAVOIR QUI VISUALISE ET QUAND UNE SOLUTION, ON STOCKE CELA COMMENT SUIVANT LA RÉPONSE À LA QUESTION AU DESSUS...


### grade (note de la dernière tentative sans tenir compte du nombre de tentatives, l'activité contrôle la pondération!)
Le grade du gradeur doit TOUJOURS gradé comme si c'était la première proposition de l'élève. Les décisions de visibilité et pondération sont prises par les activités. Une note admissible est un entier compris entre 0 et 100 inclus.

La valeur -1 du grade correspond à la décision pédagogique de ne pas noter (toute raison fondée est acceptable : formulaire non rempli, erreur d'interface, etc...). À ce moment là, un exercice raisonnable donne un warning (chaîne non vide) qui sera proposé en retour à l'élève pour reproposer des réponses. -1 ne compte pas comme une tentative !!!!

### hint (conseil du moment)
un message dynamique et personnel pour aider l'apprenant sur l'exercice
Il doit/peut être replié, 
il peut en exister plusieurs consécutifs, 
il peut être désactivé (par exemple en mode examen)
le fait de l'utiliser peut avoir une conséquence sur la notation, 
TODO : Charte graphique et couleur/mise en page explicite pour des conseils....

### feedback (retour personnalisé différable : tout de suite ou en fin d'exo)
Retour personnalisé et possiblement différable pour l'apprenant.
Basé sur une analyse fine de la réponse, 

ATTENTION !!!! différable est primordiale. Si l'exercice est un exercice à étapes ou un exercice à énoncé changeant, le créateur/enseignant éditeur est responsable de recopier des parties d'énoncés dans son feedback de manière à ce que ce dernier garde du sens même si ce retour est affiché en fin d'exercice.

### warning (consigne jetable utilisé pour le grade de -1)
Une message contextuel expliquant pourquoi le gradeur à refusé de noter. Le warning est placé juste au dessus du formulaire. 
TODO : Charte graphique et couleur/mise en page explicite pour des warning....


# Grands modes d'utilisation des exercices

* **Apprentissage :** Travail conseillé, encadré, dynamique (règles changeantes et intelligentes) évalué de manière formative
* **Révision :** Simulation libre et en autonomie d'activité en évaluation sommative
* **Examen :** Activité aux règles pré-établies en évaluation sommative

### Mode apprentissage

C'est le mode le plus dynamique, le plus réactif, au service de la performance de l'apprentissage. 

* Feedback au plus rapide des réponses élèves
* Hint et conseil activés/activables
* Note visibles sur le retour d'appel au grader
* Correction visibles si existantes 
* Relance autorisée si ça a du sens (comment le savoir? faut-il le mettre en dur dans les exos (je suis aléatoire et relançable, je suis une blague à chute, etc...))

### Mode Révision

C'est un mode d'entraînement au passage des examens. Lorsque l'apprenant travaille en mode révision, les activités et les exercices adoptent le comportent du mode examen. Toutefois, l'apprenant doit avoir accès aux notes obtenues ainsi qu'à un débriefing et à des possibles solutions une fois le travail terminé.

* Désactivation des Feedback mais collecte de ces derniers
* Hint et conseil désactivé par défault
* Note visibles seulement à la fin de l'activité sans action de l'enseignant (c'est un mode autonome...)
* Possibilité de revenir sur les exos pour visualiser les feebdacks et possibilité de visualiser les corrections **UNIQUEMENT A LA FIN** de l'activité.

### Mode Examen

Le mode conçu pour les examens dont les notes produites entre dans les modalités de contrôles des connaissances des formations. C'est une activité à réaliser sur un laps de temps imparti (par exemple une heure consécutive), dans un créneau imparti (par exemple entre 11h et 17h), éventuellement sur des postes impartis (ceux de la salle xx), sans conseils, ni indices, ni notes, ni débriefing.

* Désactivation des Feedback mais collecte de ces derniers
* Hint et conseil désactivé par défault
* Notes non consultables (seul l'enseignant peut activer l'affichage des notes via un panneau d'administration)
* Feedbacks et corrections non visualisable (seul l'enseignant peut activer la relache des feedback/corrigés via un panneau d'administration)

# Contrôles et décorateurs depuis les activités

Les trois grands modes d'utilisation sont des pré-configurations de l'interface complète des activités et Ppltp à venir...

Parmi les leviers de contrôle, il devrait y avoir :

* Autoriser/Interdire la visualisation des solutions
* Afficher/Cacher les feedback
* Mettre en place un nombre de tentative maximale ou pas
* Customiser les notations finales entre les notations rendues des grader et la note de l’activité
* Gérer la visibilité des notes (Toujours, jamais, on click du prof, etc....)
* Relâcher les corrections pour une activités  (typiquement quelques heures après un examen, autoriser la visualisation des corrigés)
* Autoriser/Interdire la relance (**avec nouvelles seed de génération aléatoire**) des exercices 
