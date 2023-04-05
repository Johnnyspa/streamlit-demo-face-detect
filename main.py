import streamlit as st
import cv2
from PIL import Image
import numpy as np

st.title("contour detection")



def blackandwhite(image):
    bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    return bw_img

def addframe(image):
    frame_h=image.shape[0];
    frame_w=image.shape[1];
    image=cv2.rectangle(image, (0,0), (frame_h , frame_v/20), (255,255,255), -1)
    return image

uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    converted_img = np.array(image.convert('RGB'))

    frame_h=converted_img.shape[0]
    frame_v=converted_img.shape[1]

    st.write(frame_h, frame_v)

    #add frame
    framed = cv2.rectangle(converted_img, (0,0), (frame_v, int(frame_h/20)), (255,255,255), -1)
    framed = cv2.rectangle(framed, (0, 0), (int(frame_v/20), frame_h), (255, 255, 255), -1)
    framed = cv2.rectangle(framed, (int(frame_v/1.05), 0), (frame_v, frame_h), (255,255,255), -1)
    framed = cv2.rectangle(framed, (0, int(frame_h/1.05)), (frame_v, frame_h), (255, 255, 255), -1)




    gray_scale = cv2.cvtColor(framed, cv2.COLOR_RGB2GRAY)
    slider = st.slider("SET Confidence Threshold", min_value=1, max_value=255, step=1, value=140)
    ret, thresh = cv2.threshold(gray_scale, slider, 255, cv2.THRESH_BINARY_INV)

    st.image(thresh, width=1000)

    Contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);
    image_copy = image.copy();
    conv_img = np.array(image_copy.convert('RGB'))

    image_copy2=((conv_img*0)+255)
    #frame_h2 = image_copy2.shape[0]
    #frame_v2 = image_copy2.shape[1]


    solve = cv2.drawContours(conv_img, Contours, -1, (0, 0, 255), 5);
    st.image(solve, width=1000)
    Area_total = 0
    for index, cnt in enumerate(Contours):
        area = cv2.contourArea(cnt)
        #perimeter = cv2.arcLength(cnt, True)
        Area_total = Area_total + area

    solve2 = cv2.drawContours(image_copy2, Contours, -1, (0, 0, 255), 5);
    st.image(solve2, width=1000)

    st.text("Total Area is"); st.write(Area_total); st.text("squared pixels")