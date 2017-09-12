import pyscopg2
DB_NAME = "news"

query1 = "select..."

query2 = "select..."

query3 = "select..."

#store results
query1_returns =
query1_returns['title'] =

query2_returns =
query2_returns['title'] =

query3_returns = dict()
query3_returns['title'] =

def return_query(query)
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results
