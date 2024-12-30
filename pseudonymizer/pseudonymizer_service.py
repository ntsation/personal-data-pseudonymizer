from pseudonymizer.text_processor import TextProcessor

class PseudonymizerService:
    def __init__(self):
        self.processor = TextProcessor()

    def pseudonymize_text(self, text):
        return self.processor.pseudonymize(text)
