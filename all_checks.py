#!/usr/bin/env python3

import shutil
import os
import sys

def check_reboot():
    ''' Retrun True if a computer has a pending reboot '''
    return os.path.exists("/run/reboot-required")


def check_disk_full(disk, min_gb, min_percent):
    '''Return True is there isnt enough disk space otherwise false '''
    du = shutil.disk_usage(disk)
    #calculate the percentage of free disk
    percent_free = 100 * du.free / du.total
    #calculate how many free gigbytes 
    gigabytes_free = du.free / 2** 30

    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False


def main():
    if check_reboot():
        print("Prending Reboot..")
        sys.exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("Disk Full.")
        sys.exit(1)
    
    print("Everything okay..")
    sys.exit(0)

main()