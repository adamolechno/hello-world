#!/usr/bin/env python

import pyhs2
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='xxxxxxx/python.log',
                    format='"%(asctime).19s", "%(name)s", "%(levelname)s",'
                           '"%(message)s"')

log = logging.getLogger(__name__)

log.debug('Connect to hiveserver2.')

with pyhs2.connect(host='xxxxx', port=10000,
                   authMechanism="KERBEROS", database='test') as conn:
    with conn.cursor() as cur:
        cur.execute("""select * from abc""")
        for i in cur.fetch():
            print i
