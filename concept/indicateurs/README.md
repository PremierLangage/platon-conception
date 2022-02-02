
# Les indicateurs 

les indicateurs sont des affichages visuels (ou pas) d'information sur les données de la plateforme.

- temps d'accès
- nombre de connection
- taux de réussite 
- nombre de tentatives 
- etc



# Organisation général des indicateurs



Le principe architectural pour mes indicateurs est le suivant:

- production de données, dans certains point stratgégiques de PLaton sont placé des "espions" qui envois sur la base de donnée de suivie des json qui sont affectés dans des tables.

- visibilité des indicateurs, l'accès aux indicateurs doit ce faire en fonction du DROIT (RGPD), et donc l'accès est toujours filtré en fonction du type d'accès et de l'utilisateur.

- l'affichage des indicateurs doit être fait par un logiciel sur étagère qui gère bien l'affichage graphique de données.





# Quelques remarques sur les indicateurs

Nous avons essayé d'être exaustif :
tableau croisé = donnée (exo, pltp,activité, cours ,formation) 
    * usage de l'acteur (etudiant, prof,createur, responsable, didactitien)

Il faudrais ajouter la référence temporelle : passé, présent, futur, dans chaque case du tableau ,
passé quel retour faire sur ce qui à eu lieux 
présent -> que peut on faire pour la prochaine action de l'acteur 
futur -> Que peut on anticiper (si il a fait cela alors il auras ce problème la dans le futur)

