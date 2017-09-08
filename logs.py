import pyscopg2

def main ():
    conn_string = "host='localhost' dbname='news'"
    conn = psycopg2.connection(conn_string)
    cursor = conn.cursor()
    print "Connected\n"


    
