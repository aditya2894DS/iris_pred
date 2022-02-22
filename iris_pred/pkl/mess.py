# from .mess2 import msg2
from django.conf import settings
import os
import pickle

def open_model(file_name):
  model_path = os.path.join(settings.BASE_DIR, 'iris\pkl', os.path.basename(file_name))
  if os.path.exists(model_path):
    print('Loading model')
    model = pickle.load(open(model_path), 'rb')
    return model