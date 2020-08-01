import builtins
original_open = open

def bin_open(filename, mode='rb'):       # note, the default mode now opens in binary
    return original_open(filename, mode)

from PIL import Image
import pytesseract
pytesseract.tesseract_cmd = r'C:\Users\Тимофей\PycharmProjects\GoToHackaton\venv\Lib\site-packages\tesseract.exe'
Image.open(r"C:\Users\Тимофей\PycharmProjects\GoToHackaton\imgs\2nWUZ-dxOYI.jpg").save('abc.png')

img = Image.open('abc.png')

try:
    builtins.open = bin_open
    bts = pytesseract.image_to_string(img)
finally:
    builtins.open = original_open

print(str(bts, 'cp1252', 'ignore'))