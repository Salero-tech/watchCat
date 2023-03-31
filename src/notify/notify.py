from dockerInteract.watchContainer import WatchContainer
from notify.discord import DiscordNotify
from notify.mail import MailNotify

class Notify:
    discord:DiscordNotify
    mail:MailNotify

    def __init__(self, config) -> None:
        self.setupGroups(config)

    def setupGroups (self, config):
        self.discord = DiscordNotify(config)
        self.mail = MailNotify(config)


    def sendNotifications (self, containers:WatchContainer):
        for container in containers:
            self.discord.addContainer(container)
            self.mail.addContainer(container)
            
        self.discord.send()
        self.mail.send()