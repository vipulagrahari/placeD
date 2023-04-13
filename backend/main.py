from flask import Flask, jsonify, request
from flask_cors import CORS
from threading import Thread
import json
from database_helper import Database

app = Flask('')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def slash():
  with Database() as db:
    result = db("SELECT * FROM emp")
    result = result.fetchall()

  return json.dumps(result)


# fetch all data code
@app.route('/api/get/all')
def home():
  categories = [
    'Year', 'company_name', 'job_prof', 'job_desc', 'remarks', 'venue', 'date',
    'eligibility', 'ctc', 'college'
  ]
  final_object = []

  with Database() as db:
    result = db("SELECT * FROM jobs")
    result = result.fetchall()

  for job in result:
    temp = {}

    for i, detail in enumerate(job):
      temp[categories[i]] = detail

    final_object.append(temp)
  # print(type(final_object))
  return json.dumps(final_object)


@app.route('/api/post', methods=['POST'])
def post_handler():
  # result = None
  json_dict = request.get_json()
  # print(json_dict)
  year = json_dict["Year"]
  cName = json_dict["company_name"]
  jProf = json_dict["job_prof"]
  jDesc = json_dict["job_desc"]
  rem = json_dict["remarks"]
  venue = json_dict["venue"]
  date = json_dict["date"]
  eligibility = json_dict["eligibility"]
  ctc = json_dict["ctc"]
  college = json_dict["college"]

  try:
    with Database() as db:
      db(
        f"INSERT INTO jobs VALUES ('{year}', '{cName}', '{jProf}', '{jDesc}', '{rem}', '{venue}', '{date}', '{eligibility}', '{ctc}', '{college}')"
      )

  except:
    return json.dumps([{"message": "Database Error"}])

  return json.dumps([{"message": "Success"}])


@app.route('/api/get/<int:year>')
def getYear(year):
  categories = [
    'Year', 'company_name', 'job_prof', 'job_desc', 'remarks', 'venue', 'date',
    'eligibility', 'ctc', 'college'
  ]
  final_object = []

  try:
    with Database() as db:
      result = db(f"SELECT * FROM jobs WHERE year == {str(year)}")
      result = result.fetchall()

    if len(result) == 0:
      return json.dumps([{"Message": "No Records Found"}])
    
    for job in result:
      temp = {}

      for i, detail in enumerate(job):
        temp[categories[i]] = detail

      final_object.append(temp)

    return json.dumps(final_object)

  except:
    return json.dumps([{"Message": "Database Error"}])


def run():
  app.run(host='0.0.0.0', port=7000)


t = Thread(target=run)
t.start()
