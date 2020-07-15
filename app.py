import sqlite3 as sql
from flask import Flask, render_template, request

app = Flask(__name__)   # flask will expose port 5000
DATABASE = 'database.db'

# class User:           # must likely we need a form to fill in these fields and then need a way to put into database
#     def __init__(self, name, school, major, role, interests):
#         self.name = name
#         self.school = school 
#         self.major = major
#         self.role = role        # mentor or mentee
#         self.interests = []     # will probably need to be a fixed assortment from frontend
#         for i in interests:
#             self.interests.append(i)


@app.route('/')         # main page, for now this is a test to see if it serves
def hello():        
    return render_template('index.html')

@app.route('/login')
def new_student():
    return render_template('student.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        try:
            name = request.form['name']
            school = request.form['school']
            major = request.form['major']
            role = request.form['role']
         
            with sql.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,school,major,role) VALUES (?,?,?,?)",(name,school,major,role))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        con.close()
        return render_template("result.html",msg = msg)

@app.route('/list')
def list():
   con = sql.connect(DATABASE)
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.run(debug=True)
