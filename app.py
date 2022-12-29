

from flask import render_template
from flask import Flask
from markupsafe import escape
from flask import request



app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World! This is my first flask app'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        thismonth = request.form['thismonth']
        thisyear = request.form['thisyear']
        return f"We are in {thismonth}, {thisyear}. Enjoy what is left of it."
    return '''
        <h1> My Trivial App </h1>
    
        <form method="post">
            <p><input type=text name=thismonth placeholder="Enter This Month Value" >
             <p><input type=text name=thisyear placeholder="Enter This Year Value">
            <p><input type=submit value=predict>
        </form>
    '''

@app.route('/welcome/')
@app.route('/welcome/<name>')
def welcome(name=None):
    return render_template('welcome.html', name=name)


if __name__ == '__main__':
    app.run()

