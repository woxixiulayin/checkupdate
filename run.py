#!/usr/bin/env python
#!coding: utf-8

from config import *
from check_update import *
import time
import os
import sys
import datetime

config = config_6605
sleep_time = 60
# config = config_test


def run(config):
    logger.info('begin to check')
    result, update, msg = check_update(config)
    if result == 0 and update == True:
        Notice(config, msg)
    logger.info(datetime.datetime.now())
    logger.info('sleep %d second' % sleep_time)
    time.sleep(sleep_time)
    # for n in range(60):
    #     time.sleep(60)
    #     logger.info('sleep %d second' % n)

if __name__ == "__main__":
    while True:
        run(config)
