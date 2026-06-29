import json
import os
from datetime import datetime

# Constants
SEPARATOR = "=" * 50
SEPARATOR2 = "-" * 30


NOTE_FILES = "notes.json"

def load_notes():
    """Load note from file, return list of dicts"""
    if not os.path.exists(NOTE_FILES):
        return []
    with open(NOTE_FILES, "r") as f:
        return json.load(f)

def save_notes(notes):
    """Save notes list to file."""
    with open(NOTE_FILES, "w") as f:
        json.dump(notes, f, indent=4)

def add_note():
    """Add a new note"""
    print("\n ADD NEW NOTE")
    title = input("Title: ").strip()
    if not title:
        print("❌ Title cannot be empty!")
        return

    content = input("Content: ").strip()
    if not content:
        print("❌ Content cannot be empty!")
        return

    notes = load_notes()
    notes.append({
        "title": title,
        "content": content,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_notes(notes)
    print(f"✅ Note '{title}' added!")

def list_note():
    """List all notes"""
    notes = load_notes()
    if not notes:
        print("\n No notes yet. Add some first!")
        return

    print("\n YOUR NOTES")
    print(SEPARATOR)
    for i, note in enumerate(notes, 1):
        print(f" {i}. {note['title']}")
        print(f"  {note.get('created', 'Unknown date')}")
        print(f"  {note['content'][:50]}..." if len(note['content']) > 50 else f" {note['content']}")
        print(SEPARATOR2)


def view_note():
    """View a specific note"""
    notes = load_notes()
    if not notes:
        print("\n Not notes to view")
        return

    list_note()
    try:
        choice = int(input("\nEnter note Number to view: "))
        if 1 <= choice <= len(notes):
            note = notes[choice -1]
            print("\n" + SEPARATOR)
            print(f" {note['title']}")
            print(f" {note.get('created', 'Unknown date')}")
            print(SEPARATOR)
            print(note['content'])
            print(SEPARATOR)
        else:
            print("❌ Invalid note number")
    except ValueError:
        print("❌ Please enter a valid number")

def delete_note():
    """Delete a note"""
    notes = load_notes()
    if not notes:
        print("\n No notes to delete")
        return

    list_note()
    try:
        choice = int(input("\nEnter note to delete (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(notes):
            deleted = notes.pop(choice - 1)
            save_notes(notes)
            print(f"✅ Deleted note: '{deleted['title']}")
        else:
            print(f"❌ Invalid note number")
    except ValueError:
        print("❌ Please enter a valid number")

def search_notes():
    """Search notes by title or content"""
    search_term = input("\n🔍 Enter search term: ").strip().lower()
    if not search_term:
        print("❌ Please enter a search term")
        return

    notes = load_notes()
    matches = []
    for note in notes:
        if (search_term in note['title'].lower()) or search_term in note['content'].lower():
            matches.append(note)

    if not matches:
        print(f"❌ No notes found matching '{search_term}'")
        return

    print(f"\n SEARCH RESULTS ({len(matches)} found)")
    print(SEPARATOR)
    for i, note in enumerate(matches, 1):
        print(f"{i}. {note['title']}")
        print(f"  {note['content'][:50]}...")
        print()

def main_menu():
    """Main menu loop"""
    while True:
        print("1. Add Note")
        print("2. List All Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("\nChoose (1-5): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            list_note()
        elif choice == "3":
            view_note()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("\n👋 Your notes are saved.")
            break
        else:
            print("❌ Invalid choice. please enter 1-6")


if __name__ == "__main__":
    print(SEPARATOR)
    print("WELCOME TO NOTE TAKING APP")
    print(SEPARATOR)
    main_menu()
