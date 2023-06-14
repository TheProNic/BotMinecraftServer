import ping as p


server = p.Ping('mc.hypixel.net')
print('couou')
print(server.isOnline())
print(server.getPlayersOnline())
print(server.getPlayersMax())