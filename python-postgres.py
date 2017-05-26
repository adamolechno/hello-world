#!/usr/bin/env python
import psycopg2
import logging
import json
import datetime

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='[%(asctime).19s] %(levelname)s (%(name)s) %(message)s')


class FirstSelect:
    """
    Class that list all in selected table in database.
    """

    def __init__(self):
        pass

    def selectallfromtable(self, database, tableindatabase):
        """
        Module that select all form specified  table.
        """
        log.info('Connect to database %s' % (database))
        conn_string = ("host='ambari.server' dbname='aolechno' user='aolechno' password='aolechno'")
        try:
            conn = psycopg2.connect(conn_string)
            log.info('Successfully connected to %s databse!' % (database))
        except:
            print "I am unable to connect to the database"

        cursor = conn.cursor()
        log.info('Select all from %s table and write to selectformpostgres.txt file' % (tableindatabase))
        wrtieselecttofile = open('selectformpostgres.txt', 'a')
        cursor.execute("SELECT * FROM %s;" % ('ao'))
        row_count = 0
        for row in cursor:
                row_count += 1
                allrows = json.dumps(row)
                print(allrows)
                log.info('Writes row %s to file selectformpostgres.txt' % (allrows))
                wrtieselecttofile.write("%s\n" % (allrows))
        wrtieselecttofile.close()

    def insertintotable(self, database, tableindatabase):
        """
        """
        log.info('Connect to database %s' % (database))
        conn_string = ("host='ambari.server' dbname='aolechno' user='aolechno' password='aolechno'")
        try:
            conn = psycopg2.connect(conn_string)
            log.info('Successfully connected to %s databse!' % (database))
        except:
            print "I am unable to connect to the database"
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO %s(nr,czas) VALUES ('1', '%s');" %
                           (tableindatabase, datetime.datetime.now()))
            log.info('Insert into table %s values %s %s' %
                     (tableindatabase, '1', datetime.datetime.now()))
            conn.commit()
        except:
            print "I am unable to connect to the database"


if __name__ == "__main__":
    selectall = FirstSelect()
    selectall.selectallfromtable('aolechno', 'ao')
    selectall.insertintotable('aolechno', 'ao')
