
# Cas d'utilisation N° 97 :  ouvrir-centrenotification

Niveau 4

##	Description

L'utilisateur membre souhaite ouvrir le centre de notification afin de les consulter.
Le centre de notifcation s'affiche comme un sous-menu de l'icone notification

  
> **Déclencheur** : Click sur l'icone de notification (cloche)  
> **Acteur Primaire**: Membre  
> **Parties Prenantes concernées** : All
 
 
## Preconditions

1. Il faut être connecté
2. Cliquer sur l'icone de notification (cloche)

## Scenario Nominal

1.	Click sur l'icone de notification (cloche)  
2.	Un sous-menu s'ouvre  
3.	La liste des notifications les plus récentes surlignées et non suivi (càd on a pas suivi le lien de la notif) et celles déjà lues sont affichées en temps réel (idéalement)
4. On peut suivre les notifications pour qu'elles soientt mise en "lue"
5. Le compteur de notifications est mis à jour et l'affichage lu/non lu également du centre de notifications.
(Cf. voir schéma)
[schema](https://app.diagrams.net?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=uc_notif_center.drawio#R7Vxbc%2BK4Ev41PEJZvmEeCQmzVTt79pLJzjn7MiVsAaqxLY8vE3J%2B%2FUq2BFiSgcnYJhBIBeyWLNn9dbdarZYH1izafEhhsv6NBCgcmEawGVj3A9OcWAb9ZoSXiuCO7YqwSnFQkcCO8Ij%2FjziRX7cqcICyWsWckDDHSZ3okzhGfl6jwTQlz%2FVqSxLWe03gCimERx%2BGKvUzDvI1pwJ3siv4BeHVmnftmeOqIIKiMn%2BSbA0D8rxHsh4G1iwlJK%2BOos0MhYx3gi%2FVdfOG0u2NpSjOT7lgswK%2F2uOnz%2BNvT4%2F%2F9Yvi%2B3dEhsC0qna%2Bw7Dgj8xvN38RPEhJEQeINQMG1t3zGufoMYE%2BK32moFPaOo9CXrx9TIOerEKYZfw4y1PyFf1OL8Q5EwbAiEschjuSy0gUyRziGKX8ugX0v67KW%2Fi9yENawDsKUpJ8gukK5ZzAHwSlOdo08ghsOU8lFpEI5ekLrSLEVYgdl1bT4OfPe9h7nLbeg90RKEMub6tt2ztI6AFHRY%2BQFSPwZ%2FY8%2B837Bz8U9odfsv99GFpAAeiJtmQM6f9%2FSI6X2Ic5JnFGz2f0MSnfZPwoP3IJpBKLGQkJ43JMGFNLLCQSDPEqpqd%2B1bB1x7hLOwynvCDCQcC60UrFTm5KqCmuj%2FymgDiv9N0U5aL7gWnZ9%2BxvC6uCoQbpRliBNxk5NWAdFdfxRIOr1Rms5nG9q4SdgyWsj1lHsk8uGpbERU%2Fl4sTVcBG0wEW9%2BVKYSM2ZUcQpggE9iOv6IbF3j4tCrD%2FCBQr%2FIBlmV9CyBclzEukUIWQ177amaY%2Fly%2FKj0ZWcJFo068pIWzAMz5gbsi0NYLbeKhMtSdhjRJsVG3ZHmGTjEaamMxstSh62YQ23g5ywhhMVbxeocLtdwa2OVZaCKm2G%2BgZNJmkPc5gllcOwxBvGVw0yTJnmMMIhY8AnuCYRZPXYeBWv7rhs3Ns72l%2BcCVpYF55jO4ZkaJnAeD7y%2FbYgqw9glmErkAnTU7NzZkeQOcfNXE2wFUXbM3DA3JP8tARP4aVQPo1Ssc%2B%2BUrXkM1hjyWewND6DobOKXld64ipMLz0FSgJNzoE0bhhTwzKcQwM%2Bl%2FiPaFn6X5YEFVOKFGX0TCgUUNF6KD8H0ToJoGbJU1E7horNJTZFIR03vtenAa0jNW5EStWTBqQEp34GKQkXVH60CF4yUryLPwimt7PVV9GMuIIslxmdU8jIbm%2Fs9WB7jWCrw1iHYL8PtdSDPTH6AnvSCLZ9XrCvD1Rg9abCY1WHFTSFh4KjMrZ0p5ln1KcER2cfJ0w2ys6mwqU1dP4tv5%2F7dZ6z4NmUMcec%2B0FsljOHJaaT9XTk0x7NeQBzSH%2FKGQX9XRaxz27qCyN8KXk793Hqh%2BhLioJREq8OClaTfWlyOloXRN6K5KkBS3HUTI2UthHa0QuTOvrfhOlShclVvf5%2BhUl1%2Bm%2FCdKnCBIwzmybvhGUBFAdTtsJCz3wW58e%2BGpps5iEKlIWXn3YyHF1k3vg5H4MD5EkAAcnlyEiR%2BohftGO%2B0g6YHGkoL5c0lIbacmCAiE5clZ0wjtoJeocvwwWkQjqEcZASHAzDYUhYsJAkQ1ZrSJ3pr7SmabM2izQj6RCYHjch9TWwI4tcJ1ia%2BYz9ncHSOFK0Sh22LI0WtbEOoh%2B2TggQHjM0JxiUhhBeP7bDtKWgrGy2TzUelnOkoY6Nh6eut%2FQ5KpwVRFtWHOeVIDrukYa6BtG8gbhbHmkJRKWhrkG0byBueS8H9V4NotxQ1yCqY99HjOJq2Gf5HEWMSnZl1RMpCL%2BdxI5XezCH19Ycye02hdzvRxbHGlHrbmKkTrNvmB3EzNKth%2FaLmRq0vWF2GDNNZk%2B%2FmAlTfMPsZNtonx2z8waNzuqUjNuaHsgBIkdOnmtwSihX4ctetYRVyJpv2DP0N9x0X3J9YdZPrW%2Fbh%2BuPzR%2BrL%2FNJqk8PKo60u6irc7vdkBmaRUqPVnkpqu%2BFMp3%2BPTBZMvLUp6rDcrjLs4cNqQ7%2BpBVhxKxi9T0djUaKRRDBxiQlPmKBtGOJe00J4T1H%2BY8ly9ojU8o51sTaqBSLnNpaati4MxutWyaqcF0Dgesj62yN45Uool3tSgUxEYSPJEUR6zjJCvYblCylIGOmrzBiizJMHFgoFvk5ygtWCgOcYGr%2Fy24MFGJeK6ODJ2uDEXGRRYSd5ihKyjZx7OMAB0VpCgr2FcIF7Z%2FVzkXf7CyCqxiybkL8rYCjvSdJdg%2FSms%2FAMzEowdmdfWKx8fthmZetk2lCJWwZlmPhmroU1Lvp0X3YLgQckk7dgAnkka092TwhuWLPf%2BCs36aPguvwJCxpIHRfG6Oy7SMNdb3UJPrT5EAVSQBzpujvzWu3JLVzgUbtdLlSnXntQCQF78FkDm67KNraRWGP67soHNdREO91FwUQucV1wGVD%2B673UdhSQoYjQDzXPgpgnBDxv7h1e%2Bt4fg81O%2FyQ8XaevcT%2B0AB7K%2FNvyu23HMnn1wQ%2FD%2FkOHcjNCUmGl77ALi%2FkvNplcpWkvr5dphNc4AvfLzWWAkPOqR5Qd%2FulgNGcrf%2B2dkxt04a6yOLn0ndQi9%2FAnikAmucVqrZc7a6p%2FtCSbGXv%2B6YAUGco73Dn1LkB72%2FvFADqDOWKd0%2BdG9ge908BcI3TmCvaptAoi29z18s2ff4mT1chT2ff%2BAKAOgN74pHQK%2FQsj7wOyzHkRUzTUwNhB8emt%2BlQqvO9m9V4i%2FE0YAB3NK6LoGWAkRpC79dKmOoUdGC69OFBpXqnH%2F71A6blokIMP2xabN3L9n7UtPwkrLoNLlXiAONjDST3W0FEwTArOTxl8aJJstkVKrkzgjCDSWkeWHLAdC85YSFfwdS27Lr1nIULWTGdWOP6CKTLJzZdXRqN3Z3%2Bq9OYp3JJu7yvfE3K1JS5c%2FmjytUt0Uyk4cTRvNWu3yUa8xpfKvJet%2BQeFj5TWvzQbY7odf8tMK%2FRFb4Jn3bHAJCDN6ob3a%2FwaV5uPAsxY%2FtNAq9RAieeNPZq1n5bkkB6unu3ehU42L2g3nr4Fw%3D%3D)
###	Extensions
3. Problème de requête en base, on ne parvient pas à obtenir les notifications.
3. bis. Problème d'inner link, le lien suivi de la notification ne mène nul part.


## Post Conditions
### Conditions de succès 
Le menu s'est bien ouvert avec les notifications les plus récentes.

### Minimal Guarantees
Les notifications restent stockées en base X temps. (Ad vitam aeternam pour le moment)
Elles sont temps réel (idéalement) et s'affichent dynamiquement (idéalement)

### Conditions final en cas d'échec
Le centre de notification est vide pour cause de problème de requête
OU
L'inner link suivi mène sur une page error html 404

### Frequence
souvent  
### Besoins Spéciaux (optionel)  
Web socket, inner links, front JS
### Performance  
###	Security  
###	Usability / Accessibility  
###	Other  

##	Problèmes et étapes suivantes  
* Liens internes
* Websocket
* API Rest 

FIXME définir ce qui pose problème dans la description **actuelle** du cas d'utilisation.  
FIXME vous pouvez ajouter ici un lien vers une issue github ou un carte de projet github.

TBR
