from flask import Flask, render_template

app = Flask(__name__)

JOBS_POSITIONS = [{
  "id": 0,
  "title": "Data Analyst",
  "local": "SC, Brazil",
  "salary": "R$ 5,000"
}, {
  "id": 1,
  "title": "Frontend Developer",
  "local": "RJ, Brazil",
  "salary": "R$ 3,500"
}, {
  "id": 2,
  "title": "Backend Developer",
  "local": "RJ, Brazil",
  "salary": "R$ 3,800"
}, {
  "id": 3,
  "title": "Mobile Developer",
  "local": "TX, USA",
  "salary": "US$ 5,000"
}, {
  "id": 4,
  "title": "Product Owner",
  "local": "AM, Brazil",
  "salary": "R$ 7,000"
}]


@app.route("/")
def home_page():
  return render_template("home.html", jobs_positions=JOBS_POSITIONS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
