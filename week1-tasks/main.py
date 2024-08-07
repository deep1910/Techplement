import json
import re
contacts = []
def main():
    load_contacts_from_file()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List All Contacts")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            if validate_phone(phone) and validate_email(email):
                add_contact(name, phone, email)
                print("Contact Added")
            else:
                print("Invalid phone number or email.")
        
        elif choice == '2':
            name = input("Enter name to search: ")
            contact = search_contact(name)
            if contact:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("Contact not found.")
        
        elif choice == '3':
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            if (not new_phone or validate_phone(new_phone)) and (not new_email or validate_email(new_email)):
                if update_contact(name, new_phone, new_email):
                    print("Contact updated.")
                else:
                    print("Contact not found.")
            else:
                print("Invalid phone number or email.")
        
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == '5':
            list_contacts()
        
        elif choice == '6':
            save_contacts_to_file()
            break
        
        else:
            print("Invalid choice, please try again.")

# import json

def save_contacts_to_file(filename='contacts.json'):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

def load_contacts_from_file(filename='contacts.json'):
    global contacts
    try:
        with open(filename, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

def list_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]

def update_contact(name, new_phone=None, new_email=None):
    contact = search_contact(name)
    if contact:
        if new_phone:
            contact['phone'] = new_phone
        if new_email:
            contact['email'] = new_email
        return True
    return False

def search_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return contact
    return None

def add_contact(name, phone, email):
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)


def validate_phone(phone):
    pattern = re.compile(r"^\+?\d{10,15}$")
    return pattern.match(phone)

def validate_email(email):
    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    return pattern.match(email)


if __name__ == "__main__":
    main()
