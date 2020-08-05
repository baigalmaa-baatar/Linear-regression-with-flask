from flask import Flask, render_template, request, jsonify
import joblib
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

app.config.from_object(os.environ["APP_SETTINGS"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

from models import Result

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            regressor = joblib.load("linear_regression_model.joblib")
            # Get years of experience from input form index.html
            data = dict(request.form.items())
            year_of_experience = float(data['YearsExperience'])
            prediction = regressor.predict([[year_of_experience]])
        except ValueError:
            return jsonify("Please enter a number.")
        result = Result(
            YearsExperience=float(year_of_experience),
            Prediction=float(prediction)
        )
        db.session.add(result)
        db.session.commit()
        return render_template('predicted.html', prediction=float(prediction))


if __name__ == '__main__':
    app.run(debug=True)
