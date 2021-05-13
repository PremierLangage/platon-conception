
## Les tests d'exercices


Les tests d'exercices sont dans un fichier tests.json dans la ressource de l'exercice.

Il est possible de définir des tests pour des modèles.
FIXME : dans ce cas le test doit être édité à la main et contenir des variables ce qui complique les choses.


le test d'un exercice doit contenir :

1 les settings 
2 la seed 
3 un test sur ce que renvois le builder 
3 les valeurs "entrées" correspondant au composant input 
4 un test sur ce que renvois le grader  

Le tout sous forme d'un json.

Si le test ce passe bien pas d'affichage.
Sinon le test affiche l'étape (builder,grader) et le delta entre attendu et optenu. 
