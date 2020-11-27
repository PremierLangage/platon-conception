
# Cas d'utilisation N° 35 :  utilisation-etabli (edition-ressource)

Niveau 1

##	Description

 Le membre veux créer ou modifier une ressource (crud).
 
 Soit il choisi la ressource qu'il veux éditer (ouverture automatique de l'établi et vérification qu'il est autorisé a le faire),
 Soit il choisi un établi dans lequelle il a le droit de créer une ressource.

 
 

> **Déclencheur** : être dans view "etablie"  et choisir de creer ou modifier une ressources
> **Acteur Primaire**: Membre   

 
 
## Preconditions

être logger en comme membre: [login.md](login.md)
[choisir-cercle.md](choisir-cercle.md) qui implique le choix d'un établi.

## Scenario Nominal



 1 L'enseignant clique sur une ressource dans les ressource de l'établi  ou le bouton créer ressource.
 1. Creation : choisir le type de ressource que l'on créer.    
   -> composite ouvre l'éditeur composite.  
   -> programmable ouvrer l'editeur programmable (pl? activités programmable). 
   -> préparé ouvir l'editeur adapté.  
2. idem avec la ressource sélectionné, récupère le type pluis on ouvre l'éditeur correspondant  
3. interaction avec l'éditeur  
 -> voir IHM/MC. 
 -> modification eventuelle des versioin (voir la fin de ce docuement). 
4. Sauvegarde -> sauvegarde la ressource, mise à jour, des liens de version,  
 et notification des propréitaires des ressources qui dépende de celle ci.  


###	Extensions

FIXME Indiquez dans quel point du scenario nominal le chemin alternatif démarre et ou il reprend.


## Post Conditions
### Conditions de succès 
La base donnnée contient la nouvelle version de la ressource, les propriétaire de ressource dépendant de celle ci sont prévenus. 


### Minimal Guarantees

### Conditions final en cas d'échec


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

```
# fichier toto.pl

extends= /model/thsqdflq.pl [valide]  # récupère le version valide la plus récente (comportement par défaut)

[last] # recupère la dernière version  

@ cercle:/gichier/alacon.py [123] # y aune problème avec la dernirère version je choisi la 123

--------------
# meta données toto

local: reference de l'établi dans lequel 
version:{ "/model/thsqdflq.pl" : 123, 
        "cercle:/gichier/alacon.py": 23,
        }

# meta données de /model/thsqdflq.pl uen par version 
valide=


Save /model/thsqdflq.pl ou valide un nouvelle version:
-> notifier le proprietaire/créateur des fichiers incluant /model/thsqdflq.pl par exemple toto.pl 

========
save totot.pl
    --> verifier les versions de tout les fichiers
    Pour tout les fichier référencés da,s toto.pl 
        Si il y a une version plus récente de "/model/thsqdflq.pl" : {132}
            --> lancer  l'éditeur de version 
                --> soit je conserve la version 123
                --> soit je choisie une autre version 124-132
                --> soit je créer une nouvelle version de "/model/thsqdflq.pl"
        on soauvergade dans les méta data la version choisi 
        
        
get filename,label=[#version,last,valide]





vous pouvez ajouter ici un lien vers une issue github ou un carte de projet github.

TBR
