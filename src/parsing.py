"""
This module provides functions to extract and process data from PDF files,
specifically resumes. It includes functionality to extract text, count the
number of pages, and find phone numbers, email addresses, and section headers
within the document. The module is designed to ensure that resumes do not
exceed one page and supports parsing of common resume sections.

Author: Dibyajyoti Jena
"""
from pypdf import PdfReader
import re

def extract_text_from_pdf(file_path):
    pdfReader = PdfReader(file_path)
    text = ""

    for page in pdfReader.pages:
        extract = page.extract_text()
        if extract:
            text += extract + "\n"
        else:
            print(f"Warning: No text found on page {page.number + 1}.")

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
        phonePattern = re.compile(r"\+?\d{0,2}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
        phoneNumber = phonePattern.findall(extract_text_from_pdf(file_path))
    except Exception as e:
        print(f"Error reading phone number: {e}")
        phoneNumber = []
    return phoneNumber

def extract_email(file_path):
    try:
        emailPattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
        emails = emailPattern.findall(extract_text_from_pdf(file_path))
    except Exception as e:
        print(f"Error reading email: {e}")
        emails = []
    return emails

def extract_section_header(file_path):
    try:
        headingPattern = re.compile(r"\b(Experience|Education|Skills|Projects|Certifications|Awards|Achievements)\b", re.IGNORECASE)
        headings = headingPattern.findall(extract_text_from_pdf(file_path))
    except Exception as e:
        print(f"Error reading section headers: {e}")
        headings = []
    return headings

def extract_links(file_path):
    try:
        linkPattern = re.compile(r"(https?://)?(www\.)?(linkedin\.com|github\.com)/[a-zA-Z0-9_-]+")
        links = linkPattern.findall(extract_text_from_pdf(file_path))
        links = ["".join(link) for link in links]
    except Exception as e:
        print(f"Error reading links: {e}")
        links = []
    return links

def extract_skills(file_path, skills_list):
    try:
        content = extract_text_from_pdf(file_path).lower()
        skills_found = [skill for skill in skills_list if skill.lower() in content]
    except Exception as e:
        print(f"Error reading skills: {e}")
        skills_found = []
    return skills_found

def extract_experience(file_path):
    try:
        experiencePattern = re.compile(r"(?i)(\b(?:intern|developer|engineer|manager|analyst|consultant)\b).*?(\b(?:at|for)\b.*?\b[A-Z][a-zA-Z]+\b)")
        experience = experiencePattern.findall(extract_text_from_pdf(file_path))
    except Exception as e:
        print(f"Error reading experience: {e}")
        experience = []
    return experience

def extract_education(file_path):
    try:
        educationPattern = re.compile(r"(?i)(\b(Bachelor|Master|PhD|Diploma|Degree)\b.*?\b(?:in|of)\b.*?\b[A-Z][a-zA-Z]+\b)")
        education_details = educationPattern.findall(extract_text_from_pdf(file_path))
    except Exception as e:
        print(f"Error reading education: {e}")
        education_details = []
    return education_details

'''
This is a test function to check the functionality of the above functions.
It is not part of the module and should be removed in production.
'''
if __name__ == "__main__":
    file_path = "../test/DibyajyotiJena_Resume.pdf"
    num_pages = number_of_pages(file_path)
    phone_number = extract_phoneNumber(file_path)
    email = extract_email(file_path)
    section_header = extract_section_header(file_path)
    links = extract_links(file_path)
    skills = ["Programming Language", "Technical Skills", "Python", "Golang"]
    skills_found = extract_skills(file_path, skills)
    experience = extract_experience(file_path)
    education = extract_education(file_path)
    print(f"Education details found: {education}")
    print(f"Skills found: {skills_found}")
    print(f"Experience found: {experience}")
    print(f"Links found: {links}")
    print(f"Section headers found: {section_header}")
    print(f"Email found: {email}")
    print(f"Phone number found: {phone_number}")
    print(f"Number of pages in the resume: {num_pages}")
    print("\n")

