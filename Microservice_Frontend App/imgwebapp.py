import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import json

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Leaf Image Classifier")
st.text("Provide URL of any leaf Image")


path = st.text_input('Enter Image URL to Classify.. ','https://beanipm.pbgworks.org/sites/pbg-beanipm7/files/styles/picture_custom_user_wide_1x/public/AngularLeafSpotFig1a.jpg')
if path is not None:
    content = requests.get(path).content
    st.write("Predicted Class :")
    with st.spinner('classifying.....'):
      response = requests.post("http://3.87.237.159/classify", data = json.dumps({'img_path_url' : path}))
      #response = requests.get("http://3.87.237.159/")
      label=response.json()
      st.write(label['class'])
    st.write("")
    image = Image.open(BytesIO(content))
    st.image(image, caption='Classifying Bean Image', use_column_width=True)
