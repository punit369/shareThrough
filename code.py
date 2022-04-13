from googletrans import Translator
from fpdf import FPDF
from os import listdir
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

global failed 

failed = []

def img_to_pdf(img_path,pdf_path):
    try:
        img = cv2.imread(img_path)
        text = pytesseract.image_to_string(img)
        translator = Translator()
        text_es = translator.translate(text, src='en', dest='es')
        text = (text_es.text)    
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=12)
        text = text.encode('latin-1', 'replace').decode('latin-1')
        for line in text.split('\n'):
            pdf.cell(200, 7, txt=line, ln=1, align='L')
        pdf.output(pdf_path)

    except:
        failed.append(img_path)
        print(img_path+"Not applicable")

for i in listdir('images'):
    img,pdf ='images/'+i,'pdfs/'+i.split('.')[0]+'.pdf'
    print(img,pdf)
    img_to_pdf(img,pdf)
