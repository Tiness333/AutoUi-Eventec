
import  os

#获取整个项目的根目录
ParentDirPath = os.path.dirname(os.path.dirname(__file__))
#获取elementLocation.ini文件的位置
elementLocationPath = os.path.join(ParentDirPath,u'ConfigFiles\elementLocation.ini')

#获取TestData文件的位置
xlsxPath = os.path.join(ParentDirPath,u'TestData\loginData.xlsx')

#获取log日志文件的位置
logPath = os.path.join(ParentDirPath,u'Logging')

#获取商品图片文件的位置
image_path = os.path.join(ParentDirPath,u'BasePages\6.png')