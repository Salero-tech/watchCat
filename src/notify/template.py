import yaml
import fileSystem

class Template:
    templateYml:dict

    def __init__(self, path) -> None:
        self.templateYml = fileSystem.loadTemplate(path)

    @property
    def type(self):
        return self.templateYml["type"]
    
    @property
    def titel(self):
        return self.templateYml ["titel"]
    
    @property
    def templateString (self) -> str:
        return self.templateYml ["string"]
    
    @property
    def insertLine (self):
        return self.templateYml ["insert"]
    
    def generateInsertStr (self, data:list[dict]):
        insertStr:str = self.insertLine
        #check and replace data with templates <%name%>
        for key in data:
            if f"<%{key}%>" in insertStr:
                insertStr = insertStr.replace(f"<%{key}%>", data[key])
        return insertStr

    

    def getStringWithInserts (self, dictList):
        insertList = []
        for item in dictList:
            insertList.append(self.generateInsertStr(item))
        
        #set data table into string
        finishedStr = self.templateString.replace(f"<%list%>", "\n".join(insertList))
        return finishedStr