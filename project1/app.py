import os
import requests
import json
from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods = ["GET", "POST"])    
def index():
   
   if request.method == "POST" or request.method == "GET":
     return render_template("welcome.html")
  
@app.route("/register", methods = ["GET", "POST"])
def register():
    
   session.clear() 
   
   if request.method == "POST":

      if not request.form.get("username"):
         return apology("Must provide username")
      if not request.form.get("password"):
         return apology("Must provide password")
      if request.form.get("password") != request.form.get("password2"):
         return apology("passwords does not match")
      if len(request.form.get("password")) <= 3:
         return apology("password must be longer than 3 characters")
      if db.execute("SELECT * FROM vartotojai WHERE username1 =  :username", {"username": request.form.get("username")}).rowcount == 1:
          return apology("Username already exists")   
      db.execute("INSERT INTO vartotojai(username1, hash1) VALUES(:username, :hash)",{"username": request.form.get("username"), "hash": generate_password_hash(request.form.get("password"))})
      db.commit()
      return redirect("/login")      

   else:
     return render_template("register.html")      

@app.route("/login", methods = ["GET", "POST"])    
def prisijungti():

   session.clear()

   if request.method == "POST":
      if not request.form.get("username"):
         return apology("Must provide username")
      if not request.form.get("password"):
         return apology("Must provide password")
         
      hello2 = db.execute("SELECT * FROM vartotojai WHERE username1= :username", {"username": request.form.get("username")}).fetchone()
      if hello2 == None:
         return apology("Invalid username")
      if not check_password_hash(hello2.hash1, request.form.get("password")):
         return apology("invalid password")

      session["user_id"] = hello2.username1
      return redirect("/home")   

   else:
      return render_template("login.html")

@app.route("/logout")
def atsijungti():

   session.clear()
   return redirect("/login")

@app.route("/home", methods = ["GET", "POST"])
@login_required
def home():

   if request.method == "POST" or request.method == "GET":
      return render_template("home.html")

@app.route("/results", methods = ["GET", "POST"])
@login_required
def results():
   text = request.form.get("duom")
   if db.execute("SELECT * FROM books WHERE isbn iLIKE '%"+text+"%' OR author iLIKE '%"+text+"%' OR title iLIKE '%"+text+"%'  ").rowcount == 0:
     return apology("Opps! no books with found with provided information")
   else:   
    Results = db.execute("SELECT * FROM books WHERE isbn iLIKE '%"+text+"%' OR author iLIKE '%"+text+"%' OR title iLIKE '%"+text+"%'  ").fetchall()
   
   return render_template("results.html", results=Results) 

@app.route("/results/<string:code>" , methods = ["POST", "GET"])
def book(code):

   username = session.get("username")
   book = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": code}).fetchone()
   if book is None:
      return apology("no book")
   res = requests.get('https://www.goodreads.com/book/review_counts.json', params={"key": "OpEFZNL2Q2nsZdVGE985Q", "isbns": code})
   average_rating = res.json()['books'][0]['average_rating']
   count1 = res.json()['books'][0]['average_rating']
   count2 = res.json()['books'][0]['work_ratings_count']
   count3 = res.json()['books'][0]['work_reviews_count']

   return render_template("book.html", book=book, average_rating=average_rating, work_reviews_count=count3, work_ratings_count=count2)    



def apology(message):
    def escape(s):
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", bottom=escape(message))


