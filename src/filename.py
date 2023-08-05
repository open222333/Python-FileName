import os
import re
from opencc import OpenCC


class FileName:

    def __init__(self, filename: str) -> None:
        """_summary_

        Args:
            filename (str): 檔名
        """
        self.set_filename(filename)

    def set_filename(self, filename: str):
        """設置 filename

        Args:
            filename (str): 檔名
        """
        self.filename = filename
        self.name, self.extension = os.path.splitext(self.filename)

    def add_prefix(self, prefix: str):
        """新增前綴後的檔名

        Args:
            prefix (str): 前綴
        """
        self.set_filename(f"{prefix}{self.name}.{self.extension}")

    def replace_keyword(self, replace_dict: dict):
        """替換指定字詞後的檔名

        Args:
            replace_dict (dict): _description_
        """
        if len(replace_dict) != 0:
            for keyword in replace_dict.keys():
                filename = re.sub(keyword, replace_dict[keyword], self.filename)
                self.set_filename(filename)

    def to_tc(self):
        """簡翻繁後的檔名
        """
        convert = OpenCC('s2twp.json')
        filename = convert.convert(self.filename)
        self.set_filename(filename)

    def change_extension(self, new_e: str):
        """回傳 更換指定副檔名後的檔名

        Args:
            new_e (str): _description_
        """
        filename = re.sub(self.extension, new_e, self.filename)
        self.set_filename(filename)

    def remove_space(self):
        """消除空白
        """
        filename = f'{self.name.strip()}{self.extension}'
        self.set_filename(filename)

    def get_file_extension(self) -> str:
        """取得副檔名

        Returns:
            str: _description_
        """
        return self.extension

    def get_filename(self) -> str:
        """取得檔名

        Returns:
            str: _description_
        """
        return self.filename
