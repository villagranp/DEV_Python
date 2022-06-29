import psycopg2

conn = None
try:
    
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
            host="172.16.23.153",
            database="dbliztex",
            user="liztex",
            password="golosin")
    print (conn.encoding)
    conn.set_client_encoding('SQLASCII')
    # create a cursor
    cur = conn.cursor()
    
    # execute a statement
    print('PostgreSQL lzty_variables:')
    cur.execute('SELECT * FROM lzty_variable limit 10;')

    # display the PostgreSQL database server version
    data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    print(column_names)
    for record in data:
        print(record)
        print(record[0])
# close the communication with the PostgreSQL
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')







