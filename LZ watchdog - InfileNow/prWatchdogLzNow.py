import time
import shutil
import psycopg2
import re
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

import constants

path = constants.PATH
pathExit = constants.PATHEXIT
go_recursively = True

#se setean los patrones para validaciones
if __name__ == "__main__":
    patterns = ["*RESPUESTA.txt"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_modified(event):
    if (event.is_directory == True):
        return False;
    print(f"Warning: {event.src_path} has been modified")
    pathPartes = event.src_path.split('\\')
    file = pathPartes[-1]
    brotenFile = re.search(r"^(FACT|NCRE)_(BRO|TEN)+", file)
    if brotenFile:
        shutil.copy(event.src_path, pathExit+file)
        saveChangeLog('Archivo trasladado correctamente.', file, event.src_path, pathExit)
    
def saveChangeLog(changeLog, filename, source, destiny):
    conn = psycopg2.connect(
            host=constants.DBHOST,
            database=constants.DBNAME,
            user=constants.DBUSER,
            password=constants.DBPASS)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO prChangeLogNowInfile (changelog, filename, source, destiny) VALUES(%s, %s, %s, %s)", 
                    (changeLog, filename, source, destiny ))
    conn.commit() 
    cursor.close()
    conn.close()
    

#se define que metodo ejecutara cada uno de los eventos
#my_event_handler.on_method = metodo_a_ejecutar
my_event_handler.on_modified = on_modified


#se define sobre que path se ejecutara el watchdog

my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

#se inicia el watchdog sobre el objeto definido de manera previa.
my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
    
