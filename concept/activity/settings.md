
### Settings des exercices/ACTIVITÉS

Les settings d'un exercice sont stockés dans l'activité car c'est elle qui décide comment doit être joué l'exercice.

1) l'activité définie le "mode" d'affichage de l'exercice dans l'activité
2) l'activité fait les appels de "grading" des exercice et donc c'est l'activité qui décide comment afficher l'exercice une fois que le réponse de la sandbox a été reçu.
3) l'activité reçoit le json de réponse du grader et donc peut en fonction de celle ci décider de l'étape suivante, c'est le rôle des settings de définir l'algorithme.
------------

# les modes d'affichage d'un exo

Le mode "play" les inputs sont actifs sinon on est en mode "answer" ou les inputs sont disabled.

En plus de "play" et "anwser" ont peut ajouter l'évaluation. 
Le mode "evaluation" contient un feedback standard et le grade/100 de l'exercice si le settings feedback est possitionné il y a aussi affichage du feedback, dans le cas ou le feedback est dans l'input celui ci est visible.

Le mode "validate" ajoute un "bouton validation" ou un "bouton suivant".

# Fonctionnement
```
Tant qu'il y a des exercices dans la variable main.
Affichage de l'exercice courrant en mode "play" avec le bouton "validate".
Quand "validate" envois à la sandbox la "réponse" de l'étudiant.

Retour de la sandbox :  
if grade==-1 (Erreur de syntaxe): continue.   
if setting.evaluation == False :  
   // Pas d'évaluation exercice suivant.   
else:  
     if grade==100  grade<100 and settings.nbtry == exo.nbtry :  
       // exo terminé avec success ou trop long  
       Affichage du mode "anwser".   
       Bouton suivant et si settings.reroll bouton reroll  
       //exercice suivant.  
     elif grade<100 and settings.nbtry > exo.nbtry :  
        Affichage de mode "play" avec évaluation et feedback (si settings.feedback)  
        Attente du click du bouton "suivant".   


Appel de next et l'on passe en mode "play" pour l'exercice suivant.

```
donc

```
settings.nbtry = nbr d'essai par tentative 0 (default) = infinity, 1  
settings.reroll = True(default)|False en cas d'echec autorisation de relancer l'exercice (pour les exercices caculatoire répétables)  
settings.feedback = True(default)|False # Affichage du feedback, analyse d'erreur, proposé par l'exercice, sinon pas de feedback.  
settings.evaluation = True(default)|False # affichage de l'évaluation (numérique) de l'exercice, ou pas.  
settings.validation = True(default)|False # le bouton de validation est géré par l'exercice, sinon il est géré par l'activité. Dangereux si l'on oublie de le proposer dans l'activité.   

DEFAULTSETTINGS = { 'nbtry':0, 'reroll':True, 'syntactic':True, 'feedback':False, 'evaluation':False, 'validation'=True }  
STEPSSETTINGS = { 'nbtry':1, 'reroll':False, 'syntactic':True, 'feedback':True, 'evaluation':True, 'validation':True }  
STANDARDSETTINGS = { 'nbtry':1, 'reroll':True, 'syntactic':True, 'feedback':True, 'evaluation':True, 'validation':True }  
EXAMSETTINGS =  {  'reroll':False, 'syntactic':True, 'feedback':False, 'evaluation':False, } # autres settings laissé a l'exercice  
CARROUSELSETTINGS=  {  'validation':False,'feedback':False, 'evaluation':False } # autres settings laissé a l'exercice  
settings.syntactic = True(default)|False  l'exercice peut si il y a une erreur de syntaxe dans la réponse autoriser une tentative non décomptée, sinon cela consome un essai, dans les deux cas si il y a encore un essai, le feedback d'erreur de saisie ou de syntaxe est fournis à l'utilisateur. 
