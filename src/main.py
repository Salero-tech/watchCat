from dockerInteract.watchCat import WatchCat
from dockerInteract.watchContainer import WatchContainer
from notify.notify import Notify
import schedule
import time
import yaml
import os
import shutil

CONFIG_FILE_PATH = '/usr/src/config/config.yml'
SAMPLE_CONFIG_FILE_PATH = '/usr/src/exampleConfig/config.yml'

class Main:
    def __init__(self) -> None:
        self.loadConfigFile()

        #set up scheduel for running periodically
        schedule.every(self.configInterval["every"]).day.at(self.configInterval["time"]).do(self.run)
    
    def loop (self):
        while True:
            schedule.run_pending()
            #sleep until next job
            time.sleep(schedule.idle_seconds())

    def loadConfigFile (self):
        #check if config file exists
        if not os.path.exists(CONFIG_FILE_PATH):
            shutil.copy(SAMPLE_CONFIG_FILE_PATH, CONFIG_FILE_PATH)

        #load yml config
        file = open(CONFIG_FILE_PATH)
        self.config = yaml.safe_load(file)
        file.close()
    
    def run (self):
        #version check of containers
        cat = WatchCat()
        cat.getMonitoredContainers()
        updatbleList:list[WatchContainer] = cat.getContainersWithUpdates()

        #all containers up to date?
        if len(updatbleList) == 0:
            return

        #notify for updates
        notify = Notify(self.configNotify)
        notify.sendNotifications(updatbleList)

    #data
    @property
    def configNotify (self):
        return self.config["notification"]
    @property
    def configInterval (self):
        return self.config["interval"]


if __name__ == "__main__":
    main = Main()
    #main.run()
    main.loop()