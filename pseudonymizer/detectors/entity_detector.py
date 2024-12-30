import spacy

class NamedEntityDetector:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_named_entities(self, text):
        doc = self.nlp(text)
        return [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
