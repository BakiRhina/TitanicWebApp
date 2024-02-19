import joblib
import numpy as np


class Model():
  def __init__(self, model_path):
    self.model = self._load_model(model_path)

  def get_prediction(self, input_data):
    numpy_data = self._process_data(input_data)
    prediction = self.model.predict(numpy_data)
    probability = self.model.predict_proba(numpy_data)
    prob_yes = probability[0][1]
    answer = 'yes' if prediction else 'no'
    return answer, prob_yes
  

  def _process_data(self, data_list):
    # 1. data_list comes as: [sex, fare, cabin]
    # 2. The model was trained using the following order of features:
    # [passengerId, pclass, sex, fare, cabin]
    # To get predictions the model needs to be fed with the
    #SAME features in the same order.

    data = data_list

    sex = int(data[0]) # String to int/bool
    fare = float(data[1]) # String to float
    cabin = int(data[2]) # String to int

    passengerId = 0 #FIXME - To be removed
    pclass = self._get_pclass(fare)

    data_def = [passengerId, pclass, sex, fare, cabin]
    return np.array([data_def])
  
  def _load_model(self, model_path):
    with open(model_path, 'rb') as file:
      model = joblib.load(file)
    return model
    
  def _get_pclass(self, fare):
    if fare < 70:
      return 1
    elif fare >= 70 and fare < 170:
      return 2
    else:
      return 3
    


  
