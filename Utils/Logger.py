import time
from ConfigFiles import ConfigPath
from loguru import logger

# logger.debug('this is a debug message')
# logger.info('this is a info message')
# logger.warning('this is a warning message')
# logger.error('this is a error message')
# logger.success('this is a success message')
# logger.critical('this is a critical message')

class Log:

    #单例，运行程序保证只有一个实例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance = super(Log,cls).__new__(cls)
        return cls.instance

    def __init__(self):
        '''
        根据时间生成.log文件
        '''
        logger.add(ConfigPath.logPath+'/runtime_{}.log'.format(time.time()))
        # logger.add('runtime_{}.log'.format(time.time()))

    def debug(self,message):
        logger.debug(message)

    def info(self,message):
        logger.info(message)

    def error(self,message):
        logger.error(message)

    def warning(self,message):
        logger.warning(message)
