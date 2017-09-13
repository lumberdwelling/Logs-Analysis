import pyscopg2
DB_NAME = "news"

# what are the most popular 3 articles of all time?
query1 = "select..."

# who are the most popular article authors of all time?
query2 = "select..."

# on which days did more than 1% of requests lead to errors?
query3 = "select..."

#store results
query1_returns = dict()
query1_returns['title'] =

query2_returns = dict()
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
