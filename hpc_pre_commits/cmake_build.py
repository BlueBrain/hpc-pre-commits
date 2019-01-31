import subprocess
import sys


def main():
    exit(subprocess.call(['cmake'] + sys.argv[1:]))


if __name__ == '__main__':
    main()
