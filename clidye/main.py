#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import sys

import clidye

parser = ArgumentParser(
        description="Command line interface for clidye",
        prog="clidye",
        usage='%(prog)s [options] <message>'
        )

parser.add_argument("-m", "--message", default="Testing 1...2...3", help="The message to log")
parser.add_argument("-n", "--name", default="clidye", help="The name of the logger")
    
def run():
    """
        Command line interface for clidye
    """
    args = parser.parse_args()

    logger = clidye.Clidye(args.name, 
                            verbose=True, 
                            enable_logging=True)
    logger.info(args.message)
    logger.debug(args.message)
    logger.warning(args.message)
    logger.fatal(args.message)
