"""Main driver implementation."""

from docopt import docopt

def cronoplug(args):
    """Usage: cronoplug --help"""
    arguments = docopt(cronoplug.__doc__, args)
    if arguments['--help']:
        print(__doc__)

if __name__ == '__main__':
    from sys import argv
    cronoplug(argv)

