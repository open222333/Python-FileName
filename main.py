from src.filename import FileName
from src.tool import get_all_files
from src import TARGET_DIR, INFO, IS_TEST, logger
from argparse import ArgumentParser
import os

parser = ArgumentParser(description='批量修改檔名')
parser.add_argument('-p', '--path', help='目標資料夾', default=TARGET_DIR)
parser.add_argument('--to_tc', action='store_true', help='簡體轉繁體')
parser.add_argument('--remove_space', action='store_true', help='移除檔名空白')
parser.add_argument('--mapping_sub_dir', action='store_true', help='遍歷子資料夾')
parser.add_argument('--replace_word',  action='store_true', help='替換字詞')
parser.add_argument('--replace_extension', action='store_true', help='替換副檔名')
parser.add_argument('--prefix', type=str, help='添加前綴')
args = parser.parse_args()

if __name__ == '__main__':

    for info in INFO:
        if info['execute']:
            files = get_all_files(
                path=TARGET_DIR,
                exclude_extensions=info['exclude_extensions'],
                exclude_dirs=info['exclude_dirs'],
                exclude_files=info['exclude_files'],
                add_abspath=True,
                exclude_dir=True,
                mapping_sub_dir=args.mapping_sub_dir
            )

            for file in files:
                filename = os.path.basename(file)
                filepath = os.path.dirname(file)

                fn = FileName(filename)

                if args.replace_word:
                    logger.debug(f'替換字詞: {info["replace_word"]}')
                    fn.replace_keyword(info['replace_word'])
                if args.to_tc:
                    fn.to_tc()
                if args.prefix:
                    logger.debug(f'增加前綴: {args.prefix}')
                    fn.add_prefix(args.prefix)
                if args.replace_extension:
                    for extension in info['replace_extension'].keys():
                        if fn.extension == extension:
                            logger.debug(f'替換副檔名: {extension} -> {info["replace_extension"][extension]}')
                            fn.change_extension(info["replace_extension"][extension])
                            break
                if args.remove_space:
                    fn.remove_space()

                filename = fn.get_filename()

                if file != f'{filepath}/{filename}':
                    logger.info(f'{os.path.basename(file)} 更名為 {filename}')
                    if not IS_TEST:
                        os.rename(file, f"{filepath}/{filename}")
                else:
                    logger.info(f'未更動:{os.path.basename(file)}')
