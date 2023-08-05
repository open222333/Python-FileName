# Python-FileName

## 使用方法

conf/config.ini 進行設定

```json
[
  {
    "execute": true, // 是否執行
    "replace_word": { // 替換字詞 可設定多種
      "old_word1": "new_word1",
      "old_word2": "new_word2"
    },
    "replace_extension": { // 替換副檔名
      "old_extension1": "new_extension1",
      "old_extension2": "new_extension2"
    },
    "exclude_dirs": [ // 排除資料夾
      ".git",
      "__pycache__"
    ],
    "exclude_files": [ // 排除檔案
      ".gitignore"
    ],
    "exclude_extensions": [ // 排除副檔名
      "md",
      "yml",
      "cnf",
      "env",
      "docx"
    ]
  }
]
```

```bash
usage: main.py [-h] [-p PATH] [--to_tc] [--remove_space] [--mapping_sub_dir] [--replace_word] [--replace_extension] [--prefix PREFIX]

批量修改檔名

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  目標資料夾
  --to_tc               簡體轉繁體
  --remove_space        移除檔名空白
  --mapping_sub_dir     遍歷子資料夾
  --replace_word        替換字詞
  --replace_extension   替換副檔名
  --prefix PREFIX       添加前綴
```