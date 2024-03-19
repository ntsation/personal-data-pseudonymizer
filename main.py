import spacy
import re

nlp = spacy.load("pt_core_news_sm")

def pseudonimizar_texto(texto):
    doc = nlp(texto)
    ent_positions = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    phone_numbers = re.findall(r'\+\d{2}\s?\(\d{2}\)\s?\d{4,5}-\d{4}', texto)
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)

    for start, end, label in reversed(ent_positions):
        if label in ['PER', 'LOC']:
            texto = texto[:start] + '*' * (end - start) + texto[end:]
    
    for phone_number in phone_numbers:
        texto = texto.replace(phone_number, '*' * len(phone_number))
    
    for email_address in email_addresses:
        texto = texto.replace(email_address, '*' * len(email_address))
    
    return texto

texto_exemplo = "O aplicante de nome José da Silva que mora na Rua das marrecas e tem número de telefone +55 (21) 9999-1234. Contato pelo e-mail jose@example.com."

texto_pseudonimizado = pseudonimizar_texto(texto_exemplo)

print(texto_pseudonimizado)
