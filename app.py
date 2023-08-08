from flask import Flask, render_template, jsonify
from database import load_jobs_position_db

app = Flask(__name__)

@app.route("/")
def home_page():
  JOBS_POSITIONS =  load_jobs_position_db()
  return render_template("home.html", jobs_positions=JOBS_POSITIONS)

@app.route("/jobs-positions")
def jobs_positions():
  JOBS_POSITIONS =  load_jobs_position_db()
  return jsonify(JOBS_POSITIONS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
