# -*- coding: utf-8 -*-
# -- ---------------------------------------------------------------------------
# --
# -- Title: run.py
# -- Date:  31 May 2017
# --
# -- ---------------------------------------------------------------------------
import timestamp
import time
import datetime
import os 

def date_time_stamp_with_string(string_to_print):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%d-%m-%Y %H:%M:%S")
    print string_to_print + ' ' + st

while True:
    date_time_stamp_with_string('Hello world')
    print 'Printing config'
    print os.environ.get('example_db')
    print '** Doing stuff **'
    time.sleep(5)
    print '** Sleeping **'
    time.sleep(10)
