# Personal Data Pseudonymizer

This is a small Python script that uses the spaCy library to identify named entities in an English text and then replaces these entities with pseudonyms (asterisks). The goal is to protect the privacy of personal information in the text, such as names, locations, phone numbers, and email addresses.

## Features

- Identification of named entities such as **people (PERSON)** and **locations (GPE)** in the text.
- Pseudonymization of people's names and locations by replacing them with asterisks (`*`).
- Removal of phone numbers and email addresses by replacing them with asterisks (`*`).
  
The pseudonymization process helps in ensuring privacy, making it useful for scenarios like data analysis, content sharing, or protecting personally identifiable information (PII).

## Requirements

Before running the script, ensure you have the following installed:

- **Python 3.x**
- **spaCy** library
- **spaCy English model (`en_core_web_sm`)**

### Installation

1. Install the `spaCy` library by running:

    ```bash
    pip install spacy
    ```

2. Download the English model for `spaCy` by running:

    ```bash
    python -m spacy download en_core_web_sm
    ```

3. Clone or download this repository, and place the script `pseudonymization.py` in your desired folder.

### Running the Script

1. Open a terminal or command prompt.
2. Navigate to the folder where the `pseudonymization.py` file is located.
3. Run the script with:

    ```bash
    python pseudonymization.py
    ```

The script will process the sample text and print the original and pseudonymized texts in the terminal.

### Sample Output

```text
Original text:
The applicant John Doe, living at Maple Street, has the phone number +1 (415) 555-1234, and his email is john.doe@example.com. He also visited New York.

Pseudonymized text:
The applicant **** ** ***, living at ***** Street, has the phone number ************, and his email is ********@*****.***. He also visited ***** York.
```

## How it Works

1. **Entity Extraction**: The script uses spaCy to extract named entities, such as people's names (`PERSON`) and geographical locations (`GPE`).
2. **Pseudonymization**: It replaces these identified entities with asterisks. The same approach is used for phone numbers and email addresses, which are also detected using regular expressions.
3. **Logging**: The script logs the pseudonymization process, providing details about which entities were replaced.

## Use Cases

- **Data Privacy**: This script helps ensure that personally identifiable information (PII) is masked or pseudonymized before sharing or analyzing text data.
- **GDPR & Data Protection**: Useful for ensuring compliance with data protection regulations like GDPR (General Data Protection Regulation) or LGPD (Lei Geral de Proteção de Dados).
- **Text Anonymization**: Ideal for anonymizing content that contains sensitive personal information, such as survey responses, customer feedback, or legal documents.

## References

[Medium - Demystifying Individual Privacy](https://medium.com/@nick.ruberg/demystifying-individual-privacy-anonymization-and-pseudonymization-in-the-age-of-data-protection-0bf7055fc0fd)
