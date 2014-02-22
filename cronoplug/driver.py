"""Main driver implementation."""

from docopt import docopt

def cronoplug(args):
    """Usage: cronoplug --bees"""
    arguments = docopt(cronoplug.__doc__, args)
    if arguments['--bees']:
        print("Covered in bees.")

if __name__ == '__main__':
    from sys import argv
    cronoplug(argv[1:])

