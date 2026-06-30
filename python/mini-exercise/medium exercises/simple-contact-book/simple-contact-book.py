import csv
import os

# Constants
SEPARATOR = "=" * 50
SEPARATOR2 = "-" * 30
CONTACTS_FILE = "contacts.csv"


def load_contacts():
    """Load contacts from CSV file"""
    contacts = []
    if not os.path.exists(CONTACTS_FILE):
        return contacts

    with open(CONTACTS_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            contacts.append(row)
    return contacts


def save_contacts(contacts):
    """Save contacts to CSV file"""
    with open(CONTACTS_FILE, "w", newline="") as f:
        fieldnames = ["name", "phone", "email"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)


def add_contact():
    """Add a new contact"""
    print("\nADD NEW CONTACT")
    name = input("Name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return

    phone = input("Phone number: ").strip()
    email = input("Email: ").strip()

    contacts = load_contacts()

    # Check if contact already exists
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"❌ Contact '{name}' already exists!")
            return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added!")


def list_contacts():
    """List all contacts"""
    contacts = load_contacts()

    if not contacts:
        print("\n No contacts found. Add some first!")
        return

    print("\n📋 CONTACT LIST")
    print(SEPARATOR)
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']}")
        print(f"   📞 {contact['phone'] if contact['phone'] else 'No phone'}")
        print(f"   ✉️  {contact['email'] if contact['email'] else 'No email'}")
        print(SEPARATOR2)


def search_contacts():
    """Search for contacts by name"""
    search_term = input("\n🔍 Enter name to search: ").strip().lower()

    if not search_term:
        print("❌ Please enter a search term")
        return

    contacts = load_contacts()
    matches = [c for c in contacts if search_term in c["name"].lower()]

    if not matches:
        print(f"❌ No contacts found matching '{search_term}'")
        return

    print(f"\nSEARCH RESULTS ({len(matches)} found)")
    print(SEPARATOR)
    for contact in matches:
        print(f"\n📌 {contact['name']}")
        if contact['phone']:
            print(f"   📞 {contact['phone']}")
        if contact['email']:
            print(f"   ✉️  {contact['email']}")


def delete_contact():
    """Delete a contact"""
    contacts = load_contacts()

    if not contacts:
        print("\n No contacts to delete")
        return

    print("\nDELETE CONTACT")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']}")

    try:
        choice = int(input("\nEnter number to delete (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(contacts):
            deleted = contacts.pop(choice - 1)
            save_contacts(contacts)
            print(f"✅ Deleted '{deleted['name']}'")
        else:
            print("❌ Invalid choice")
    except ValueError:
        print("❌ Please enter a valid number")


def main_menu():
    """Main menu loop"""
    while True:
        print("\n" + SEPARATOR)
        print("📞 CONTACT BOOK MENU")
        print(SEPARATOR)
        print("1. Add Contact")
        print("2. List All Contacts")
        print("3. Search Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nChoose (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-5")


# Run the contact book
if __name__ == "__main__":
    main_menu()