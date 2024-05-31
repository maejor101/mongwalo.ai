import pytesseract

def recognize_handwriting(image):
    custom_config = r'--oem 1 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text
