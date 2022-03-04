from genral.function import mapping_dir
from genral.function import get_filename_after_replace_keyword
from genral.function import get_filename_after_translation_ch_tw
from genral.function import get_filename_after_add_prefix
from genral.function import get_filename_after_change_extension, get_file_extension
from genral import TARGET_DIR
from genral import FUNCTION_TRANSLATION, FUNCTION_REPLACE, FUNCTION_USE_PREFIX, FUNCTION_REPLACE_EXTENSION
from genral import REPLACE_DICT, EXTENSION, PREFIX
import os


os.chdir(os.path.dirname(__file__))

if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)

files = mapping_dir(TARGET_DIR)

for file in files:
    filename = os.path.basename(file)
    filepath = os.path.dirname(file)
    if FUNCTION_REPLACE and (len(REPLACE_DICT) != 0):
        filename = get_filename_after_replace_keyword(filename, REPLACE_DICT)
    if FUNCTION_TRANSLATION:
        filename = get_filename_after_translation_ch_tw(filename)
    if FUNCTION_USE_PREFIX and PREFIX != None:
        filename = get_filename_after_add_prefix(filename, PREFIX)
    if FUNCTION_REPLACE_EXTENSION and (len(EXTENSION) != 0):
        for e in EXTENSION.keys():
            file_e = get_file_extension(filename)
            if file_e == e:
                filename = get_filename_after_change_extension(filename, file_e, EXTENSION[e])
                break
    os.rename(file, f"{filepath}/{filename}")
