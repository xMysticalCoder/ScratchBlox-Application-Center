from flask import Flask, redirect, url_for, render_template, request, jsonify
import keep_alive
from replit import db

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("home.html")
@app.route("/applied", methods=["GET", "POST"])
def applied():
  if request.method == "POST":
    user = request.form.get("username")
    job = request.form.get("job")
    work = request.form.get("work")
    optional = request.form.get("optional")
    if user in db.keys():
      return "You have already applied before. If you want to change your application, contact xMysticalCoder"
    else:
      print(user)
      print(job)
      print(work)
      print(optional)
      db[user] = str(job)+":"+str(work)+":"+str(optional)
      return "Applied!"
  return render_template("home.html")

@app.route("/applications")
def applications():
  return f"{db.keys()} <br><br> {db.values()}"


if __name__ == "__main__":
  app.run("0.0.0.0")