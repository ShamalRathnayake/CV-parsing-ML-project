import re
import spacy
import phonenumbers
from models.candidate_profile import CandidateProfile


class ExtractionService:
    def __init__(self, parser):
        self.parser = parser
        self.nlp = spacy.load('en_core_web_sm')

    def extract_candidate_profile(self, file_path: str) -> CandidateProfile:
        # Step 1: Extract raw text from the file
        text = self.parser.parse(file_path)

        # Step 2: Extract structured fields
        name = self.extract_name(text)
        email = self.extract_email(text)
        phone = self.extract_phone_number(text)
        skills = self.extract_skills(text)
        education = self.extract_education(text)
        experience = self.extract_experience(text)

        # Step 3: Return structured object
        return CandidateProfile(
            name=name,
            emails=email,
            phone_numbers=phone,
            skills=skills,
            education=education,
            experience=experience
        )

    def extract_name(self, text: str) -> str:
        doc = self.nlp(text)
        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                return ent.text
        return None

    def extract_email(self, text: str) -> str:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        matches = re.findall(pattern, text)
        return matches

    def normalize_phone_number(self, number: str) -> str:
        if number.startswith('0'):
            return '+94' + number[1:]  # Assuming Sri Lanka as default
        if not number.startswith('+'):
            return '+' + number
        return number

    def extract_phone_number(self, text: str) -> str:
        phone_numbers = set()

        # Find rough candidates
        potential_numbers = re.findall(r'\+?\d[\d\s\-()]{7,}\d', text)

        for number in potential_numbers:
            # Remove spaces, dashes, parentheses
            cleaned_number = re.sub(r'[\s\-\(\)]', '', number)

            try:
                # Try parsing it as a phone number
                if not cleaned_number.startswith('+'):
                    # Assume it's Sri Lanka (+94) if no country code (You can change default_region if needed)
                    parsed_number = phonenumbers.parse(cleaned_number, "LK")
                else:
                    parsed_number = phonenumbers.parse(cleaned_number, None)

                # Validate if it's a real number
                if phonenumbers.is_valid_number(parsed_number):
                    formatted_number = phonenumbers.format_number(
                        parsed_number,
                        phonenumbers.PhoneNumberFormat.E164  # Example: +94778891312
                    )
                    phone_numbers.add(formatted_number)
            except phonenumbers.NumberParseException:
                continue

        return list(phone_numbers)
    def extract_skills(self, text: str) -> list:
        # Predefined list of common skills
        skills_list = [
            "Python", "Java", "JavaScript", "SQL", "Machine Learning", "Data Science", 
            "C++", "C#", "HTML", "CSS", "React", "Django", "Flask", "Docker", "AWS", 
            "Cloud", "Git", "Node.js", "Angular", "TensorFlow", "PyTorch", "Keras"
        ]

        skills = []

        # Loop through the skills list and check if they exist in the text
        for skill in skills_list:
            if skill.lower() in text.lower():
                skills.append(skill)

        return skills

    def extract_education(self, text: str) -> list:
        # TODO: Implement education extraction
        return []

    def extract_experience(self, text: str) -> list:
        # TODO: Implement experience extraction
        return []
