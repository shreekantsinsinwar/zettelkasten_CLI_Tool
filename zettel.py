import argparse
import os
import time

# Directory to store notes
NOTES_DIR = "notes"

# Ensure notes directory exists
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)


def create_note(title, content):
    """Creates a new note with timestamp"""
    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = f"{title}_{timestamp}.txt"
    filepath = os.path.join(NOTES_DIR, filename)
    
    with open(filepath, "w") as file:
        file.write(content)
    
    print(f"[✔] Note created: {filename}")


def list_notes():
    """Lists all notes in the notes directory"""
    notes = os.listdir(NOTES_DIR)
    if not notes:
        print("[ℹ] No notes found.")
    else:
        print("[🗂] Available Notes:")
        for note in sorted(notes):
            print(f" - {note}")


def view_note(filename):
    """Displays content of a note"""
    filepath = os.path.join(NOTES_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            content = file.read()
        print(f"\n--- {filename} ---\n{content}\n")
    else:
        print(f"[✘] Note '{filename}' not found.")


def search_notes(keyword):
    """Searches all notes for a keyword"""
    found = False
    for note in os.listdir(NOTES_DIR):
        filepath = os.path.join(NOTES_DIR, note)
        with open(filepath, "r") as file:
            content = file.read()
            if keyword.lower() in content.lower():
                print(f"[🔍] Found in: {note}")
                found = True
    if not found:
        print(f"[✘] No notes contain the keyword '{keyword}'.")


def link_notes(source, target):
    """Adds a reference of target note inside source note"""
    source_path = os.path.join(NOTES_DIR, source)
    target_path = os.path.join(NOTES_DIR, target)
    
    if os.path.exists(source_path) and os.path.exists(target_path):
        with open(source_path, "a") as file:
            file.write(f"\n\n[🔗 Linked to: {target}]\n")
        print(f"[✔] Linked '{source}' to '{target}'.")
    else:
        print("[✘] One or both note files do not exist.")


def main():
    parser = argparse.ArgumentParser(description="🧠 Zettelkasten Note-Taking CLI Tool")

    parser.add_argument('--new', nargs=2, metavar=('TITLE', 'CONTENT'), help='Create a new note')
    parser.add_argument('--list', action='store_true', help='List all notes')
    parser.add_argument('--view', metavar='FILENAME', help='View a specific note')
    parser.add_argument('--search', metavar='KEYWORD', help='Search for a keyword in notes')
    parser.add_argument('--link', nargs=2, metavar=('SOURCE', 'TARGET'), help='Link one note to another')

    args = parser.parse_args()

    if args.new:
        create_note(args.new[0], args.new[1])
    elif args.list:
        list_notes()
    elif args.view:
        view_note(args.view)
    elif args.search:
        search_notes(args.search)
    elif args.link:
        link_notes(args.link[0], args.link[1])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
