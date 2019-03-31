import os
import sys

def main():
    while True:
        comm = input("[GIT]: ")
        if comm == 'exit':
            sys.exit(0)
            
        else:
            os.system("git " + comm)
            
if __name__ == '__main__':
    main()