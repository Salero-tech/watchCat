from notify.notificationItem import NotificationItem
from dockerInteract.watchContainer import WatchContainer

class Group:
    name:str
    notifications:list[NotificationItem] = []
    containerList:list[WatchContainer] = []

    def __init__(self, name ,groupConfig) -> None:
        #why python list should be empty
        self.notifications = []
        self.containerList = []
        self.name = name
        self.setupNotifications(groupConfig)

    def setupNotifications (self, config):
        for notification in config:
            self.notifications.append(NotificationItem(config[notification]))
    
    def send (self):
        #gathering data
        containerDictList =  []
        for container in self.containerList:
            containerDictList.append(container.toDict())

        #sending notifications
        for item in self.notifications:
            item.send(containerDictList)

    def addContainer (self, container:WatchContainer):
        self.containerList.append(container)

