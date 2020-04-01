
# Cas d'utilisation N° 4 :  aav-add-ressource

Niveau 1

##	Description

Un membre (d'un cercle quelconque) est en train de consulter une **[demande](https://github.com/PremierLangage/plconception/blob/master/conception/concept/demande.md)** (un AAV). Il propose un lien vers une ressource pouvant répondre à l'AAV.
 
 C'est une action très simple qui consiste à donner du liens entre les **objectifs pédagogiques** surveillés (les AAV crés par les membres de PLaTon) par PLaTon et les ressources disponibles à l'intérieur du **serveur central** de ressources.
 

> **Déclencheur** : N'importe quand lorsqu'un membre connait la demande (AAV) mais aussi l'existance de la ressource. (l'exercice qui y répond à la demande). Cela peut être une découvrete spontanée, celle d'un rodeur sur les ressources. Ça peut être aussi le membre créateur qui vient de créer un nouvel exercice et qui souhaite renseigner PLaTon sur l'intérêt pédagogique de son nouvel exercice.

> **Acteur Primaire**: [membre](https://github.com/PremierLangage/platon-conception/blob/master/acteur/Membre.md)
> **Acteurs secondaires**: le demandeur (créateur originel de l'AAV).
> **Parties Prenantes concernées** : les autres membres surveillants aussi la demande en question (notification?)
 
 
## Preconditions

- Une demande [crud-aav](https://github.com/PremierLangage/platon-conception/blob/master/UC/Membre/crud-aav.md) a été faite.
- Une ressource existante répond à l'AAV.


## Scenario Nominal


1.	Le système affiche la **demande** (la page de l'AAV).
2.	L'utilisateur clic sur le bouton (ajouter une **réponse** (lier une ressource)).
3.	Cela conduit à une view dans laquelle il y a le champ de réponse et moteur de recherche sur le **serveur central**.
4.	L'utilisateur fait sa recherche, sélectionne une ressource et crée un lien vers la ressource en faisant un commentaire.
4.1 L'utilisateur peut prévisualisé sont commentaire markdown. 
5. Il valide.
6. Le système lui affiche le lien interne de la ressource et le commentaire et son lien de profil.
7. Une notification est envoyée au demandeur et aux personnes qui suivent la demande. 

###	Extensions
6. l'utilisateur n'est pas satisfait et il peut retourner en 4 back du navigateur.


## Post Conditions

### Conditions de succès 

Le lien sur la ressource et le commentaire sont enregistés dans la base de données. Les notifications ont été envoyées.

### Frequence

Un cas simple d'utilisation. 

## Besoins du cas d'utilisation 

Liens Internes vers les ressources.

IHM de selection de ressource -> commun avec l'editeurComposite @mc


