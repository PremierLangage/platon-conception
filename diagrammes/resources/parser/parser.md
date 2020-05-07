Les parsers de PL doivent permettre de fournir deux sortie :

* Une fournissant un dictionnaire permettant l'exécution d'un exercice.
* L'autre permettant à l'éditor d'offrir des fonctionnalité de linter et de colorisation syntaxique.

## Dictionnaire d'exécution

Le dictionnaire doit contenir l'ensemble des clés déclarées dans le fichier parsé. Il contient en plus
4 clés suffixé par deux underscore `__` :

* `parser__` : Identifiant unique indiquant le parser utilisé pour obtenir le dictionnaire.
* `files__` : Resources qui seront envoyés sur la sandbox les fichier `grader.py` et `builder.py`
sont obligatoires.
* `dependencies__` : Autres resources dont dépends ce PL (extends, fichier envoyé sur la sandbox, etc...)
* `filtered__` : Dictionnaire des filtres à appliquer pour une variable. Chaque clés doit correspondre à une
variable déclaré. L'ordre de la lsite correspond à l'ordre d'application des filtres.


```json
{
    "parser__" : "[parser]",
    "files__" : {
        "grader.py": "[resource]",
        "builder.py": "[resource]",
        "[filename1]": "[resource1]",
        "[filename2]": "[resource2]",
    },
    "dependencies__" : ["[resource1]", "[resource2]"],
    "filtered__": {
      "[var1]": ["[filter1]", "[filter2]"],
      "[var4]": ["[filter1]"]
    },
    "[var1]": "[value1]",
    "[var2]": "[value2]",
    "[var3]": "[value3]",
    "[var4]": "[value4]"
}
```

## Dictionnaire pour l'éditeur
