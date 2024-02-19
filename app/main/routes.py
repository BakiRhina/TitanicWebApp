from flask import Blueprint, render_template, request
from .model_utils import Model
from config import rf_model_path

# initialize model
model = Model(rf_model_path)

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():

    return render_template('home.html', result=None)

@main_bp.route('/', methods=['POST'])
def process_form():
    sex = request.form.get('sex')
    cabin = request.form.get('cabin')
    age = request.form.get('age') # Not used for now
    fare = request.form.get('fare')
    
    input_data = [sex, fare, cabin]

    # The model was trained using the following order of features:
    # [passengerId, pclass, sex, fare, cabin]
    # To get predictions the model needs to be fed with the
    #SAME features in the same order.

    result_text, prob_yes = model.get_prediction(input_data)

    return render_template('home.html', result=prob_yes, resultText = result_text)
  