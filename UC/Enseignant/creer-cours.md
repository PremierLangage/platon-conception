
# Cas d'utilisation N° 20 :  creer-cours

Niveau 1

##	Description

Permet de créer un cours avec rien dedans (un cours vide) Utilise [choisir-cercle.md](choisir-cercle.md). Quand le prof créer son cours il doit le placer dans un cercle disciplinaire. **[coursvide](https://github.com/PremierLangage/plconception/blob/master/conception/concept/coursvide.md)**  

> **Niveau** : objectif utilisateur
> **Déclencheur** : Cliquer pour la première fois sur un lien d'un LMS menant sur un serveur d'assets  
> **Acteur Primaire**: Enseignant   
 
 
## Preconditions

Avoir accès à un LMS utilisant LTI
Avoir les droits d'édition sur un cours du LMS
Avoir la clé et le secret du serveur d'assets pour créer une activité externe sur le LMS

## Scenario Nominal

1.	Créer un lien sur le LMS menant vers un serveur d'assets  
2.	Cliquer sur ce lien
3.	Un cours vide est alors créé sur PLaTon.
4.	Il faut choisir un cercle disciplinaire pour ce cours
5. L'enseignant peut désormais utiliser son cours sur PLaTon


## Post Conditions
### Conditions de succès 
Le cours est créé sur PLaTon, et des étudiants peuvent y accéder depuis le LMS

### Minimal Guarantees
Un cours vide est créé

### Conditions final en cas d'échec
Si le lien a déjà été cliqué, le cours n'est pas créé et on y accède directement



### Frequence
Assez rarement

### Besoins Spéciaux (optionel)  
Le cours créé sur PLaTon doit etre unique pour le cours sur le LMS d'origine.

###	Security  
Un étudiant ne peut pas créé un cours, seul un utilisateur ayant le role enseignant sur le LMS le peut

###	Usability / Accessibility  
Un lien vers la racine du site sur le LMS permet de créer le cours en question depuis le LMS (assez facile de créer une activité externe)

##	Problèmes et étapes suivantes 

[create-classe.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/create-classe.md)

[integrer-mon-cours.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/integrer-mon-cours.md)

[partage-cours.md](https://github.com/PremierLangage/platon-conception/blob/master/UC/Enseignant/partage-cours.md)
TBR
