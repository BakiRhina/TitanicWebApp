from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html', result=None)

@main_bp.route('/process_form', methods=['POST'])
def process_form():
    sex = request.form.get('sex')
    cabin = request.form.get('cabin')
    age = request.form.get('age')

    # Perform operations with the received data
    # For demonstration purposes, let's just echo the data
    result_message = f"Survived Titanic? Sex: {sex}, Cabin: {cabin}, Age: {age}"

    return render_template('index.html', result=result_message)
