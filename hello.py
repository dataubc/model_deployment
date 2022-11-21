

from flask import render_template
from flask import Flask
from markupsafe import escape
from flask import request
from joblib import load
import pandas as pd

app = Flask(__name__)

model_path = "models/model.pkl"
with open(model_path, 'rb') as file:
    model = load(file)

@app.route('/')
def hello():
    return 'Hello, World! This is my first flask app'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        gas_type = request.form['gas_type']
        water_content = float(request.form['water_content'])
        viscosity = float(request.form['viscosity'])
        time_minutes = float(request.form['time_minutes'])
        inputs = [[gas_type,water_content,viscosity,time_minutes]]
        df = pd.DataFrame(inputs, columns=['Gas', 'Water_content',
                                         'viscosity','time_minutes'])
        prediction = model.predict(df)[0]
        prediction = round(prediction, 2)
        
        return render_template('predict.html', prediction_text='Estimated IFT =  {} mN/m'.format( prediction))
    

@app.route('/welcome/')
@app.route('/welcome/<name>')
def welcome(name=None):
    return render_template('welcome.html', name=name)


if __name__ == '__main__':
    app.run()


