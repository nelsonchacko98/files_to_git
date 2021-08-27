import os
from pdf2image import convert_from_path

def convert(file,outputDir) :
    if not os.path.exists(outputDir) :
        os.makedirs(outputDir)
    
    pages = convert_from_path(file,500)
    counter = 0 
    file_name = file.replace(".pdf","/")
    
    for page in pages : 
        if not os.path.exists(outputDir+file_name) :
            os.makedirs(outputDir+file_name)
        myfile = outputDir+file_name+str(counter)+".jpg"
        counter = counter + 1
        page.save(myfile,"jpeg")    
    
file = "1620387138667-MEGHA_RESUME.pdf"
outputDir = "images/"
convert(file,outputDir)