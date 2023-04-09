from dockerInteract.watchContainer import WatchContainer
from notify.group import Group

class Notify:
    groups:dict[str,Group] = {}

    def __init__(self, config) -> None:
        self.setupGroups(config)

    def setupGroups (self, config):
        for group in config:
            self.groups[group] = Group(group, config[group])



    def sendNotifications (self, containers:list[WatchContainer]):
        #add containers to their groups
        for container in containers:
            for group in container.groups:
                if group in self.groups:
                    self.groups[group].addContainer(container)
                else:
                    print(f"group {group} not found, continuing")

        #sending notifications
        for group in self.groups:
            self.groups[group].send()

        
            