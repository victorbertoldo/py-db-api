# "Database code" for the DB Forum.
import psycopg2
import datetime

# conn = psycopg2.connect(dbname="test", user="postgres", password="secret")

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(dbname=DBNAME, user="postgres", password="postgres")
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  return c.fetchall()
  db.close()
  

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(dbname=DBNAME, user="postgres", password="postgres")
  c = db.cursor()
  c.execute("insert into posts values (%s)", (content,))
  db.commit()
  db.close()


