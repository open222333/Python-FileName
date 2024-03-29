from configparser import ConfigParser
from datetime import datetime
from traceback import print_exc
from pprint import pprint
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler

import logging
import socket
import json
import os


class Log():

    def __init__(self, log_name: str) -> None:
        self.log_name = log_name
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.WARNING)

        # 當前日期
        self.now_time = datetime.now().__format__('%Y-%m-%d')

        self.log_path = 'logs'
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

        self.log_file = os.path.join(self.log_path, f'{log_name}-all.log')
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def set_log_path(self, log_path: str):
        """設置log檔存放位置

        Args:
            log_path (str): 路徑 預設為 logs
        """
        self.log_path = log_path
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

    def set_log_file_name(self, name: str):
        """設置log檔名稱 預設為 {log_name}-all.log

        Args:
            name (str): _description_
        """
        self.log_file = os.path.join(self.log_path, name)

    def set_date_handler(self, days: int = 7) -> TimedRotatingFileHandler:
        """設置每日log檔

        Args:
            log_file (_type_): log檔名
            days (int, optional): 保留天數. Defaults to 7.

        Returns:
            TimedRotatingFileHandler: _description_
        """
        self.log_file = os.path.join(self.log_path, f'{self.log_name}-{self.now_time}.log')
        handler = TimedRotatingFileHandler(self.log_file, when='D', backupCount=days)
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)

    def set_file_handler(self, size: int = 1 * 1024 * 1024, file_amount: int = 5) -> RotatingFileHandler:
        """設置log檔案大小限制

        Args:
            log_file (_type_): log檔名
            size (int, optional): 檔案大小. Defaults to 1*1024*1024 (1M).
            file_amount (int, optional): 檔案數量. Defaults to 5.

        Returns:
            RotatingFileHandler: _description_
        """
        handler = RotatingFileHandler(self.log_file, maxBytes=size, backupCount=file_amount)
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)

    def set_msg_handler(self) -> logging.StreamHandler:
        """設置log steam

        Returns:
            logging.StreamHandler: _description_
        """
        handler = logging.StreamHandler()
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)

    def set_log_formatter(self, formatter: str):
        """設置log格式 formatter

        %(asctime)s - %(name)s - %(levelname)s - %(message)s

        Args:
            formatter (str): log格式.
        """
        self.formatter = logging.Formatter(formatter)

    def set_level(self, level: str = 'WARNING'):
        """設置log等級

        Args:
            level (str): 設定紀錄log等級 DEBUG,INFO,WARNING,ERROR,CRITICAL 預設WARNING
        """
        if level == 'DEBUG':
            self.logger.setLevel(logging.DEBUG)
        elif level == 'INFO':
            self.logger.setLevel(logging.INFO)
        elif level == 'WARNING':
            self.logger.setLevel(logging.WARNING)
        elif level == 'ERROR':
            self.logger.setLevel(logging.ERROR)
        elif level == 'CRITICAL':
            self.logger.setLevel(logging.CRITICAL)

    def debug(self, message: str, exc_info: bool = False):
        self.logger.debug(message, exc_info=exc_info)

    def info(self, message: str, exc_info: bool = False):
        self.logger.info(message, exc_info=exc_info)

    def warning(self, message: str, exc_info: bool = False):
        self.logger.warning(message, exc_info=exc_info)

    def error(self, message: str, exc_info: bool = False):
        self.logger.error(message, exc_info=exc_info)

    def critical(self, message: str, exc_info: bool = False):
        self.logger.critical(message, exc_info=exc_info)


config = ConfigParser(os.environ)
config.read(f"conf/config.ini")

try:
    LOG_PATH = config.get('LOG', 'LOG_PATH', fallback='logs')
    # 關閉log
    LOG_DISABLE = config.getboolean('LOG', 'LOG_DISABLE', fallback=False)
    # 關閉記錄檔案
    LOG_FILE_DISABLE = config.getboolean('LOG', 'LOG_FILE_DISABLE', fallback=False)
    # 設定紀錄log等級 預設WARNING, DEBUG,INFO,WARNING,ERROR,CRITICAL
    LOG_LEVEL = config.get('LOG', 'LOG_LEVEL', fallback='WARNING')

except Exception as err:
    print_exc()

# 建立log資料夾
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

if LOG_DISABLE:
    logging.disable()

logger = Log()
logger.set_level(LOG_LEVEL)
if not LOG_FILE_DISABLE:
    logger.set_date_handler()
logger.set_msg_handler()

# 目標資料夾
TARGET_DIR = config.get('SETTING', 'TARGET_DIR', fallback="target")

# 是否為測試 預設 關
IS_TEST = config.getboolean('SETTING', 'IS_TEST', fallback=False)

# json檔路徑 預設 conf/word.json
JSON_PATH = config.get('SETTING', 'JSON_PATH', fallback="conf/word.json")
with open(JSON_PATH, 'r') as f:
    INFO = json.loads(f.read())
