import os
import sys

def check_reboot():
    ''' Retrun True if a computer has a pending reboot '''
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Prending Reboot..")
        sys.exit(1)
    print("Everything okay..")
    sys.exit(0)

main()