from genericpath import exists
from pdf2image import convert_from_path
import os 
from tqdm import tqdm as tq


def convert(file,outputDir) :
    if not os.path.exists(outputDir) :
        os.makedirs(outputDir)
    
    try :
        pages = convert_from_path(file,500)
        file_name = file.replace(".pdf","/")
        counter = 0
        
        for page in pages : 
            
            if not os.path.exists(outputDir+file_name) :
                os.makedirs(outputDir+file_name)
                
            myfile = outputDir+file_name+str(counter)+".jpg"
            counter = counter + 1
            page.save(myfile,"jpeg")    
            
    except : 
        print(f"some error occuered with {file}")
        
        
        
def convert_in_dir(inputDir,outputDir) : 
    
    pdf_files = []
    
    for file in os.listdir(inputDir) :
        if file.endswith(".pdf") :
            pdf_files.append(file)
            
    for file in tq(pdf_files) : 
        file_path = inputDir+file
        convert(file_path,outputDir)
        
    
# file = "1620387138667-MEGHA_RESUME.pdf"
inputDir = "TestResumes/"
outputDir = "TestImages/"

# convert(file,outputDir)
convert_in_dir(inputDir,outputDir)
