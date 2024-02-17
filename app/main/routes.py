from flask import Blueprint, render_template, request
from model_utils import Model
from ....TitanicWebApp.config import rf_model_path


main_bp = Blueprint('main', __name__)
model = Model(rf_model_path)

@main_bp.route('/')
def index():
    return render_template('home.html', result=None)

@main_bp.route('/process_form', methods=['POST'])
def process_form():
    sex = request.form.get('sex')
    cabin = request.form.get('cabin')
    age = request.form.get('age')
    fare = request.form.get('fare')
    
    # The model was trained using the following order of features:
    # [passengerId, pclass, sex, fare, cabin]
    # To get predictions the model needs to be fed with the
    #SAME features in the same order.

    input_data = [sex, fare, cabin]
    numpy_data = model.process_data(input_data)
    answer = model.get_prediction(numpy_data)


    # Perform operations with the received data
    # For demonstration purposes, let's just echo the data
    result_message = f"Survived Titanic? {answer}"

    return render_template('home.html', result=result_message)
  