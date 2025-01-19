from flask import *
from datamanager import DBMmanager

app = Flask("my firs program")
db_name = "Projects.db"
app.secret_key = "228"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/projeckts")
def show_page():
    db_manager = DBMmanager(db_name)
    projeckts = db_manager.get_projeckts()
    return render_template("projects.html" , projeckts=projeckts)


@app.route("/projeckts/<int:poj_id>")
def show_projeckt(poj_id):
    #nomer = session["quest_index"]
    #q = session["questions"][nomer]
    db_manager = DBMmanager(db_name)
    projekts = db_manager.get_projeckts()
    projekt = projekts[poj_id]


    return render_template("projecktpsssport.html" , poj_id=poj_id , projekt=projekt)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)