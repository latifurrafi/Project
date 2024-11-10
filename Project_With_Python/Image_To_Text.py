import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

image = Image.open('/home/rafi/VSCODE/CodeCraze/Project_With_Python/test.png')

text = pytesseract.image_to_string(image)

print("Extracted Text:\n", text)
