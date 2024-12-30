from pseudonymizer.pseudonymizer_service import PseudonymizerService

def main():
    example_text = (
        "The applicant John Doe, living at Maple Street, has the phone number "
        "+1 (415) 555-1234, and his email is john.doe@example.com. He also visited New York."
    )

    service = PseudonymizerService()
    pseudonymized_text = service.pseudonymize_text(example_text)

    print("Original text:")
    print(example_text)
    print("\nPseudonymized text:")
    print(pseudonymized_text)

if __name__ == "__main__":
    main()
