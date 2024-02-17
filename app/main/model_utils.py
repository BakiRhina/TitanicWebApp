import joblib


class Model():
  def __init__(self, model_path):
    self.model = joblib.load(model_path)

  def _upload_model(self):
