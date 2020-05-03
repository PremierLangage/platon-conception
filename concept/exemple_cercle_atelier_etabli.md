Exemples de fichiers et de mise en oeuvre des cercle et des établis:




```
Cercle1: Maitre # ou bien général yggdrasil ... 
    Atelier du Cercle1: Atelier1 # ou un autre mot simple 
        /models/qcm.pl # Un modèle utilisé par tout le monde dans le cercle Maitre
        /data/cartes/france.gif # des données visible par tous
            # car utilisables dans plein de discplines (wikipedia commons)
    Etabli de "jean dupont" # noob de son état c'est dire membre du cercle maitre 
        /models/qcm.pl # recupération de repertoires de l'atelier Atelier1
        /data/cartes/france.gif # dito
        exo1.pl # un exo de qcm qui contient la référence
            extends= /models/qcm.pl # (fait référence au fichier Atelier1/models/qcm.pl mais est ici une référence relative)
Cercle 2 : Computer Science
    super : maitre # le cercle2 hérite des capacités du cercle 1
    Atelier du cercle 2: computers # ou un autre mot simple 
         /models/qcmcs.pl # un nouveau fichier de l'atelier computers
      plus les fichiers de Atelier1
        /models/qcm.pl # recupération de repertoires de l'atelier Atelier1
        /data/cartes/france.gif # des données visible par tout car utilisable dans plein de discpline (wikipedia commons)
      plus les fichiers publiés localement
    Etabli de "Nicole Borie"  # Hacker devant l'éternel et donc membre de computerscience
        exo1.pl # tient lui aussi il a appeler exo1 son exo1.
            extends= /models/qcm.pl # (fait référence au fichier Atelier1/models/qcm.pl mais est ici une référence relative c'est donc la référence
                computers/models/qcm.pl)
        exo2.pl 
            extends=/models/qcmcs.pl

Cercle 3: python 
    super: Computer Science
    Atelier du cercle 3: yo-python 
          /models/pltest.pl # un template vraiement que pour le python (il utilise les doctest python pour evaluer)
        plus les fichiers de computer
            /models/qcmcs.pl # un nouveau fichier de l'atelier computers
            /models/qcm.pl # recupération de repertoires de l'atelier Atelier1
            /data/cartes/france.gif # des données visible par tout car utilisable dans plein de discpline (wikipedia commons)
        plus les publications locales
            /AP1/variables/intialisation.pl
            /AP1/variables/affectation.pl
            
    Etablie "Joe Coumes"  # Hacker python  devant les hommes et donc membre de python
        py1.pl
            extends= /models/qcm.pl # (fait référence au fichier yo-python/models/qcm.pl qui est aussi  Atelier1/models/qcm.pl mais aussi computers/models/qcm.pl)
        py2.pl
            extends= /models/pltest.pl # ca c'est du python 


Cercle 4: L'acceuil. # Cercle d'acceuil des nouveaux 
    super: Maitre 
    Atelier du cercle 4: acceuil
        /models/qcm.pl # Un modèle utilisé par tout le monde dans le cercle Maitre
        /data/cartes/france.gif # des données visible par tous
        plus les fichiers de acceuil
            /tutoriel/prepare.pl
            /tutoriel/edition.pl
            /tutoriel/evaluator.pl
            /tutoriel/before.pl
            /tutoriel/builder.pl
            /tutoriel/grader.pl
        plus les publications (ici tout le monde a le droit de publier).
            /nimportenawak/pasmieux.pl
            
        
```

Règle de publication, On ne peut pas écraser un fichier avec un autre, on peut juste l'éditer directement, cela évite des catastrophes. 
    Donc si l'on cherche a publier il y a vérification que l'on écrase pas (sauf dans le cas ou l'on est l'auteur du fichier que l'on écrase ...).

Règle de visibilité,
    un fichier n'est visible par les autres et par les serveurs d'assets que si il est publié.
    une fois visible il n'apparait plus dans le home mais dans publish et peut  être modifié par d'autres.
    Pour l'utilisateur le changement entre home et published ne doit être qu'une manifestation graphique (genre italic ou couleur).
    Le fichier conserve sa référence locale. 


Organisation des cercles:

Maitre/
    Acceuil/
    Sciences/
        Mathématiques/
        Informatique/
    LSH/
    Santé/
    Pluridisciplinaire/






