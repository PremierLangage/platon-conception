# reload

Le serveur de ressource propose un méthode reload.

### Quand ?

Lorsqu'un utilisateur veut modifier une ressource déjà existante.

### Principe

Les ressources sont stockées sur le serveur de ressource. Lorsqu'un client voudra modifier une ressource, il effectuera un **reload**.
Ce **reload** créera une nouvelle branche de la ressource modifiée. Il ira ensuite appeler la méthode **load** qui transformera la ressource en JSON qui sera envoyé au serveur d'Assets.

Le serveur d'Assets réceptionnera l'asset et devra checker la version de tous les files du JSON (qui auront une version de packetage). Il mettra ensuite dans le checkbox les fichiers inexistant ou ceux qui ont une version inférieure à ceux reçu dans le JSON.
