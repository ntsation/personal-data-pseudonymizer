import unittest
from pseudonymizer.pseudonymizer_service import PseudonymizerService

class TestPseudonymizer(unittest.TestCase):
    def setUp(self):
        self.service = PseudonymizerService()

    def test_pseudonymize_text(self):
        text = "John Doe's email is john.doe@example.com and his phone is +1 (123) 456-7890."
        pseudonymized = self.service.pseudonymize_text(text)
        self.assertNotIn("John Doe", pseudonymized)
        self.assertNotIn("john.doe@example.com", pseudonymized)
        self.assertNotIn("+1 (123) 456-7890", pseudonymized)

if __name__ == "__main__":
    unittest.main()
