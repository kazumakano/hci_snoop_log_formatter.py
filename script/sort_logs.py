import argparse
import csv
import os.path as path
from datetime import datetime
from glob import iglob
from typing import Union
import numpy as np

ROOT_DIR = path.dirname(__file__) + "/../"

def _sort_log(file: str) -> None:
    ts = np.empty(0, dtype=datetime)     # timestamp
    mac = np.empty(0, dtype=str)         # MAC address
    rssi = np.empty(0, dtype=np.int8)    # RSSI (>= -128)

    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            ts = np.hstack((ts, datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")))
            mac = np.hstack((mac, row[1]))
            rssi = np.hstack((rssi, np.int8(row[2])))

    sorted_index_list = ts.argsort()

    with open(file, "w") as f:
        writer = csv.writer(f)
        is_sorted = False
        last = 0
        for i in sorted_index_list:
            if i < last:
                is_sorted = True
            writer.writerow((ts[i], mac[i], rssi[i]))
            last = i

    if is_sorted:
        print(f"{path.basename(file)} has been sorted")
    else:
        print(f"{path.basename(file)} is already in order")

def sort_logs(file: Union[str, None] = None, dir: Union[str, None] = None) -> None:
    if file is None and dir is None:
        for file in iglob(ROOT_DIR + "formatted/*.csv"):    # loop for default directory
            _sort_log(file)

    elif file is None:
        for file in iglob(dir):
            _sort_log(file)

    elif dir is None:
        _sort_log(file)

    else:
        raise Exception("'file' and 'dir' are specified at the same time")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="specify file", metavar="PATH_TO_FILE")
    parser.add_argument("-d", "--dir", help="specify directory", metavar="PATH_TO_DIR")
    args = parser.parse_args()

    sort_logs(args.file, args.dir)
