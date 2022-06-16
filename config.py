"""
日志配置
"""
import logging
from logging import handlers
import os

# 工程根目录
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def init_log_config():
    print('init_log_config')
    # 日志格式输出
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    # 创建日志器
    logger = logging.getLogger('tpshop')
    logger.setLevel(logging.INFO)
    # 创建 输出到控制台的处理器
    sh = logging.StreamHandler()
    # 输出到控制台的级别是error级别
    # sh.setLevel(logging.INFO)
    # 创建 输出到文件 的处理器
    # fh = logging.FileHandler('../log/tpshop_test.log', 'w', encoding='utf-8')
    # 创建输出到文件 处理器
    fh = logging.handlers.TimedRotatingFileHandler(BASE_DIR + '/log/WebAutoTest.log', when='S',
                                                   interval=5,
                                                   backupCount=5,
                                                   encoding='utf-8')
    # 输出到文件的级别是debug级别
    # fh.setLevel(logging.INFO)
    # 创建格式器
    formater = logging.Formatter(fmt)
    # 给处理器设置格式
    fh.setFormatter(formater)
    sh.setFormatter(formater)
    # 将处理器加入日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
