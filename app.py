from flask import Flask
from flask import render_template

app = Flask(__name__)   # flask will expose port 5000

class Mentee:           # must likely we need a login form to fill in these fields and then need a way to put into database
    def __init__(self, name, school, major, interests):
        self.name = name
        self.school = school
        self.major = major
        self.interests = []
        for i in interests:
            self.interests.append(i)


class Mentor:
    def __init__(self, name, school, major, interests):
        self.name = name
        self.school = school
        self.major = major
        self.interests = []
        for i in interests:
            self.interests.append(i)
    

@app.route('/')         # main page, for now this is a test to see if it serves
def hello():        
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
