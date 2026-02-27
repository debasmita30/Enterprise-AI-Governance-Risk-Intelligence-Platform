import re

def detect_pii(text):
    email_pattern = r'\S+@\S+'
    phone_pattern = r'\d{10}'
    
    if re.search(email_pattern, text):
        return True
    if re.search(phone_pattern, text):
        return True
    return False

def data_sensitivity_score(text):
    if detect_pii(text):
        return 80
    return 30