def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print(f"Contact {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    search_term = input("Enter Name or Phone Number to search: ")
    found_contacts = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    
    if not found_contacts:
        print("No contacts found.")
        return
    
    print("\nSearch Results:")
    for contact in found_contacts:
        print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")

def update_contact(contacts):
    search_term = input("Enter the Name or Phone Number of the contact to update: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Current details of {contact['name']}:")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            
            print("\nEnter new details (leave blank to keep current value):")
            contact['name'] = input(f"New Name [{contact['name']}]: ") or contact['name']
            contact['phone'] = input(f"New Phone Number [{contact['phone']}]: ") or contact['phone']
            contact['email'] = input(f"New Email [{contact['email']}]: ") or contact['email']
            contact['address'] = input(f"New Address [{contact['address']}]: ") or contact['address']
            
            print(f"Contact {contact['name']} updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    search_term = input("Enter the Name or Phone Number of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Deleting contact: {contact['name']}")
            contacts.pop(i)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")
#will be optimized
def main():
    contacts = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice!!!!!! Please select a valid option.")

if __name__ == "__main__":
    main()
