import cv2
import numpy
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\nelson.c\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

config = r"--oem 3 --psm 6"

def detect_chars(img: numpy.ndarray) -> None :
    boxes = pytesseract.image_to_boxes(img,config=config)
    hImg,wImg,_ = img.shape

    for b in boxes.splitlines() : 
        b = b.split()

        x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])

        cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
        cv2.putText(img,b[0],(x,hImg-y+30),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

    cv2.imshow('Result',img)
    cv2.waitKey(0)

def detect_words(img:   numpy.ndarray) -> None :
    boxes = pytesseract.image_to_data(img,config=config)
    hImg,wImg,_ = img.shape

    for i,b in enumerate(boxes.splitlines()) :
        if i!=0 :
            b=b.split()
            if (len(b)) == 12 :
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
                cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(50,50,255),1)

    cv2.imshow('Result',img)
    cv2.waitKey(0)


if __name__ == '__main__' :
    img_raw = cv2.imread(r"C:\Users\nelson.c\dev\Text_OCR\images\ilovepdf_pages-to-jpg\Resume_Nelson_page-0001.jpg")
    img_raw = cv2.cvtColor(img_raw,cv2.COLOR_BGR2RGB)

    # detect_chars(img_raw)
    detect_words(img_raw)