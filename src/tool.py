from . import logger
from typing import Union
import os


def get_all_files(path: str, exclude_extensions: Union[list[str], None] = None, exclude_dirs: Union[list[str], None] = None, exclude_files: Union[list[str], None] = None, add_abspath: bool = False, exclude_dir: bool = True, mapping_sub_dir: bool = False) -> list[str]:
    """取得所有檔案

    Args:
        path (str): 檔案資料夾
        exclude_extensions (Union[list[str], None], optional): 指定排除副檔名,若無指定則全部列出. Defaults to None.
        exclude_dirs (Union[list[str], None], optional): 指定排除資料夾,若無指定則全部列出. Defaults to None.
        exclude_files (Union[list[str], None], optional): 指定排除檔名,若無指定則全部列出. Defaults to None.
        add_abspath (bool, optional): 列出 絕對路徑. Defaults to False.
        exclude_dir (bool, optional): 回傳的內容排除資料夾. Defaults to True.
        mapping_sub_dir (bool, optional): 映射子資料夾的檔案. Defaults to False.

    Returns:
        list[str]: 回傳串列
    """
    target_file_path = []
    path = os.path.abspath(path)

    for file in os.listdir(path):

        is_dir = False

        if exclude_dir:
            is_dir = os.path.isdir(f'{path}/{file}')
            logger.debug(f'{path}/{file}, 是資料夾:{is_dir}')

        if not is_dir:
            if add_abspath:
                target_path = f'{path}/{file}'
            else:
                target_path = f'{file}'

            _, file_extension = os.path.splitext(file)
            if exclude_extensions and exclude_files:
                logger.debug(f'{file_extension[1:]} in {exclude_extensions}: {file_extension[1:] not in exclude_extensions}')
                logger.debug(f'{file} in {exclude_files}: {file not in exclude_files}')
                if file_extension[1:] in exclude_extensions or file in exclude_files:
                    logger.debug(f'pass {target_path} - 排除副檔名或檔名')
                else:
                    logger.debug(f'add {target_path}')
                    target_file_path.append(target_path)
            elif exclude_extensions:
                logger.debug(f'{file_extension[1:]} not in {exclude_extensions}: {file_extension[1:] not in exclude_extensions}')
                if file_extension[1:] not in exclude_extensions:
                    logger.debug(f'add {target_path}')
                    target_file_path.append(target_path)
                else:
                    logger.debug(f'pass {target_path} - 排除副檔名')
            elif exclude_files:
                logger.debug(f'{file} not in {exclude_files}: {file not in exclude_files}')
                if file not in exclude_files:
                    logger.debug(f'add {target_path}')
                    target_file_path.append(target_path)
                else:
                    logger.debug(f'pass {target_path} - 排除檔名')
            else:
                logger.debug(f'add {target_path}')
                target_file_path.append(target_path)
        else:
            # 資料夾處理
            if mapping_sub_dir:
                logger.debug('進行映射子資料夾')
                if exclude_dirs:
                    logger.debug('進行排除資料夾')
                    logger.debug(f'{file} not in {exclude_files}: {file not in exclude_files}')
                    if file in exclude_dirs:
                        logger.debug(f'pass {path}/{file} - 排除資料夾')
                        continue

                logger.debug(f'映射 {path}/{file}')
                # 遞迴
                files = get_all_files(
                    path=f'{path}/{file}',
                    exclude_extensions=exclude_extensions,
                    exclude_dirs=exclude_dirs,
                    exclude_files=exclude_files,
                    add_abspath=add_abspath,
                    exclude_dir=exclude_dir,
                    mapping_sub_dir=mapping_sub_dir
                )
                target_file_path.extend(files)

    target_file_path.sort()
    return target_file_path
