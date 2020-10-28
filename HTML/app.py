from flask import Flask, render_template
 
app = Flask(__name__)

@app.route("/") 
def home():

    return render_template("index.html")

@app.route("/bar.html") 
def bar():

    return render_template("bar.html")

if __name__ == "__main__":
    app.run()





  
