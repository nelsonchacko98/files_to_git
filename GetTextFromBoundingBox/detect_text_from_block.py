import cv2
import numpy as np
import pytesseract
import find_contours

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\nelson.c\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def get_blocks(image:np.array,cnts:list) -> list :
    """
    @para : image imported via opencv method imread()
    @para : list of contour values
    
    @result : list containing block text 
    """
    block_list = []
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        block = image[y:y+h, x:x+w]

        text = pytesseract.image_to_string(block)
        block_list.append(text)
    return block_list

if __name__ == "__main__":
    im = cv2.imread("athira.PNG")
    image = im.copy()

    cnts = find_contours.get_contours(image)
    blocks = get_blocks(image,cnts)
    for i,text in enumerate(blocks) :
        print(f"Block {i} : {text} \n")
    


