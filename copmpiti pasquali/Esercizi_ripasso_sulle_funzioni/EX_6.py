from typing import Dict, Optional

def create_contact(name: str, email: Optional[str] = None, telefono: Optional[int] = None) -> Dict[str, Optional[str | int]]:
    contact = {"profile": name}
    if email is not None:
        contact["email"] = email
    if telefono is not None:
        contact["telefono"] = telefono
    return contact

def update_contact(dictionary: Dict[str, Optional[str | int]], name: str, email: Optional[str] = None, telefono: Optional[int] = None) -> Dict[str, Optional[str | int]]:
    if dictionary.get("profile") == name:
        if email is not None:
            dictionary["email"] = email
        if telefono is not None:
            dictionary["telefono"] = telefono
    return dictionary

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))

	