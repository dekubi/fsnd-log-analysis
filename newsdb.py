import psycopg2

DBNAME = "news"

def get_popular_article():
    """Return all articles from the database, most popular article comes first"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT title, COUNT(*) AS views
            FROM authors,articles,log
            WHERE authors.id=articles.author AND log.path='/article/'||articles.slug
            GROUP BY articles.title
            ORDER BY views DESC;""")
    popular_article = c.fetchall()
    db.close()
    return popular_article

def get_popular_author():
    """Return all authors from the database, most popular author comes first"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT name, COUNT(*) AS view
                FROM authors,articles,log
                WHERE authors.id=articles.author and '/article/'||articles.slug=log.path
                GROUP BY authors.name
                ORDER BY view DESC;""")
    popular_author = c.fetchall()
    db.close()
    return popular_author

def get_request_error():
    """Return request errors from the database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT * FROM (SELECT date(time) AS date,round(100.0*sum(case status when 
                '200 OK' then 0 else 1 end)/count(status),2) AS error FROM log group
                BY date ORDER BY  error DESC) AS subquery WHERE error > 1;""")
    request_error =  c.fetchall()
    db.close()
    return request_error
                  
                







    