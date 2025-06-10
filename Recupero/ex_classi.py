class Contact:

    def __init__(self, nome:str, phone_nummber: list[str]) -> None:
        self.nome = nome
        self.phone_number = phone_nummber

    def create_contact(self,name: str, phone_numbers: list[str]):
        if not isinstance(name, str) or not isinstance(phone_numbers, list):
            raise ValueError("Invalid input types.")
        return {"name": name, "phone numbers": phone_numbers}

    def add_phone_number(self, contact_name:str, phone_number:str) -> dict[str, list[str]]:
        if contact_name == self.nome:
            self.phone_number.append(phone_number)
        else:
            raise ValueError("Contact name does not match.")
        
    def remove_phone(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        if contact_name == self.nome:
            if phone_number in self.phone_number:
                self.phone_number.remove(phone_number)
            else:
                raise ValueError("Phone number not found.")
        else:
            raise ValueError("Contact name does not match.")
        
    def update_phone(self,contact_name: str, old_phone_number: str,new_phone_number: str) ->dict[str, list[str]]:
        if contact_name == self.nome:
            if old_phone_number in self.phone_number:
                index = self.phone_number.index(old_phone_number)
                self.phone_number[index] = new_phone_number
            else:
                raise ValueError("Olde phone number not found.")
        else:
            raise ValueError("Contact name does noy match.")
        
    def list_contacts(self) -> str:
        return f"Contacts: {self.nome}, Phone Numbers: {', '.join(self.phone_number)}"
    
    def list_phone_numbers(self, contact_name: str):
        if contact_name == self.nome:
            return f"Phone Number for {self.nome}: {', '.join(self.phone_number)}"
        else:
            raise ValueError("Contacts name does not match.")
        
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:

        contact_found = []

        for contact in self.phone_number:
            if phone_number in contact:
                contact.found.append(contact)
                if contact_found:
                    return f"Contact found: {', '.join(contact_found)}"
                return "No contact found whith that phone number."
            
            
if __name__ == "__main__":
    print("---Inizio Test---")
    rubrica = Contact("Alice", ["958309904", "5894359"])
    print(rubrica.list_contacts())
    rubrica.add_phone_number("Mia", "9485374")
    print(rubrica.list_contacts())
    rubrica.remove_phone("tchala", "9859034859")
    print(rubrica.list_contacts())
    rubrica.update_phone("kikki", "85738973")
    print(rubrica.list_contacts())
    print(rubrica.list_phone_numbers("yole", "9534870"))
    print(rubrica.search_contact_by_phone_number("98306832986"))
    print("---Fine Test---")



        

