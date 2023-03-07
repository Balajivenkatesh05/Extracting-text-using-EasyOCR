import streamlit as st
import easyocr
from PIL import Image
import numpy as np
import re
import pandas as pd

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

    mail = []
    for i in result:
        if re.search(pattern= "[a-zA-Z0-9]{1,20}@[a-zA-Z0-9].[a-z]", string=str(result)):
            mail.append(re.search(pattern= "[a-zA-Z0-9]{1,20}@[a-zA-Z0-9].[a-z]", string=str(result)))
            break
    st.write(mail)

    phone = []
    for i in result:
        if re.search(pattern='\d{2,3}-\d{3}-\d{4}', string=str(result)):
            phone.append(re.search(pattern='\d{2,3}-\d{3}-\d{4}', string=str(result)))
            break
    st.write(phone)

    website = []
    for i in result:
        if re.search(pattern=r'[w]{2,3}', string=str(result)):
            website.append(re.search(pattern='[w]{2,3}[a-zA-Z]\.[a-z]{2,3}', string=str(result)))
            break
    st.write(website)

    pin_code = []
    for i in result:
        if re.findall(pattern='[0-9]{6}', string=str(result)):
            pin_code.append(re.search(pattern='[0-9]{6}', string=str(result)))
            break
    st.write(pin_code)

    designation = []
    for i in result:
        if re.findall(pattern='[a-zA-Z]{1,10}\s[*&][a-zA-Z]{1,10}', string=str(result)):
            designation.append((re.search(pattern='[a-zA-Z]{1,10}\s[*&][a-zA-Z]{1,10}', string=str(result))))
            break
    st.write(designation)

    name = []
    for i in result:
        if re.findall(pattern='[a-zA-Z]{1,10}', string=str(result)):
            name.append(re.search(pattern='[a-zA-Z]{1,10}', string=str(result)))
            break
    st.write(name)



    df = pd.DataFrame(data=[mail, phone, website, pin_code, designation, name], columns=['Mail', 'Phone', 'Website', 'Pincode', 'Designation', 'Name'])





else:
    st.write('Please upload an image')

upload_button = st.button('Upload to Database')
