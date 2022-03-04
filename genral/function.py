import os
import re
from opencc import OpenCC
from . import IGNORE_DIRS, IGNORE_EXTE, IGNORE_FILE


def get_filename_after_add_prefix(file_name: str, prefix: str):
    '''回傳 新增前綴後的檔名'''
    return f"{prefix}{file_name}"


def get_filename_after_replace_keyword(file_name: str, replace_dict: dict):
    '''回傳 替換指定字詞後的檔名'''
    if len(replace_dict) != 0:
        for keyword in replace_dict.keys():
            file_name = re.sub(keyword, replace_dict[keyword], file_name)
        return file_name


def get_filename_after_translation_ch_tw(file_name: str):
    '''回傳 簡翻繁後的檔名'''
    convert = OpenCC('s2twp.json')
    return convert.convert(file_name)


def get_filename_after_change_extension(file_name: str, old_e: str, new_e):
    '''回傳 更換指定副檔名後的檔名'''
    return re.sub(old_e, new_e, file_name)


def get_file_extension(file_path):
    '''取得副檔名'''
    return os.path.splitext(file_path)[1][1:]


def mapping_dir(dir_path):
    '''取得所有檔案路徑'''
    stack = []
    files = os.listdir(dir_path)
    for file in files:
        if os.path.isdir(f"{dir_path}/{file}"):
            if file not in IGNORE_DIRS:
                stack += mapping_dir(f"{dir_path}/{file}")
        else:
            if file not in IGNORE_FILE and get_file_extension(file) not in IGNORE_EXTE:
                stack.append(f"{dir_path}/{file}")
    return stack
