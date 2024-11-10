import pytesseract
from PIL import Image

# Set the correct path to Tesseract (for Linux)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Load your image
image = Image.open('/home/rafi/VSCODE/CodeCraze/Project_With_Python/test.png')

# Extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:\n", text)
