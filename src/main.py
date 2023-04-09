from dockerInteract.watchCat import WatchCat
from dockerInteract.watchContainer import WatchContainer
from notify.notify import Notify
import schedule
import time
import fileSystem

class Main:
    config = {}
    def __init__(self) -> None:
        fileSystem.init()
        #loadconfig
        self.config = fileSystem.loadConfigFile()
        #set up scheduel for running periodically
        schedule.every(self.configInterval["every"]).day.at(self.configInterval["time"]).do(self.run)
    
    def loop (self):
        while True:
            #reload config
            self.config = fileSystem.loadConfigFile()
            schedule.run_pending()
            #sleep until next job
            time.sleep(schedule.idle_seconds())
    
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