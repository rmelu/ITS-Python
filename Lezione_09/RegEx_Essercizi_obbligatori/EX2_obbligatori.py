import re
def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    return emails
text = "conttataci a info@azienda.com oppure support@help.org. Per maggiori informazioni scrivi a sales.dept@another-co.net"
emails_trovate = extract_emails(text)
print(emails_trovate)


'''

def estrai_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)'''