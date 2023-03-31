import smtplib
from dockerInteract.watchContainer import WatchContainer
from email.mime.text import MIMEText

class MailNotify:
    configMap:map = {}
    containerList:list[str] = []

    def __init__(self, config:map) -> None:
        for groupName in config:
            if not ('mail' in config[groupName].keys()):
                return
            self.configMap[groupName] = config[groupName]["mail"]

    def addContainer (self, container:WatchContainer):
        #if no mail return
        if self.configMap == {}:
            return
        
        self.containerList.append(container)

    def generateHtml (self, htmlListItems:list):
            
            return f"""
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <style>
                        table {{
                            font-family: arial, sans-serif;
                            border-collapse: collapse;
                            width: 100%;
                        }}

                        td, th {{
                            border: 1px solid #dddddd;
                            text-align: left;
                            padding: 8px;
                        }}

                        tr:nth-child(even) {{
                            background-color: #dddddd;
                        }}
                    </style>
                </head>

                <body>
                    <h2>available Updates:</2h>
                    <table>
                        <tr>
                            <th>name</th>
                            <th>id</th>
                            <th>image</th>
                        </tr>
                        {"".join(htmlListItems)}
                    </table>
                </body>

                </html>
                """


    def send (self):
        #if no mail return
        if self.configMap == {}:
            return
        
        htmlListItems = []

        #if group setup for mail send mail
        for group in self.configMap:
            groupHasContainer = False

            for container in self.containerList:
                #check group
                if group in container.groups:
                   groupHasContainer = True
                   htmlListItems.append(f"""
                    <tr>
                        <td>{container.name}</td>
                        <td>{container.idShort}</td>
                        <td>{container.imageName}</td>
                    </tr>
                    """)
                    
            
            print(self.configMap[group])
            if groupHasContainer:
                #set variables
                fromMail = f"Watch Cat <{self.configMap[group]['from_mail']}>"
                toMail = self.configMap[group]["to_mail"]
                

                #create html msg
                html = self.generateHtml(htmlListItems)
                msg = MIMEText(html, "html")
                msg['from'] = fromMail
                msg['to'] = ", ".join(toMail)
                msg['subject'] = "docker updates"

                #set smtp connection
                smtpServer = smtplib.SMTP(self.configMap[group]["host"], self.configMap[group]["port"])
                smtpServer.login(self.configMap[group]["user"], self.configMap[group]["passwd"])

                #send msg
                smtpServer.sendmail(fromMail, toMail, msg.as_string())
                smtpServer.quit()