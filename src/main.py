from dockerInteract.watchCat import WatchCat
from dockerInteract.watchContainer import WatchContainer
from notify.notify import Notify
import schedule
import time
import yaml
import os

CONFIG_FILE_PATH = '/usr/src/config/config.yml'

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
            #reload config
            self.loadConfigFile()

    def loadConfigFile (self):
        #check if config file exists
        if not os.path.exists(CONFIG_FILE_PATH):
            exit("config file not found")

        #load yml config
        file = open(CONFIG_FILE_PATH)
        self.config = yaml.safe_load(file)
        file.close()
    
    def run (self):
        print("start scan now")
        #version check of containers
        cat = WatchCat()
        cat.getMonitoredContainers()
        updatbleList:list[WatchContainer] = cat.getContainersWithUpdates()

        #all containers up to date?
        if len(updatbleList) == 0:
            print("no containers to update")
            return

        print("sending notifications")
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