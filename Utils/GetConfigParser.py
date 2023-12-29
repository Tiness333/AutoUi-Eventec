import configparser
from ConfigFiles.ConfigPath import elementLocationPath

class GetConfigParser:

    def __init__(self):
        self.cp=configparser.ConfigParser()
        self.cp.read(elementLocationPath)

    #读取ini文件里写的内容并将其封装为字典
    def getSection(self,sectionName):
        optionPath = dict(self.cp.items(sectionName))
        return optionPath





if __name__ == '__main__':

    parse=GetConfigParser()
    print(parse.getSection('163mail_login'))