import os
import sys
import sqlite3
from subprocess import Popen


import pandas as pd

try:
    target = sys.argv[1]
except IndexError:
    print('file required')
    sys.exit(0)

if os.path.isdir(target):
    print('is directory')
    sys.exit(0)

dirname = os.path.abspath('.')
_, ext = target.rsplit('.', 1)
if ext.startswith('sqlite'):
    Popen("open -a 'DB Browser For Sqlite' {}".format(target), shell=True)
elif ext.lower() == 'csv':
    df = pd.read_csv(target)
    df.to_sql('_dbb', sqlite3.connect('{}.sqlite3'.format(target)), if_exists='replace', index=False)
    sh = Popen("open -a 'DB Browser For Sqlite' {}.sqlite3".format(target), shell=True)

