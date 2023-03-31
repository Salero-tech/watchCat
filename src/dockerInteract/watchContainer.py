import docker

class WatchContainer:
    container:docker.models.containers.Container
    client:docker.DockerClient

    def __init__(self, container:docker.models.containers.Container, client) -> None:
        self.container = container
        self.client = client

    @property
    def name (self):
        return self.container.name
    
    @property
    def groups (self):
        labels = self.container.labels
        #check if any group specified if not return default
        if not "watchCat.group" in labels:
            return ["default"]
        
        #if specified return groups specified
        #convert to list
        return self.container.labels["watchCat.group"].split(" ")

    @property
    def idShort (self):
        return self.container.short_id

    @property
    def imageName (self):
        img = self.container.image
        return img.tags[0]

    def isUpdateAvilable (self) -> bool:
        #local img
        img = self.container.image
        repoIdLocal = img.attrs["RepoDigests"][0].split("@")[1]

        #remote img
        imgReg = self.client.images.get_registry_data(self.imageName)
        repoId = imgReg.id

        #is update available
        self.update = repoId != repoIdLocal
        return self.update

    def __str__ (self):
        return f"{self.name}, {self.idShort}, {self.isUpdateAvilable()}"
