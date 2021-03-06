# coding=utf-8
import logging
import time
import os

f_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(f_path), "logs")
# 判断项目下是否有logs文件夹，没有就创建一个
if not os.path.exists(log_path): os.makedirs(log_path)

class Log():
    def __init__(self):
        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        print ()
    def __printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__printconsole('debug', message)
    def info(self, message):
        self.__printconsole('info', message)
    def warning(self, message):
        self.__printconsole('warning', message)
    def error(self, message):
        self.__printconsole('error', message)
if __name__ == "__main__":
    log = Log()
    st="猪"
    a=st.encode("unicode")
    log.info(a)
    log.info("__________end____________")
    print (os.path.abspath(log_path))