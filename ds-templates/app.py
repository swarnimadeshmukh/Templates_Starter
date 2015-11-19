from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')          						#This is the main URL
@app.route('/index')
def index():
    return render_template("index.html", name="index", title="HOME")		#The argument should be in templates folder

@app.route('/interests')   
def interests():
    return render_template("interests.html", name="interests", title="INTERESTS")

#Add the code for courses
@app.route('/courses')   
def courses():
    return render_template("courses.html", name="courses", title="COURSES")

#Add the code for other
@app.route('/other')   
def other():
    return render_template("other.html", name="other", title="OTHER")


if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
