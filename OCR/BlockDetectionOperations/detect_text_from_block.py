import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import find_contours

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\nelson.c\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

im = cv2.imread("Resume_Nelson_page-0001.jpg")
image = im.copy()

cnts = find_contours.get_contours(image)

block_text = []
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    block = image[y:y+h, x:x+w]

    text = pytesseract.image_to_string(block)
    print(text)
    block_text.append(text)


for i,text in enumerate(block_text) :
    print(f"Block {i} : {text} \n")

# 