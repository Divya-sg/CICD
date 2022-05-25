from fastapi import Request,FastAPI
from pydantic import BaseModel
import uvicorn
import json
import tensorflow as tf
import numpy as np
from PIL import Image
import requests

app = FastAPI()

class SummaryRequest(BaseModel):
    img_path_url: str

def load_model():
  model = tf.keras.models.load_model('./models/')
  return model

classes=['angular_leaf_spot','bean_rust','healthy']

model = load_model()

def decode_img(image):
  img = tf.image.decode_jpeg(image, channels=3)
  img = tf.image.resize(img,[224,224])
  return np.expand_dims(img, axis=0)

#path = st.text_input('Enter Image URL to Classify.. ','https://beanipm.pbgworks.org/sites/pbg-beanipm7/files/styles/picture_custom_user_wide_1x/public/AngularLeafSpotFig1a.jpg')

@app.get('/')
def home():
    return {"message": "Hello World"}

@app.post("/classify")
def getclassify(user_request_in: SummaryRequest):
    payload = {"img_path_url":user_request_in.img_path_url}
    content = requests.get(payload['img_path_url']).content
    label =np.argmax(model.predict(decode_img(content)),axis=1)
    return {
        'class': classes[label[0]]
    }
    #summ = get_summary(payload,tokenizer,model)
    #summ["Device"]= torch_device

# def lambda_handler(event, context):
#    # TODO implement
#    model = load_model()
#    path = event['path']
#    content = requests.get(path).content
#    label =np.argmax(model.predict(decode_img(content)),axis=1)
#    return {
#        'statusCode': 200,
#        'body': classes[label[0]]
#    }
