import joblib
import numpy as np


class Model():
  def __init__(self, model_path):
    self.model = self._load_model(model_path)


  
  def process_data(self, data_list):
    # 1. data_list comes as: [sex, fare, cabin]
    # 2. The model was trained using the following order of features:
    # [passengerId, pclass, sex, fare, cabin]
    # To get predictions the model needs to be fed with the
    #SAME features in the same order.

    data = data_list
    passengerId = 400 #FIXME - To be removed
    pclass = self._get_pclass(data[1])
    data_def = [passengerId, pclass, data[0], data[1], data[2]]
    return np.array([data_def])
  
  def get_prediction(self, ndarray_values):
    prediction = self.model.predict(ndarray_values)
    
    return prediction

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
    


  
