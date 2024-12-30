from pseudonymizer.detectors.entity_detector import NamedEntityDetector
from pseudonymizer.detectors.phone_detector import PhoneDetector
from pseudonymizer.detectors.email_detector import EmailDetector
from pseudonymizer.logger import setup_logging

class TextProcessor:
    def __init__(self):
        self.logger = setup_logging()
        self.entity_detector = NamedEntityDetector()
        self.phone_detector = PhoneDetector()
        self.email_detector = EmailDetector()

    def pseudonymize(self, text):
        self.logger.info("Starting text pseudonymization.")

        # Detect entities, phone numbers, and emails
        entities = self.entity_detector.extract_named_entities(text)
        phone_numbers = self.phone_detector.detect_phone_numbers(text)
        email_addresses = self.email_detector.detect_emails(text)

        # Replace entities with asterisks
        for start, end, label in reversed(entities):
            if label in ['PERSON', 'GPE']:
                text = text[:start] + '*' * (end - start) + text[end:]
                self.logger.info(f"Pseudonymized entity: {text[start:end]} (Type: {label})")

        # Replace phone numbers
        for phone in phone_numbers:
            text = text.replace(phone, '*' * len(phone))
            self.logger.info(f"Pseudonymized phone number: {phone}")

        # Replace email addresses
        for email in email_addresses:
            text = text.replace(email, '*' * len(email))
            self.logger.info(f"Pseudonymized email: {email}")

        self.logger.info("Pseudonymization complete.")
        return text
