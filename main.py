from flask import Flask, render_template,request,redirect
from fun import *

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    registration_status=""
    if request.method=="POST":
        register_stud(request.form["stud_name"],request.form["stud_age"],request.form["course"],request.form["address"])
        data=read_json()
        registration_status="success"
        return render_template("index.html",stud_data=data["students"],registration_status=registration_status)
    data=read_json()
    return render_template("index.html",stud_data=data["students"],registration_status=registration_status)


@app.route("/delete/<id>")
def delete(id):
    delete_stud(id)
    return redirect("/")


@app.route("/update/<id>",methods=["POST","GET"])
def update(id):
    if request.method=="POST":
        update_stud(id,request.form["stud_name"],request.form["stud_age"],request.form["course"],request.form["address"])
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
    
