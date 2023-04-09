import apprise
from notify.template import Template



class NotificationItem:
    url:str
    template:Template

    def __init__(self, config) -> None:
        self.url = config["url"]
        self.template = Template(config["template"])

    def send(self, dictList):
        #setup apprise
        apobj = apprise.Apprise()
        apobj.add(self.url)
        apobj.notify(
        body_format=self.template.type,
        body=self.template.getStringWithInserts(dictList),
        title=self.template.titel,
        )
        
