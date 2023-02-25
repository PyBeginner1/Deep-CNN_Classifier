import streamlit as st
import pandas as pd
from PIL import Image
from io import StringIO
import numpy as np
import tensorflow as tf

"Deep Classifier Project"

#model = tf.keras.models.load_model("D:/iNeuron/Complete Project/Deep-CNN_Classifier/artifacts/training/model.h5")
model = tf.keras.models.load_model("model.h5")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    img_resize = image.resize((224,224))
    img_array = np.array(img_resize)
    img_array_expand = np.expand_dims(img_array, axis = 0)
    result = model.predict(img_array_expand)
    

    if result[0][0] == 1:
        st.image(image, caption='Predicted: Cat')
    else:
        st.image(image, caption='Predicted: Dog')
