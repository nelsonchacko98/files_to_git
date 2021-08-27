from numpy.core.shape_base import block
import detect_text_from_block
import find_contours
import cv2
import re

# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\nelson.c\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def check_block(blocks) :
    personal_block = []

    for i,block in enumerate(blocks) :

        emails = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
        phone = "(?:(?:\+|0{0,2})91(\s*[\\-]\s*)?|[0]?)?[789]\d{2}\s*\d{3}\s*\d{4}"    
        check_regex = re.findall(emails, block)

        if(len(check_regex)!=0) :
            personal_block.append(block)
            
    return personal_block


if __name__ == '__main__' :
    image = cv2.imread("Resume_Nelson_page-0001.jpg")
    cnts = find_contours.get_contours(image)
    blocks = detect_text_from_block.get_blocks(image,cnts)
    
    pblocks = check_block(blocks)
    for block in pblocks :
        print(block)
