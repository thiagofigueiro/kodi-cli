# -*- coding: utf-8 -*-
"""kodi-cli
Usage:
  kodi (-h | --help)
  kodi videolibrary (clean|update)

Options:
  -h --help     Show this screen.
"""
from docopt import docopt


def cmd_videolibrary(args):
    """Process the videolibrary command"""
    if args.get('clean'):
        print('clean goes here')
    elif args.get('update'):
        print('update goes here')
    else:
        raise NotImplementedError


def main():
    """console script entrypoint"""
    arguments = docopt(__doc__, version='kodi-cli 0.1.0')
    if arguments.get('videolibrary'):
        cmd_videolibrary(arguments)
    else:
        raise NotImplementedError
