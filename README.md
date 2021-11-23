# hci_snoop_log_formatter.py
This is Python module to convert logs format from CSV exported by Wireshark to CSV able to be interpreted by [particle_filter.py](https://github.com/kazumakano/particle_filter.py).

## Usage
### format_logs.py
You can run formatter as following.
You can specify source file or directory and target directory with flags.
Default source and target directory are `raw/` and `formatted/`.
```sh
python script/format_logs.py [--src_file PATH_TO_SRC_FILE] [--src_dir PATH_TO_SRC_DIR] [--tgt_dir PATH_TO_TGT_DIR]
```

### sort_logs.py
You may need to run sorter after formatting logs if there are multiple log files which are logged on same date.

You can run sorter as following.
You can specify file or directory with flags.
Default directory is `formatted/`.
```sh
python script/sort_logs.py [--file PATH_TO_FILE] [--dir PATH_TO_DIR]
```
