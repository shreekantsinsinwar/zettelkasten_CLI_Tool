# 🧠 Zettelkasten CLI Tool — Your Second Brain in the Terminal

A minimal, file-based Zettelkasten-style note-taking tool built in Python.  
It lets you quickly create, search, view, and link atomic notes using simple commands.  
Perfect for devs, writers, thinkers, and anyone tired of forgetting ideas.

---

## 🚀 Features

✅ Create timestamped atomic notes with a title  
✅ Link notes using IDs or tags  
✅ Search notes with keywords  
✅ View a note by its unique ID  
✅ Clean and extendable Python structure  
✅ No database needed — all notes stored as `.md` files  
✅ Works offline — local Zettelkasten vault

---

## ⚙️ How It Works

Each note is saved in the `notes/` folder with a unique filename:
```bash
[ID]_[Title_Sanitized].md

---

## 🚀 How to Use

### 📥 Create a new note
```bash
python zettel.py --new "What is Zettelkasten?"
python zettel.py --list
python zettel.py --view 20250704_1442
python zettel.py --search "irrelevant"
python zettel.py --link 20250704_1442 20250704_1330


# Title
<timestamp>

Your content here...

#tags #linked_notes


git clone https://github.com/shreekantsinsinwar/zettelkasten-cli.git
cd zettelkasten-cli

python zettelkasten.py --help
```

## CLI Usage
```bash
python zettelkasten.py --new "Your Title" "Some content here"
python zettelkasten.py --view 20250704153522
python zettelkasten.py --search keyword
python zettelkasten.py --link 20250704153522 20250704144501
