from flask import Flask, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient
import Scrape 
import joblib

app = Flask(__name__)



@app.route("/") 
def home():
   
    return render_template("index.html")

@app.route("/bar.html") 
def bar():

    return render_template("bar.html")

@app.route("/gantt.html") 
def gantt():

    return render_template("gantt.html")

@app.route("/radial.html") 
def radial():

    return render_template("radial.html")    


@app.route("/scrape") 
def scrape():
    
    data = Scrape.scrapping() #activates the scrapping function
    # linear_model = joblib.load('Linear_model.sav')
    # prediction = linear_model.predict([data])
    # logistic_model = joblib.load('Logistic_model.sav')
    return render_template("scrape.html", xyz = data )
    

if __name__ == "__main__":
    app.run()





  
