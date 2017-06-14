#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='xxxxxxxx/python-postgres.log',
                    format='"%(asctime).19s", "%(name)s", "%(levelname)s",'
                           '"%(message)s"')

log = logging.getLogger(__name__)

SQL_STATEMENT = """COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"""


def process_file(conn, table_name, file_object):
    cursor = conn.cursor()
    cursor.copy_expert(sql=SQL_STATEMENT % table_name, file=file_object)
    conn.commit()
    cursor.close()
