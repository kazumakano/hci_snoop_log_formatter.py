# log_formatter.py
This is Python module to convert logs format from CSV exported by Wireshark to CSV able to be interpreted by [particle_filter.py](https://github.com/kazumakano/particle_filter.py).

## Usage
You can run this formatter as following.
You can specify source file or directory and target directory with flags.
Default source and target directory are `raw/` and `formatted/`
```sh
python script/format_logs.py [--src_file PATH_TO_SRC_FILE] [--src_dir PATH_TO_SRC_DIR] [--tgt_dir PATH_TO_TGT_DIR]
```
