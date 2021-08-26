import cv2 
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\nelson.c\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


if __name__ == '__main__' :
    im = cv2.imread('ROI_2.png',0)

    text = pytesseract.image_to_string(im)
    print(text)

