
# Cas d'utilisation N° 15 :  communication-cercle

Niveau 1

## Description

L'idée est de fournir un / plusieurs moyens de communication pour permettre au membres d'un même **[cercle](https://github.com/PremierLangage/plconception/blob/master/conception/concept/cercle.md)**   de communiquer.

Il peut être utile d'avoir deux moyens de communication à différentes vitesse. L'un s'apparenterais plus à un chat et permettrais un échange rapide (discord / slack / riot).
L'autre permettrais un échange plus formet et réfléchis (forum / QA), utilisant un système de notification ([envoyer-notification.md](envoyer-notification.md)) pour signaler toutes nouvelles réponses.

Il est problement intéressant d'exporter ces fonctionnalités sur des services existants.

En plus de ces moyen de communication, une page d'annonce est mise à disposition du Président du cercle (en Markdown), celle-ci pourra contenir des liens vers les différents mediums choisis.

Le scénario ci-dessous ne concerne que l'édition de la page de présentation par le président.

> **Niveau** : Haut niveau
> **Déclencheur** : Clique de la part du président sur le bouton d'édition de la page de présentation. 
> **Acteur Primaire**: Président
 
 
## Preconditions
Être enseignant et appartenir à un cercle.


## Scenario Nominal.
1.	Depuis la vue de président du cercle, celui-ci clique sur le bouton d'édition de la page de présentation du cercle.
2. Le président effectue les modifications de la page de présentation.
3. Le président valide ses modifications à l'aide du bouton "Sauvegarder"
4. Les modifications sont sauvegardé et le président redirigé sur la vue de président du cercle.

### Extensions
2. Le président effectue les modifications de la page de présentation.
3. Le président annule ses modifications à l'aide du bouton "Annuler"
4. Le président redirigé sur la vue de président du cercle.


## Post Conditions
### Conditions de succès 
La page de présentation à été correctement modifié.

### Minimal Guarantees
Les modifications de l'enseignant ne sont perdu que si celui-ci annule personnellement sont édition.

### Conditions final en cas d'échec
La page de présentation à n'a pas été modifiée.


### Frequence
Peu souvent.
