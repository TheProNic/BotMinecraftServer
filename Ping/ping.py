# Ping get informations from a minecraft server
import mctools

class Ping():
    def __init__(self, serverName):
        self.serverName = serverName
        self.ping = mctools.PINGClient(serverName)
        self.query = mctools.QUERYClient(serverName)
        self.statistics = self.ping.get_stats()
        self.status = self.statistics['version']['name'][self.statistics['version']['name'].find('O'):]
        self.stats = 'Oupsi'
        try:
            self.stats = self.query.get_full_stats()
        except:
            pass
        self.players = self.stats['players']
        self.players_online = self.players['online']
        self.players_max = self.players['max']

    def getPlayersOnline(self):
        return self.players_online
    
    def getPlayersMax(self):
        return self.players_max
    
    def isOnline(self):
        return self.status == 'Online'
    