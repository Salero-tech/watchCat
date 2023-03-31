from dockerInteract.watchContainer import WatchContainer
from notify.discord import DiscordNotify

class Notify:
    discord:DiscordNotify

    def __init__(self, config) -> None:
        self.setupGroups(config)

    def setupGroups (self, config):
        config = config
        self.discord = DiscordNotify(config)


    def sendNotifications (self, containers:WatchContainer):
        for container in containers:
            self.discord.addContainer(container)
            
        self.discord.send()