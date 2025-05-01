'''
The python file contains functions to parse the input data 
and convert it into a format suitable for the model.
This parser currently supports PDFs and Word Documents.

Author: Dibyajyoti Jena
'''
from pypdf import PdfReader
import re

def extract_text_from_pdf(file_path):
    pdfReader = PdfReader(file_path)
    text = ""

    for page in pdfReader.pages:
        text = page.extract_text() + "\n"

    return text.strip()

def number_of_pages(file_path):
    try:
        pdfReader = PdfReader(file_path)
        num_pages = len(pdfReader.pages)
        if num_pages > 1:
            raise ValueError("The resume should not be more than 1 page.")
    except Exception as e:
        print(f"Error reading number of pages: {e}")
        num_pages = 0
    return num_pages


def extract_phoneNumber(file_path):
    try:
        pdfReader = PdfReader(file_path)
        phonePattern = re.compile(r"\+?\d{0,2}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
        phoneNumber = phonePattern.findall(extract_text_from_pdf(file_path))
    except Exception as e:
        print(f"Error reading phone number: {e}")
        phoneNumber = []
    return phoneNumber


if __name__ == "__main__":
    file_path = "../test/DibyajyotiJena_Resume.pdf"
    num_pages = number_of_pages(file_path)
    phone_number = extract_phoneNumber(file_path)
    print(f"Phone number found: {phone_number}")
    print(f"Number of pages in the resume: {num_pages}")

