from src.function import (
    get_all_files,
    get_filename_after_replace_keyword,
    get_filename_after_translation_ch_tw,
    get_filename_after_add_prefix,
    get_filename_after_change_extension,
    get_file_extension,
    remove_space
)
from src import (
    TARGET_DIR,
    FUNCTION_TRANSLATION,
    FUNCTION_REPLACE,
    FUNCTION_USE_PREFIX,
    FUNCTION_REPLACE_EXTENSION,
    FUNCTION_REMOVE_SPACE,
    FUNCTION_MAPPING_SUB_DIR,
    REPLACE_DICT,
    EXTENSION,
    PREFIX,
    IGNORE_DIRS,
    IGNORE_EXTE,
    IGNORE_FILE,
    IS_TEST,
    logger
)
import os

os.chdir(os.path.dirname(__file__))
files = get_all_files(
    path=TARGET_DIR,
    exclude_extensions=IGNORE_EXTE,
    exclude_dirs=IGNORE_DIRS,
    exclude_files=IGNORE_FILE,
    add_abspath=True,
    exclude_dir=True,
    mapping_sub_dir=FUNCTION_MAPPING_SUB_DIR
)

for file in files:
    filename = os.path.basename(file)
    filepath = os.path.dirname(file)

    if FUNCTION_REPLACE and (len(REPLACE_DICT) != 0):
        logger.debug(f'REPLACE_DICT:{REPLACE_DICT}')
        filename = get_filename_after_replace_keyword(filename, REPLACE_DICT)
    if FUNCTION_TRANSLATION:
        filename = get_filename_after_translation_ch_tw(filename)
    if FUNCTION_USE_PREFIX and PREFIX != None:
        logger.debug(f'PREFIX:{PREFIX}')
        filename = get_filename_after_add_prefix(filename, PREFIX)
    if FUNCTION_REPLACE_EXTENSION and (len(EXTENSION) != 0):
        logger.debug(f'EXTENSION:{EXTENSION}')
        for e in EXTENSION.keys():
            file_e = get_file_extension(filename)
            if file_e == e:
                filename = get_filename_after_change_extension(filename, file_e, EXTENSION[e])
                break
    if FUNCTION_REMOVE_SPACE:
        logger.debug(f'移除檔名空格 開始 /{filename}/')
        filename = remove_space(filename)
        logger.debug(f'移除檔名空格 結束 /{filename}/')

    if file != f'{filepath}/{filename}':
        logger.info(f'{os.path.basename(file)} 更名為 {filename}')
        if not IS_TEST:
            os.rename(file, f"{filepath}/{filename}")
    else:
        logger.info(f'未更動:{os.path.basename(file)}')
