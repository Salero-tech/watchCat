import docker
from dockerInteract.watchContainer import WatchContainer
APPLICATION_NAME = "watchCat"

class WatchCat:
    client:docker.DockerClient
    monitoredContainers:list[WatchContainer] = []

    def __init__(self) -> None:
        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    def getMonitoredContainers (self):
        #get all containers
        allContainers = self.client.containers.list()

        #filter monitored containers
        for container in allContainers:
            #does contain key application name
            labels = container.labels
            if not (APPLICATION_NAME in labels.keys()):
                continue

            if labels[APPLICATION_NAME] == 'True':
                self.monitoredContainers.append(WatchContainer(container, self.client))

    def getContainersWithUpdates (self):
        updatableContainers = []

        for container in self.monitoredContainers:
            if container.isUpdateAvilable():
                updatableContainers.append(container)
        
        return updatableContainers
