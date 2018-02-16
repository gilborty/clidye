#!/usr/bin/env python
# -*- coding: utf-8 -*-

import clidye


def main():
    logger = clidye.Clidye('tester', 
                            verbose=True, 
                            enable_logging=True,
                            logging_file='./tester.log',
                            log_fmt='JSON')
    logger.info('Info')
    logger.debug('Debug')
    logger.warning('Warning')
    logger.fatal('Fatal')

if __name__ == '__main__':
    main()