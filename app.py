
from flask import Flask,render_template

app = Flask(__name__)
JOBS =[ 
    {
    "id": "1",
    "title": "Data Analyst",
    "location": "Austin, TX, USA",
    "salary": "$75,000 - $95,000"
  },
  {
    "id": "2",
    "title": "Software Engineer",
    "location": "Bengaluru, Karnataka, India",
    "salary": "₹8,00,000 - ₹15,00,000 per year"
  },
  {
    "id": "3",
    "title": "Marketing Manager",
    "location": "London, UK",
    "salary": "£45,000 - £65,000"
  },
  {
    "id": "4",
    "title": "Marketing Manager",
    "location": "Bangalore, India",
    "salary": "£45,000 - £65,000"
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                          jobs=JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
