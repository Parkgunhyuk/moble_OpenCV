from PIL import Image
import pytesseract
 
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
 
str = pytesseract.image_to_string(Image.open('.\data\sample.jpg'), lang='kor')
 
print(str)
