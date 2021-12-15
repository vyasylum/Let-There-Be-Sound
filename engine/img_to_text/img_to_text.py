import pyautogui
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open("demo1.png")

str = pytesseract.image_to_string(img)

print(str)