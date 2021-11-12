import argparse
import csv
import os.path as path
from datetime import datetime
from glob import iglob
from typing import Union

ROOT_DIR = path.dirname(__file__) + "/../"

def _format_log(src_file: str, tgt_dir: str) -> None:
    with open(src_file) as f:
        reader = csv.reader(f)
        next(reader)    # skip first row
        row = next(reader)
        log_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f").date()    # get date from second row

        with open(tgt_dir + str(log_date) + ".csv", mode="a") as g:
            writer = csv.writer(g)
            writer.writerow((row[0], row[1], row[2][:-4]))
            for row in reader:
                writer.writerow((row[0], row[1], row[2][:-4]))

    print(f"{path.basename(src_file)} has been loaded")
    print(f"written to {log_date}.csv")

def format_logs(src_file: Union[str, None] = None, src_dir: Union[str, None] = None, tgt_dir: Union[str, None] = None) -> None:
    if tgt_dir is None:
        tgt_dir = ROOT_DIR + "formatted/"    # save to default target directory

    if src_file is None and src_dir is None:
        for src_file in iglob(ROOT_DIR + "raw/*.csv"):    # loop for default source directory
            _format_log(src_file, tgt_dir)

    elif src_file is None:
        for src_file in iglob(src_dir):    # loop for specified source directory
            _format_log(src_file, tgt_dir)

    elif src_dir is None:
        _format_log(src_file, tgt_dir)

    else:
        raise Exception("'src_file' and 'src_dir' are specified at the same time")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src_file", help="specify source file", metavar="PATH_TO_SRC_FILE")
    parser.add_argument("--src_dir", help="specify source directory", metavar="PATH_TO_SRC_DIR")
    parser.add_argument("--tgt_dir", help="specify target directory", metavar="PATH_TO_TGT_DIR")
    args = parser.parse_args()
    
    format_logs(args.src_file, args.src_dir, args.tgt_dir)
