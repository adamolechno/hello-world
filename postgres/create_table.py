#!/usr/bin/env python
import psycopg2
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='xxxxxxxxxxxxxxxxxxxx/python-postgres.log',
                    format='"%(asctime).19s", "%(name)s", "%(levelname)s",'
                           '"%(message)s"')

log = logging.getLogger(__name__)


def table_company(database, user, host, password):
    try:
        log.info('Connect to database %s' % database)
        conn = psycopg2.connect("dbname= '%s' user='%s'"
                                "host='%s' password='%s'"
                                % (database, user, host, password)
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()

    try:
        log.info('Create table company.')
        cur.execute("""CREATE TABLE IF NOT EXISTS COMPANY(
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL);""")
        conn.commit()
        log.info('Create sucesfully.')
    except:
        log.error('Create table failed!')
        print "I can't create table company!"

if __name__ == "__main__":
    a = table_company('xxx', 'xxx', 'xxx', 'xxx')
