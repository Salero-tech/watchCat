from discord_webhook import DiscordWebhook, DiscordEmbed
from dockerInteract.watchContainer import WatchContainer

class DiscordNotify:
    configMap:map = {}
    containerList:list[str] = []

    def __init__(self, config:map) -> None:
        for groupName in config:
            if not ('discord' in config[groupName].keys()):
                return
            self.configMap[groupName] = config[groupName]["discord"]

    def addContainer (self, container:WatchContainer):
        #if no discord return
        if self.configMap == {}:
            return
        
        self.containerList.append(container)

    def send (self):
        #if no discord return
        if self.configMap == {}:
            return
        
        #if group setup for discord send message
        for group in self.configMap:
            groupHasContainer = False
            #set webhook
            webhook = DiscordWebhook(url=self.configMap[group]["url"], content=self.configMap[group]["onUpdate"])
            embed = DiscordEmbed(title=f'update available!', color='03b2f8')

            for container in self.containerList:
                #check group
                if group in container.groups:
                    embed.add_embed_field(name='name', value=container.name)
                    embed.add_embed_field(name='id', value=container.idShort)
                    embed.add_embed_field(name='image', value=container.imageName)
                    
                    groupHasContainer = True

            if groupHasContainer:
                #send msg
                webhook.add_embed(embed)
                response = webhook.execute()