import spacy
import re
import logging

# Load the spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Configure logging to track the pseudonymization process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to detect and extract named entities
def extract_named_entities(text):
    doc = nlp(text)
    entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    return entities

# Function to detect phone numbers
def detect_phone_numbers(text):
    return re.findall(r'\+\d{1,2}\s?\(\d{1,3}\)\s?\d{3,4}-\d{4}', text)

# Function to detect email addresses
def detect_emails(text):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# Main function to pseudonymize the text
def pseudonymize_text(text):
    logging.info("Starting text pseudonymization.")
    
    # Extract named entities
    ent_positions = extract_named_entities(text)
    
    # Detect phone numbers and emails
    phone_numbers = detect_phone_numbers(text)
    email_addresses = detect_emails(text)

    # Iterate over the named entities to pseudonymize them
    for start, end, label in reversed(ent_positions):
        if label in ['PERSON', 'GPE']:  # Person (PERSON) and Geopolitical Entity (GPE)
            text = text[:start] + '*' * (end - start) + text[end:]
            logging.info(f"Pseudonymized entity: {text[start:end]} (Type: {label})")

    # Pseudonymize phone numbers
    for phone_number in phone_numbers:
        text = text.replace(phone_number, '*' * len(phone_number))
        logging.info(f"Pseudonymized phone number: {phone_number}")

    # Pseudonymize email addresses
    for email_address in email_addresses:
        text = text.replace(email_address, '*' * len(email_address))
        logging.info(f"Pseudonymized email: {email_address}")
    
    logging.info("Pseudonymization complete.")
    return text

# Function to test the pseudonymization process
def test_pseudonymization():
    # Example text
    example_text = (
        "The applicant John Doe, living at Maple Street, has the phone number "
        "+1 (415) 555-1234, and his email is john.doe@example.com. He also visited New York."
    )

    # Call the function to pseudonymize the example text
    pseudonymized_text = pseudonymize_text(example_text)

    # Display the results
    print("Original text:")
    print(example_text)
    print("\nPseudonymized text:")
    print(pseudonymized_text)

# Run the test
if __name__ == "__main__":
    test_pseudonymization()
