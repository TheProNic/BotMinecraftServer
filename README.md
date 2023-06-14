# BotMinecraftServer
Ce projet doit avoir :
- Un bot discord qui :
  - choisir le channel dans lequel apparait le message d'update
  - envoie un message quand l'état d'un serv mc change (online/offline)
  - (optionnel) dire combien de joueur / joueurs max son co

- Un systeme de ping au serveurs minecraft (mctools) qui :
  - ping les serveurs pour get les infos (online/offline/players/...)
  - ping toutes les 30 min pour pas agir sur le TPS

- Une BDD qui : 
  - contient toutes les IP a ping

Table de sauvegarde des ip :

| Colonne | Type |
|---------|------|
| id      | int  |
| ip      | varchar(50) |
| is_online | boolean |
