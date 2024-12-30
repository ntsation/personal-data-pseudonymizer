import re

class PhoneDetector:
    def detect_phone_numbers(self, text):
        return re.findall(r'\+\d{1,2}\s?\(\d{1,3}\)\s?\d{3,4}-\d{4}', text)
