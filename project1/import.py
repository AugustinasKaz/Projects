import os, csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():

    db.execute("CREATE TABLE reviews (username VARCHAR PRIMARY KEY, isbn TEXT NOT NULL, review TEXT NOT NULL) ")

    db.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, year SMALLINT NOT NULL)")
    f=open("books.csv")
    reader =csv.reader(f)
    line_count = 0
    for isbn,title,author,year in reader:
        if line_count == 0:
         line_count += 1
        else:
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:a,:b,:c,:d)",{"a":isbn,"b":title,"c":author,"d":year})
            line_count += 1
    print(f'Processed {line_count} lines.')

    print('created')
    db.commit()



if __name__ == "__main__":
    main()