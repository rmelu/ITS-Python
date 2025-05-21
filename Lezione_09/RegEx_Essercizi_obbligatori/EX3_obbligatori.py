import re
def mask_numbers(text):
    pattern = r"\d+"
    masked_text = re.sub(pattern, "###", text)
    return masked_text
text = "Il codice è 12345 e la data è 2025. L'anno prossimo sarà il 2026."
masked_text = mask_numbers(text)
print(masked_text)