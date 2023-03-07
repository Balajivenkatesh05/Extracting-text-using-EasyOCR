import streamlit as st
import easyocr
from PIL import Image
import numpy as np


st.title('Extracting Business Card Data with OCR')
upload_img = st.file_uploader(label='Upload the image (JPG,PNG,JPEG)', type=['png', 'jpg', 'jpeg'])  #image uploading

  #easyOCR text conversion

if upload_img is not None:
    input_img = Image.open(upload_img)  #to show the uploaded image using pillow module
    st.image(input_img)
    st.balloons()
    reader = easyocr.Reader(['en'])
    result = reader.readtext(np.array(input_img), detail=0)  #reading the image text ignoring the details
    y = st.table(result)


else:
    st.write('Please upload an image')

upload_button = st.button('Upload to Database')
