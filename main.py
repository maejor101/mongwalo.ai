from src.pdf_to_images import pdf_to_images
from src.preprocess_image import preprocess_image
from src.recognize_handwriting import recognize_handwriting
import os

def extract_handwriting_from_pdf(pdf_path, output_path):
    images = pdf_to_images(pdf_path)
    extracted_text = []
    for img in images:
        preprocessed_img = preprocess_image(img)
        text = recognize_handwriting(preprocessed_img)
        extracted_text.append(text)
    with open(output_path, 'w') as f:
        f.write("\n".join(extracted_text))

if __name__ == "__main__":
    pdf_path = 'input/sample.pdf'
    output_path = 'output/recognized_text.txt'
    if not os.path.exists('output'):
        os.makedirs('output')
    extract_handwriting_from_pdf(pdf_path, output_path)
    print(f"Handwritten text extracted to {output_path}")
