import psycopg2

conn = None
try:
    
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
            host="172.16.23.149",
            database="mgpstatus",
            user="liztex",
            password="golosin")

    
    # create a cursor
    cur = conn.cursor()
    
# execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT * FROM status;')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)
    
# close the communication with the PostgreSQL
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')







