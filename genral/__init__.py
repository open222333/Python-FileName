from configparser import ConfigParser
import json
import os


config = ConfigParser(os.environ)
config.read(f"config.ini")

TARGET_DIR = config.get('FILE', 'TARGET_DIR', fallback="target")

# 翻譯 功能
FUNCTION_TRANSLATION = config.getboolean('FILE', 'FUNCTION_TRANSLATION', fallback=False)

# 替換字詞 功能
FUNCTION_REPLACE = config.getboolean('FILE', 'FUNCTION_REPLACE', fallback=False)
REPLACE_DICT = json.loads(config.get('FILE', 'REPLACE_DICT', fallback="{}"))
# 替換字詞 功能
FUNCTION_REPLACE_EXTENSION = config.getboolean('FILE', 'FUNCTION_REPLACE_EXTENSION', fallback=False)
EXTENSION = json.loads(config.get('FILE', 'EXTENSION', fallback="{}"))

# 加入前綴 功能
FUNCTION_USE_PREFIX = config.getboolean('FILE', 'FUNCTION_USE_PREFIX', fallback=False)
PREFIX = config.get('FILE', 'PREFIX', fallback=None)

# 忽略
IGNORE_DIRS = json.loads(config.get('IGNORE', 'IGNORE_DIRS', fallback="{}"))
IGNORE_FILE = json.loads(config.get('IGNORE', 'IGNORE_FILE', fallback="{}"))
IGNORE_EXTE = json.loads(config.get('IGNORE', 'IGNORE_EXTE', fallback="{}"))
