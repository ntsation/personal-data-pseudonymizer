import spacy
import re

# Carrega o modelo do spaCy para o idioma português
nlp = spacy.load("pt_core_news_sm")

# Função para pseudonimizar o texto
def pseudonimizar_texto(texto):
    # Processa o texto com o modelo do spaCy
    doc = nlp(texto)
    # Extrai as posições das entidades nomeadas (pessoas, locais, etc.)
    ent_positions = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    # Encontra números de telefone no texto
    phone_numbers = re.findall(r'\+\d{2}\s?\(\d{2}\)\s?\d{4,5}-\d{4}', texto)
    # Encontra endereços de e-mail no texto
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)

    # Itera sobre as posições das entidades nomeadas, substituindo os nomes por asteriscos
    for start, end, label in reversed(ent_positions):
        if label in ['PER', 'LOC']:  # Verifica se a entidade é uma pessoa ou um local
            texto = texto[:start] + '*' * (end - start) + texto[end:]  # Substitui o texto pelo pseudônimo
    
    # Substitui os números de telefone por asteriscos
    for phone_number in phone_numbers:
        texto = texto.replace(phone_number, '*' * len(phone_number))
    
    # Substitui os endereços de e-mail por asteriscos
    for email_address in email_addresses:
        texto = texto.replace(email_address, '*' * len(email_address))
    
    return texto

# Texto de exemplo
texto_exemplo = "O aplicante de nome José da Silva que mora na Rua das marrecas e tem número de telefone +55 (21) 9999-1234. Contato pelo e-mail jose@example.com."

# Chama a função para pseudonimizar o texto de exemplo
texto_pseudonimizado = pseudonimizar_texto(texto_exemplo)

# Imprime o texto pseudonimizado
print(texto_pseudonimizado)
